# KU mini Search Engine

[![Python](https://img.shields.io/badge/python-3.1-blue.svg)](https://www.python.org/) [![HTML5](https://img.shields.io/badge/HTML5-5!-orange.svg)](https://html.com/) [![CSS3](https://img.shields.io/badge/CSS3-3!-green.svg)](https://www.w3schools.com/css/) [![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)](https://www.javascript.com/) [![NLTK](https://img.shields.io/badge/NLTK-%3E%3D-blue.svg)](https://www.nltk.org/)

**Description:**

This project implements a search engine that crawls web pages, processes them, and allows users to search for information using Boolean queries and the Vector Space Model.

**Features:**

  * **Web crawling:** Uses a multi-threaded web crawler to efficiently gather web pages from specified domains.
  * **Document preprocessing:** Removes HTML tags, converts text to lowercase, removes stop words, and performs stemming.
  * **Inverted index:** Constructs an inverted index for efficient document retrieval.
  * **Search functionality:** Supports Boolean queries and the Vector Space Model for ranked retrieval.
  * **Term proximity:** Integrates term proximity into search scoring for better results.
  * **Relevance feedback:** Allows users to provide feedback on search results to improve future queries.

**Technologies:**

  * Python 3.1
  * HTML
  * CSS
  * JavaScript
  * NLTK library

**Installation:**

1.  Clone the repository:
    ```bash
    git clone [https://github.com/jaypal1-7/Ku-search-engine.git](https://github.com/jaypal1-7/Ku-search-engine.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

**Usage:**

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Enter your search query.
3.  (Optional) Provide relevance feedback to improve search results.

**Contributing:**

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request to the main repository.
