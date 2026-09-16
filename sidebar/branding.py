import streamlit as st


def render_branding():

    logo_col, text_col = st.columns(
        [1, 3],
        gap="small"
    )

    with logo_col:
        st.image(
            "assets/logo.png",
            width=60
        )

    with text_col:
        st.markdown(
            """
            **DESIGN**  
            **INTELLIGENCE HUB**
            """
        )

        st.caption(
            "Design Smarter. Deliver Better."
        )

    st.divider()