import streamlit as st

#from modules.RetrievalAugmentedGenerator import RAG


with st.sidebar:
    "## SDSC4001 Group Project"
    "Members: "
    "SEIVABEL-JESSICA-HALIM"
    "NATASSA-CATALINA-BUNTARA"
    "PATRICIA-VIANNEY"
    "Ivana JESSLYN"
    "Beatrice ABDINEGARA"

    user_id = st.text_input("User ID", value="4614")

st.title("📚💬 BookWise Chat")
st.caption("🚀Delayed Rewards Recommender System Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi there! What kind of book would you like me to recommend today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    def output(prompt):
        #print("hello", prompt)
        
        {
    "output": "Certainly! Here are some romance book recommendations:1. Pride and Prejudice by Jane Austen - A timeless classic exploring the complexities of love and societal expectations 2. Outlander by Diana Gabaldon - A gripping tale of love, time travel, and adventure set in 18th-century Scotland. 3. To All the Boys I've Loved Before by Jenny Han - A sweet and funny story about love letters and unexpected romance. 4. The Fault in Our Stars by John Green - A poignant tale of love and loss, beautifully written for young adult readers."}


    response = output(prompt)
    print("RESPONSE ===>", response)
    print("KEYS ===>", response.keys())
    
    msg = {"role": "assistant", "content": response["output"]}

    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])
