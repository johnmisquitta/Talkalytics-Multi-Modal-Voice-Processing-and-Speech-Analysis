import streamlit as st

# Streamlit app title
st.title("Speech Recognition Demo")

# Streamlit app styles
st.markdown(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
            min-width: 100%;
            min-height: 100vh;
            font-family: sans-serif;
            text-align: center;
            color: #fff;
            background: #000;
        }

        button {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 5em;
            height: 2em;
            margin-left: -2.5em;
            margin-top: -1em;
            z-index: 100;
            padding: .25em .5em;
            color: #fff;
            background: #000;
            border: 1px solid #fff;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1.15em;
            font-weight: 200;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
            transition: box-shadow .5s;
        }

        button:hover {
            box-shadow: 0 0 30px 5px rgba(255, 255, 255, 0.75);
        }

        main {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        main>div {
            display: inline-block;
            width: 3px;
            height: 100px;
            margin: 0 7px;
            background: currentColor;
            transform: scaleY(.5);
            opacity: .25;
        }

        main.error {
            color: #f7451d;
            min-width: 20em;
            max-width: 30em;
            margin: 0 auto;
            white-space: pre-line;
        }

        #transcript {
            position: fixed;
            top: 60%;
            width: 100vw;
            padding-left: 20vw;
            padding-right: 20vw;
            font-size: x-large;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app content
st.markdown("<main></main>", unsafe_allow_html=True)
st.button("start", on_click=lambda: st.markdown("<div id='transcript'></div>", unsafe_allow_html=True))
