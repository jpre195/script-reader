import streamlit as st


def main():
    st.title(body="Script Reader", anchor=False, text_alignment="center")

    cols = st.columns(2)

    with cols[0].container(border=True):
        st.header(body="Script", anchor=False, text_alignment="center")
        script = st.text_area(label="Script")

    with cols[1].container(border=True):
        st.header(body="Roles", anchor=False, text_alignment="center")

    go_btn = st.button(label="Go", key="go", type="primary")


if __name__ == "__main__":
    main()
