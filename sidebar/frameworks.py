import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#94A3B8;
        font-size:11px;
        letter-spacing:1px;
        margin-bottom:8px;
    }

    .framework-divider{
        height:1px;
        background:rgba(59,130,246,.15);
        margin-bottom:12px;
    }

    .framework-group{
        color:white;
        font-weight:600;
        font-size:14px;
        margin-bottom:10px;
    }

    .framework-item{
        display:flex;
        align-items:center;
        gap:10px;
        padding:7px 10px;
        color:#E2E8F0;
        border-radius:6px;
        margin-bottom:3px;
    }

    .framework-item-active{
        display:flex;
        align-items:center;
        gap:10px;
        padding:9px 12px;
        border-radius:6px;
        margin-bottom:6px;
        color:white;
        font-weight:600;
        background:linear-gradient(
            90deg,
            #6D28D9,
            #7C3AED
        );
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

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-group">⌄ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-item-active">🔴 Ferry PS</div>',
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