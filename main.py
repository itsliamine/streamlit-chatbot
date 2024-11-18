from src.data_preprocessing.preprocess import preprocess_csv

raw_filepath = "data/bdd.csv"
preprocessed_filepath = "data/preprocessed.csv"

if __name__ == "__main__":
    preprocess_csv(raw_filepath, preprocessed_filepath)
    print("Cleaned data saved.")