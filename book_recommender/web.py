import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="wide"
)

books = pd.read_csv("Books.csv")
ratings = pd.read_csv("Ratings.csv")

data = pd.merge(ratings, books, on="ISBN")

data.columns = data.columns.str.strip()

st.sidebar.title("📖 Book Recommender")
st.sidebar.write("Find your next favorite book!")

st.markdown(
    "<h1 style='text-align: center;'>📚 Smart Book Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Powered by Kaggle Dataset</p>",
    unsafe_allow_html=True
)

book_list = data["Book-Title"].dropna().unique()
selected_book = st.selectbox("📘 Select a book you like:", book_list)

def recommend_books(book_name):
    book_info = data[data["Book-Title"] == book_name].iloc[0]
    author = book_info["Book-Author"]

    recommendations = data[
        (data["Book-Author"] == author) &
        (data["Book-Title"] != book_name)
    ].drop_duplicates("Book-Title")

    return recommendations.head(5)

if st.button("✨ Recommend Books"):
    st.subheader("📖 You may also like")

    recs = recommend_books(selected_book)

    cols = st.columns(5)

    for idx, (_, row) in enumerate(recs.iterrows()):
        with cols[idx]:
            if "Image-URL-L" in row and pd.notna(row["Image-URL-L"]):
                st.image(row["Image-URL-L"], use_container_width=True)
            st.markdown(f"**{row['Book-Title']}**")
            st.caption(f"✍️ {row['Book-Author']}")

