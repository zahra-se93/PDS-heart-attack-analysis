def run():
    import streamlit as st

    st.markdown("# Overview Page")
    st.sidebar.header("Overview Sidebar")
    st.write(
        """Write an overview of heart attack here!"""
    )


# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()