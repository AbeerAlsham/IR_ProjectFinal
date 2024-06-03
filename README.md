# Information Retrieval System

This repository contains an information retrieval (IR) system that allows users to search and retrieve relevant documents from a given corpus. The system is designed to handle different datasets, perform text processing, and rank documents based on query relevance.

## Features

- **Multiple Dataset Support**: The system supports multiple datasets (e.g., "Antique" and "Lotte").
- **Query Processing**: Includes text normalization, tokenization, and lemmatization.
- **Query Suggestion**: Provides query suggestions based on user input.
- **Text Processing**: Normalizes text, removes punctuation, and lemmatizes words.
- **TF-IDF Representation**: Calculates TF-IDF vectors for queries and documents.
- **Document Ranking**: Employs cosine similarity to rank documents based on relevance.
- **Translation**: Translates queries to English (optional).
- **Multilingual Support**: Capable of translating queries into English for processing.


## Project Structure

The project is organized into several directories, each serving a specific purpose in the IR system:

- `application`: Initialization scripts for setting up the application.
- `configuration`: Configuration settings for datasets and language preferences.
- `controller`: Controllers for handling search and refinement logic.
- `datasource`: Data access layer for documents and queries.
- `engine`: Core search engine components including query processing and ranking.
- `services`: Houses various text processing services (e.g., lemmatization, punctuation removal), representation, Utility services such as IO operations, and translation.
- `static`: Static files for the web interface, including JavaScript and CSS.
- `templates`: HTML templates for rendering the search interface and results.
- `app.py`: The main Flask application entry point.

Each directory contains Python modules that encapsulate the functionality relevant to their respective areas of concern.

## Getting Started

To get the IR system up and running on your local machine, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/AbeerAlsham/IR_ProjectFinal.git
   ```
2. **Install Dependencies**:
   Navigate to the project directory and install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
3. **Load Data**:
   Ensure that your datasets are loaded and preprocessed data structures (like vectorizers and inverted indexes) are in place.
4. **Run the Application**:
   Start the Flask server by running:
   ```sh
   python app.py
   ```

## Usage

Once the application is running, you can interact with the IR system in the following ways:

- **Web Interface**:
  Open your web browser and navigate to `http://localhost:5000` to use the search interface.
- **Search Documents**:
  Enter a query, select a dataset, and specify the language (if applicable). Click "Search" to retrieve documents.
- **Query Suggestions**:
  Enter a query, select a dataset.  Click "Suggestions" to retrieve query suggestions.


---