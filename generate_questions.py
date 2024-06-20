import pandas as pd
import random

# Load the data
file_path = 'Data/clean_data.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Define a function to generate patient-specific queries and responses based on the data
def generate_patient_queries(data, num_examples=100):
    symptoms_list = [
        "headache", "fever", "cough", "sore throat", "muscle pain", "fatigue",
        "nausea", "vomiting", "diarrhea", "rash", "shortness of breath", 
        "chest pain", "dizziness", "loss of taste", "loss of smell", 
        "joint pain", "swelling", "itching", "redness", "blurred vision"
    ]
    
    pairs = []
    
    for _ in range(num_examples):
        random_row = data.sample(1).iloc[0]
        medicine_name = random_row['NOM']
        side_effects = random_row['effet indesirable']
        
        symptom1, symptom2 = random.sample(symptoms_list, 2)
        
        # Generate a "What medicine can I take for these symptoms?" query
        context = f"I have {symptom1} and {symptom2}. What medicine can I take?"
        response = f"You might consider taking {medicine_name} for symptoms like {symptom1} and {symptom2}."
        pairs.append((context, response))
        
        # Generate a "Can I take this medicine if I have these symptoms?" query
        context = f"Can I take {medicine_name} if I have {symptom1} and {symptom2}?"
        response = f"{medicine_name} can be taken if you have symptoms like {symptom1} and {symptom2}, but it's best to consult with a doctor."
        pairs.append((context, response))
        
        # Generate a "What are the side effects of this medicine?" query
        if pd.notna(side_effects):
            context = f"What are the side effects of {medicine_name}?"
            response = f"The side effects of {medicine_name} include {side_effects}."
            pairs.append((context, response))
    
    return pairs

# Generate 100 context-response pairs
generated_pairs = generate_patient_queries(data, num_examples=100)

# Convert pairs to DataFrame
generated_pairs_df = pd.DataFrame(generated_pairs, columns=['Context', 'Response'])

# Save to Excel
output_file_100_examples_patient = 'dialog_agent_100_examples_patient.xlsx'
generated_pairs_df.to_excel(output_file_100_examples_patient, index=False)

print(f"Generated pairs saved to {output_file_100_examples_patient}")
