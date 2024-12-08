# import streamlit as st
# import pickle

# # Load your trained model
# with open("results_df.pkl", "rb") as f:
#     model = pickle.load(f)

# # App title
# st.title("Simple Machine Learning App")

# # User inputs
# st.header("Enter your input values:")
# feature1 = st.number_input("Feature 1")
# feature2 = st.number_input("Feature 2")
# # Add more input fields as needed

# # Predict button
# if st.button("Predict"):
#     # Convert inputs into a 2D array for model
#     input_data = [[feature1, feature2]]
#     prediction = model.predict(input_data)
#     st.success(f"Prediction: {prediction[0]}")
