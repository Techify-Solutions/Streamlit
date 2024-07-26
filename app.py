# Import sqlite3 and pandas
import sqlite3
import pandas as pd
import streamlit as st

# Connect to the database and create table if not exists
def init_db():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (author TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, date DATE NOT NULL)''')
    c.close()
    conn.close()

# Define a function to add a new post
def add_post(author, title, content, date):
    conn = None
    c = None
    try:
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('INSERT INTO posts (author, title, content, date) VALUES (?,?,?,?)', (author, title, content, date))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c:
            c.close()
        if conn:
            conn.close()

# Define a function to get all the posts
def get_all_posts():
    conn = None
    c = None
    data = []
    try:
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT * FROM posts')
        data = c.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c:
            c.close()
        if conn:
            conn.close()
        return data

# Define a function to get a post by title
def get_post_by_title(title):
    conn = None
    c = None
    data = None
    try:
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT * FROM posts WHERE title=?', (title,))
        data = c.fetchone()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c:
            c.close()
        if conn:
            conn.close()
        return data

# Define a function to delete a post
def delete_post(title):
    conn = None
    c = None
    try:
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('DELETE FROM posts WHERE title=?', (title,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c:
            c.close()
        if conn:
            conn.close()

# Initialize the database
init_db()

# Streamlit app
# Define some HTML templates for displaying the posts
title_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author: {}</h6>
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

post_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<h6>Author: {}</h6>
<h6>Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;">
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

# Create a sidebar menu with different options
menu = ["Home", "View Posts", "Add Post", "Search", "Manage"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected option
if choice == "Home":
    st.title("Welcome to my blog")
    st.write("This is a simple blog app built with streamlit and python.")
    st.write("You can view, add, search, and manage posts using the sidebar menu.")
    st.write("Enjoy!")

elif choice == "View Posts":
    st.title("View Posts")
    st.write("Here you can see all the posts in the blog.")
    posts = get_all_posts()
    for post in posts:
        st.markdown(title_temp.format(post[1], post[0], post[2][:50] + "..."), unsafe_allow_html=True)
        if st.button("Read More", key=post[1]):
            st.markdown(post_temp.format(post[1], post[0], post[3], post[2]), unsafe_allow_html=True)

elif choice == "Add Post":
    st.title("Add Post")
    st.write("Here you can add a new post to the blog.")
    with st.form(key="add_form"):
        author = st.text_input("Author")
        title = st.text_input("Title")
        content = st.text_area("Content")
        date = st.date_input("Date")
        submit = st.form_submit_button("Submit")
    if submit:
        add_post(author, title, content, date)
        st.success("Post added successfully")

elif choice == "Search":
    st.title("Search")
    st.write("Here you can search for a post by title or author.")
    query = st.text_input("Enter your query")
    if query:
        posts = get_all_posts()
        results = [post for post in posts if query.lower() in post[0].lower() or query.lower() in post[1].lower()]
        if results:
            st.write(f"Found {len(results)} matching posts:")
            for result in results:
                st.markdown(title_temp.format(result[1], result[0], result[2][:50] + "..."), unsafe_allow_html=True)
                if st.button("Read More", key=result[1]):
                    st.markdown(post_temp.format(result[1], result[0], result[3], result[2]), unsafe_allow_html=True)
        else:
            st.write("No matching posts found")

elif choice == "Manage":
    st.title("Manage")
    st.write("Here you can delete posts or view some statistics.")
    titles = [post[1] for post in get_all_posts()]
    title = st.selectbox("Select a post to delete", titles)
    if st.button("Delete"):
        delete_post(title)
        st.success("Post deleted successfully")
    if st.checkbox("Show statistics"):
        posts = get_all_posts()
        df = pd.DataFrame(posts, columns=["author", "title", "content", "date"])
        st.write("Number of posts:", len(posts))
        st.write("Number of authors:", len(df["author"].unique()))
        st.write("Most recent post:", df["date"].max())
        st.write("Oldest post:", df["date"].min())
        st.write("Posts by author:")
        author_count = df["author"].value_counts()
        st.bar_chart(author_count)

# Add initial test posts only if this script is run as the main module
if __name__ == "__main__":
    # add_post('Jyoti', 'Django vs Flask', 'This post is about Django vs Flask', '2023-12-05')
    # add_post('Jaimin', 'Artificial Intelligence', 'This post is about Artificial Intelligence', '2024-01-02')
    # add_post('Jeevansh', 'TalkPython', 'This post is about TalkPython', '2024-01-23')
    # print(get_all_posts())
    # print(get_post_by_title('Artificial Intelligence'))
    # delete_post('TalkPython')
    # print(get_all_posts())
    pass
# To run the Streamlit app, execute the following command in the terminal:
# streamlit run app.py
