# 🎬 Content-Based Movie Recommender

This project is a **content-based movie recommendation system** built using NLP techniques and metadata from the TMDB 5000 dataset. The system suggests similar movies based on title, overview, genres, keywords, cast, and crew using cosine similarity on processed tags.

---

## 🚀 Features

- 📄 Uses metadata such as `overview`, `genres`, `cast`, `crew`, and `keywords`
- 🧠 NLP-based tag generation and text preprocessing
- 📐 Cosine similarity using `CountVectorizer`
- 💾 Model saved with `pickle` for deployment or future use
- 🔍 Recommend top 5 similar movies to a given title

---

## 📦 Dataset

Dataset used: [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🧰 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/content-based-movie-recommender.git
   cd content-based-movie-recommender
2 Install dependencies:

pip install -r requirements.txt
Download and place the TMDB CSV files in the root directory.

## 🧪 How It Works
# Step 1: Preprocessing
Extracts metadata fields like genres, cast, crew, keywords

Keeps only top 3 cast members and director

Combines all relevant metadata into a single tags column

Applies lowercase, tokenization, and stemming

# Step 2: Feature Extraction
Uses CountVectorizer (Bag of Words) on processed tags

Limits to top 5000 features and removes English stop words

# Step 3: Similarity Calculation
Computes pairwise cosine similarity between movies
# 📚 Dependencies
pandas

numpy

scikit-learn

nltk

# 📜 License
This project is open-source and available under the MIT License.

# 🙋‍♂️ Author
Sunny Wazeer

Feel free to contribute or raise issues!
