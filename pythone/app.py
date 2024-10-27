import streamlit as st
from run import find_best_match

st.set_page_config(page_title = "Nyaya AI") 
st.title("Nyaya AI")


# Store generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hello there! How can I help you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
    
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
            response = find_best_match(prompt)
            st.write("Taking a moment to thank you for your patience. Below are the relevant IPC sections corresponding to your concern :")
            for item in response[:5]:
                law = item.get("law", "")
                description = item.get("description", "")
                punishment = item.get("punishment", "")

                st.markdown(f"""
                    Law: {response['laws']}<br>
                    Description: {response['description']}<br>
                    Punishment: {response['Punishment']}<br><br>
                """, unsafe_allow_html=True)
            st.write("Feel free to reach out if you need further assistance!")
    st.session_state.messages.append(message)