import streamlit as st
from NyayaAI import model

st.set_page_config(page_title = "Nyaya AI") 
st.title("Nyaya AI")

st.sidebar.markdown("""<p style="color: #faca2b; font-weight: bold; font-size: 18px;">Disclaimer : Testing and Development Phase Notice</p>""", unsafe_allow_html=True)

st.sidebar.write("This model is currently undergoing testing and development. While we strive for accuracy and reliability, it is important to note that errors may occur during this phase. Users are encouraged to use the information provided by the model with caution and to verify critical information through alternative sources where necessary. Your feedback is invaluable in helping us improve the performance and accuracy of the model. Thank you for your understanding and cooperation during this process.")


#st.sidebar.text_input("Name:",placeholder="Shashank Singh")
#st.sidebar.slider("Age:",0,100,21)
#st.sidebar.text_input("Email:",placeholder="singhshashankthakur596@gmail.com")
#st.sidebar.selectbox("Profession:",["Legal Professionals","Non-legal Professions"],placeholder="Select Your Profession")
#save = st.sidebar.button("Save")
#if save:
    #success_message = st.sidebar.success("Success! Your submission has been saved!")
    #time.sleep(5)
    #success_message.empty()

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
            response = model(prompt)
            st.write("Taking a moment to thank you for your patience. Below are the relevant IPC sections corresponding to your concern :")
            for item in response[:5]:
                law = item.get("law", "")
                description = item.get("description", "")
                punishment = item.get("punishment", "")

                st.markdown(f"""
                    Law: {law}<br>
                    Description: {description}<br>
                    Punishment: {punishment}<br><br>
                """, unsafe_allow_html=True)
            st.write("Feel free to reach out if you need further assistance!")
    st.session_state.messages.append(message)