# Next-Word Prediction with LSTM

This project is a simple Streamlit-based web app that predicts the next word in a sentence using an LSTM model. The model is trained on a text dataset and generates the most likely next word based on the input sequence.

## Features

- **LSTM model**: Uses a pre-trained LSTM model to predict the next word in a sentence.
- **Streamlit interface**: User-friendly interface for easy input and interaction.
- **Text preprocessing**: Tokenizer and padding to preprocess the input for prediction.

## Requirements

To run this project, you need the following Python packages:

```bash
streamlit==1.25.0
numpy==1.24.2
tensorflow==2.10.0
pickle-mixin
```

You can install them using the following command:

```bash
pip install streamlit numpy tensorflow pickle-mixin
```

## How to Run the Project

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/next-word-prediction-lstm.git
    cd next-word-prediction-lstm
    ```

2. **Download the model and tokenizer**:

   - Make sure to place your `next_word_lstm.h5` (LSTM model) and `tokenizer.pickle` files in the project directory.

3. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

4. **Use the app**:

   - Once the app is running, enter a partial sentence in the text box and click "Predict" to generate the next word.

## Project Structure

```bash
|-- app.py                    # Streamlit app code
|-- next_word_lstm.h5          # Pre-trained LSTM model
|-- tokenizer.pickle           # Tokenizer for text preprocessing
|-- README.md                  # Project documentation
```
