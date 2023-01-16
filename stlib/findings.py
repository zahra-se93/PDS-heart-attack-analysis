def run():
    import streamlit as st

    st.markdown("# Findings")
    st.sidebar.header("Findings Sidebar")
    st.write(
    """Write about the findings we found for Heart Attack Analysis"""
    )


# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()