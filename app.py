import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# load lstm model
model=load_model('next_word_lstm.h5')

# load the tokenizer
with open('tokenizer.pickel','rb') as handle:
    tokenizer=pickle.load(handle)
    
# Define the predict_next_word function (example implementation)
def predict_next_word(model, tokenizer, text, max_sequence_len):
    sequence = tokenizer.texts_to_sequences([text])[0]
    padded_sequence = pad_sequences([sequence], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(padded_sequence, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=-1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

# streamlit app
st.title("Next word Prediction ")
input_text=st.text_input("Enter the sentence in the file :","to be or not to be")
if st.button("Predict"):
    max_sequence_len=model.input_shape[1]+1
    next_word=predict_next_word(model,tokenizer,input_text,max_sequence_len)
    st.write(f"Next word : {next_word}")