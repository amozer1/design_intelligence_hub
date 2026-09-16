import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#AFC0D8;
        font-size:14px;
        font-weight:600;
        letter-spacing:0.8px;
        margin-bottom:6px;
    }

    .framework-divider{
        height:1px;
        background:rgba(80,120,255,.18);
        margin-bottom:10px;
    }

    .framework-group{
        color:#FFFFFF;
        font-size:14px;
        font-weight:600;
        margin:0;
        padding:2px 0 6px 0;
    }

    .framework-item{
        color:#D9E3F0;
        font-size:14px;
        margin:0;
        padding:5px 0 5px 16px;
        line-height:1.2;
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

        padding:10px 12px;
        margin:4px 0 5px 0;
    }

    .framework-space{
        height:4px;
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
        '<div class="framework-space"></div>',
        unsafe_allow_html=True
    )

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