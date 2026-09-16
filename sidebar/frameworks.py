import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#B7C7DA;
        font-size:14px;
        font-weight:600;
        letter-spacing:.5px;
        margin-bottom:6px;
    }

    .framework-divider{
        height:1px;
        background:rgba(80,120,255,.15);
        margin-bottom:10px;
    }

    .framework-group{
        color:white;
        font-size:15px;
        font-weight:600;
        margin:0;
        padding:0 0 4px 0;
    }

    .framework-item{
        color:#E2E8F0;
        font-size:14px;
        line-height:1.2;
        padding:3px 0 3px 18px;
        margin:0;
    }

    .framework-active{
        background:linear-gradient(
            90deg,
            #6624D6,
            #7C3AED
        );

        border-radius:6px;

        color:white;
        font-size:14px;
        font-weight:600;

        padding:8px 12px;

        margin:2px 0 4px 0;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">⌄ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">⚪ Pennington Flash</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">⚪ Davyhulme ASP4</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:4px'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">⌄ UU DD&amp;B Framework</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-active">🔴 Ferry PS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟠 Rossall Outfall</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟢 Flass Lane</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟡 Tally Ho</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item">🟢 Eccleston Bridge</div>',
        unsafe_allow_html=True
    )