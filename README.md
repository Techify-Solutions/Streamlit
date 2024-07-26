# Streamlit Blog App

This is a simple blog app built with Streamlit and Python. The app allows you to view, add, search, and manage blog posts.

## Features

- **Home:** Welcome page with a brief introduction.
- **View Posts:** See all the posts in the blog.
- **Add Post:** Add a new post to the blog.
- **Search:** Search for a post by title or author.
- **Manage:** Delete posts or view some statistics.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of your project and add any necessary environment variables.

5. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

- Open the app in your browser using the link provided by Streamlit.
- Use the sidebar to navigate through different sections.
- Add, view, search, and manage posts as per your requirement.

## Database

The app uses SQLite for storing blog posts. The database file (`blog.db`) is created automatically in the root directory.