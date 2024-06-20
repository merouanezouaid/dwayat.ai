import pandas as pd
import uuid, requests, random
from dataset_preparing import chat_bow, stopword_
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


dfs = pd.read_csv('Data\clean_data.csv', usecols=['NOM', 'contre indication', 'effet indesirable', 'précaution emploi', 'PPV', 'TAUX_REMBOURSEMENT'])


def potential_substance_chunk_detection2(text):
    text = text.title()

    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree:
            for token, pos in subtree.leaves():
                if pos == "NN" or pos == "NNP" or pos == "NNS":
                    current_chunk.append(token)
    return current_chunk

def detect_price_question(text):
    text = text.lower()
    list = ['cost', 'price', 'much', 'buy', 'worth', 'purchase']
    if any(word in text for word in list):
        return True
    else:
        return False
def detect_contraindication(text):
    text = text.lower()
    list = ['contraindication', 'condition']
    if any(word in text for word in list):
        return True
    else:
        return False

def detect_refunding(text):
    text = text.lower()
    list = ['refund', 'reimbursement', 'repayment', 'redemption', 'rebate']
    if any(word in text for word in list):
        return True
    else:
        return False

def detect_precaution(text):
    text = text.lower()
    list = ['precaution', 'safety', 'measure', 'caution', 'preventative measure', 'prevent']
    if any(word in text for word in list):
        return True
    else:
        return False
def detect_effects(text):
    text = text.lower()
    list = ['effect', 'negative effect', 'adverse effect', 'bad effect', 'side effects', 'undesirable effect']
    if any(word in text for word in list):
        return True
    else:
        return False

def substance_answer(text):
    org_chunks = potential_substance_chunk_detection2(text)
    effect_template = ["The adverse effects of {} are : \n {}", "{} can cause : \n {}", "{} may cause : \n {}", "Be careful with the following {}'s negative effects : \n {}"]
    price_template = ['{} costs about : {}', 'The price of {} is : {}', 'You can purchase {} at : {}']
    contraindication_template = ['You should not take {} if you have : {}', '{} should not be taken if you have : {}']
    refunding_template = ['When purchasing {} You are refunded at : {}', '{} is refunded by : {}']
    precaution_template = ['You should take the following precaution when taking {} : {}', 'if you are taking {} , pay attention to what follows : {}']
    if org_chunks:
        for i in org_chunks:
            r = stopword_(i)
            if r:
                r = r.upper()
                ans_row = dfs.index[dfs['NOM'].str.startswith(r)].tolist()
                ans_row_bis = dfs.index[dfs['NOM'].str.endswith(r)].tolist()
                x = set(ans_row) & set(ans_row_bis)
                if x:
                    row = x.pop()
                    if detect_price_question(text):
                        return random.choice(price_template).format(r, " ".join([dfs['PPV'][row], "DHS"]))
                    if detect_precaution(text):
                        return random.choice(precaution_template).format(r, dfs['précaution emploi'][row])
                    elif detect_contraindication(text):
                        return random.choice(contraindication_template).format(r, dfs['contre indication'][row])
                    elif detect_refunding(text):
                        return random.choice(refunding_template).format(r, str(dfs['TAUX_REMBOURSEMENT'][row]))
                    elif detect_effects(text):
                        return random.choice(effect_template).format(r, dfs['effet indesirable'][row])
                    else:
                        return "Sorry I didn't get your demand correctly, can you reformulate ?"
        return False
    return False


def bot_response(text):
    poten_ans = substance_answer(text)
    if poten_ans == False:
        answer = chat_bow(text)
        return answer
    else:
        return get_translation(poten_ans)


def get_translation(text_input):
    return text_input
    # tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    # model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

    # inputs = tokenizer(text_input, return_tensors="pt")

    # translated_tokens = model.generate(
    #     **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=30
    # )
    # print(tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0])
    # return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
