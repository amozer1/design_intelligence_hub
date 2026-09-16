import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-divider{
        border-top:1px solid rgba(255,255,255,.08);
        margin:6px 0 12px 0;
    }

    .framework-title{
        color:#B7C7DA;
        font-size:14px;
        font-weight:700;
        margin-bottom:10px;
    }

    .framework-group{
        color:white;
        font-size:15px;
        font-weight:600;
        margin-bottom:4px;
    }

    .framework-item{
        color:white;
        font-size:14px;
        line-height:1.2;
        padding:2px 0 2px 20px;
    }

    .framework-active{
        background:linear-gradient(
            90deg,
            #6624D6,
            #7C3AED
        );
        border-radius:8px;
        color:white;
        font-size:14px;
        font-weight:600;
        padding:8px 12px;
        margin:4px 0;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
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

    st.markdown("<div style='height:6px'></div>",
                unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-group">▾ UU DD&amp;B Framework</div>',
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