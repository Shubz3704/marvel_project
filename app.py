import streamlit as st
from marvel_package.marvel_api import fetch_character_by_id, fetch_character_list
from marvel_package.utils import apply_function

st.title("Marvel Characters Explorer")

# Sidebar for mode selection
mode = st.sidebar.selectbox("Choose an option", ["Fetch by Character ID", "List Characters"])

if mode == "Fetch by Character ID":
    st.header("Fetch Character by ID")
    character_id = st.text_input("Enter Character ID:")
    if st.button("Fetch Character"):
        if character_id:
            results = apply_function(fetch_character_by_id, character_id)
            if "error" in results:
                st.error(results["error"])
            else:
                st.json(results)
        else:
            st.warning("Please enter a valid character ID.")

elif mode == "List Characters":
    st.header("List Characters")
    limit = st.number_input("Number of characters to fetch:", min_value=1, max_value=100, value=10)
    offset = st.number_input("Offset:", min_value=0, value=0)
    name_filter = st.text_input("Filter by name (optional):")
    if st.button("Fetch Characters"):
        results = apply_function(fetch_character_list, limit, offset, name_filter)
        if "error" in results:
            st.error(results["error"])
        else:
            for character in results:
                st.subheader(character["name"])
                st.write(character.get("description", "No description available."))
