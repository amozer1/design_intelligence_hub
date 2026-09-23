import streamlit as st


def load_executive_summary_styles():

    st.markdown(
        """
        <style>

        /* Match sidebar palette */

        [data-testid="stVerticalBlockBorderWrapper"]{
            *ackground:#081322 !important;
    *       border:1px solid rgba(255,2*5,255,.08) !important;
           *border-radius:12px !important;
   *    }

        .stCaption{
       *    color:#9CA3AF !important;
    *   }

        </style>
        """*
        unsafe_allow_html=True
  * )