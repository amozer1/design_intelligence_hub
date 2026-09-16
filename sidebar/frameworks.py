import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#B8C7D9;
        font-size:13px;
        font-weight:600;
        letter-spacing:0.8px;
        margin-bottom:6px;
    }

    .framework-divider{
        height:1px;
        background:rgba(80,120,255,.15);
        margin-bottom:10px;
    }

    .framework-group{
        color:white;
        font-size:14px;
        font-weight:600;
        margin:0;
        padding:0 0 4px 0;
    }

    .framework-item{
        color:#E2E8F0;
        font-size:14px;
        line-height:1.2;
        padding:4px 0 4px 18px;
        margin:0;
    }

    .framework-active{
        background:linear-gradient(
            90deg,
            #6624D6 0%,
            #7C3AED 100%
        );
        border-radius:6px;
        color:white;
        font-size:14px;
        font-weight:600;
        padding:8px 12px;
        margin:2px 0 4px 0;
    }

    .framework-small-gap{
        height:4px;
    }

    </style>
    """, unsafe_allow_html=True)

    # -----------------------------------------
    # TITLE
    # -----------------------------------------

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-divider"></div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # ENTERPRISE
    # -----------------------------------------

    st.markdown(
        '<div class="framework-group">⌄&nbsp;&nbsp;UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">⚪&nbsp;&nbsp;Pennington Flash</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">⚪&nbsp;&nbsp;Davyhulme ASP4</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-small-gap"></div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------
    # DD&B
    # -----------------------------------------

    st.markdown(
        '<div class="framework-group">⌄&nbsp;&nbsp;UU DD&amp;B Framework</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-active">🔴&nbsp;&nbsp;Ferry PS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟠&nbsp;&nbsp;Rossall Outfall</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟢&nbsp;&nbsp;Flass Lane</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟡&nbsp;&nbsp;Tally Ho</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟢&nbsp;&nbsp;Eccleston Bridge</div>',
        unsafe_allow_html=True
    )