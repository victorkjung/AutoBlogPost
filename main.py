import streamlit as st

def display_sidebar():
    st.sidebar.header("About this App")
    st.sidebar.write("""
        This application generates prompt to summarize a business article into a social media post using OpenAI ChatGPT.
    """)

    st.sidebar.header("Instructions")
    st.sidebar.write("""
        1. Enter the URL in the 'Enter the URL' field.
        2. Select the tone of the blog post from 'Select Tone' field.
        3. Click 'Generate' to create your custom blog post prompt.
    """)

    st.sidebar.markdown(
        """
        [Buy :star-struck: me a :coffee: coffee](https://www.buymeacoffee.com/5gDeDWWMCI)
        """,
        unsafe_allow_html=True,
    )

def main():
    # Set the title of the application
    st.title("Business Editorial :robot_face: Bot")

    # Display the sidebar
    display_sidebar()

    # Define your template paragraph
    template = ("You are an award-winning business reporter for the Wall Street Journal. "
                "Summarize the following article into a **{Tone}** Linkedin 500 word "
                "post of 7 sections - Headline, introduction about the topic, "
                "listicle on key points, an overview of the topic, an analysis of "
                "the topic, supporting argument, and conclusion: **{URL}**")
    st.write("**PROMPT TEMPLATE:** ", template)

    # Create input boxes for the user to fill in their data
    url = st.text_input("Enter the URL", "")
    tone = st.multiselect("Select Tone", ["Witty", "Professional", "Engaging", "Casual"])

    # Create a button to generate the new result
    if st.button("Generate"):
        if not url:
            st.error("Please provide a **URL** before clicking 'Generate'.")
        elif not tone:
            st.error("Please select at least one tone before clicking 'Generate'.")
        else:
            for selected_tone in tone:
                result = template.format(Tone=selected_tone, URL=url)
                st.markdown(f'<div style="background-color: #f5f5f5; padding: 10px; border: 1px solid black; border-radius: 5px;">{result}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
