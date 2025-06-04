import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

#Session state
# We use session_state to persist values between reruns (like keeping count)
if "count" not in st.session_state:
    st.session_state.count=0

#sidebar navigation
# Create a dropdown menu in the sidebar to switch between app pages
page=st.sidebar.selectbox("Select Page",["Home","Form","Upload & Data","Chart","Counter"])

#Home page
if page=="Home":
    st.title("Streamlit Demo (title)")
    st.header("welcome (header)")
    st.markdown("Shows various streamlit components (markdown)")
    
    #layout using columns
    col1,col2=st.columns(2)     #split screen into 2 cols
    with col1:
        st.text("Layout: column 1")
        st.text("Text input widget:")
        st.text_input("Your name") #text input widget
        st.text("slider input widget:")
        st.slider("Your age",0,100) #slider input from 0 to 100
    with col2:
        st.text("Layout: column 2")
        st.text("Radio button group")
        st.radio("Gender",["Male","Female","Other"]) #radio button group
        st.text("checkbox input")
        st.checkbox("I agree")
     
    # Expandable section for extra info   
    st.text("expandable section")
    with st.expander("More info"):
        st.write("This expander hides text until clicked")
        
    st.balloons()

#form page
elif page=="Form":
    st.header("Input Form (header)")
    
    # Forms let you group multiple inputs together and submit once
    with st.form("info_form"):
        name = st.text_input("Enter your name")         # Input name
        bday = st.date_input("Birthday", value=date(2000, 1, 1))  # Select date
        submitted = st.form_submit_button("Submit")     # Submit button
    if submitted:
        st.write(f"Hello, {name}! Your birthday is {bday}.")

#upload page
elif page=="Upload & Data":
    st.header("Upload a csv file (header)")
    
    #file upload widget
    uploaded_file=st.file_uploader("Choose a file",type=["csv"])
    if uploaded_file:
        #read file as dataframe using pandas
        df=pd.read_csv(uploaded_file)
        st.dataframe(df)   #display df

#chart page
elif page=="Chart":
    st.header("Simple chart with plotly")
    
    # Create a sample dataframe manually
    df = pd.DataFrame({
        "Fruits": ["Apples", "Bananas", "Cherries"],
        "Quantity": [10, 30, 20]
    })

    # Use plotly to generate a bar chart from the dataframe
    fig = px.bar(df, x="Fruits", y="Quantity")

    st.plotly_chart(fig)

#counter page:session state
elif page=="Counter":
    st.header("Session state")
    # Show current count stored in session_state
    st.write("Current count:", st.session_state.count)
    
    # Increment button increases count by 1
    if st.button("Increment"):
        st.session_state.count += 1
    
    # Reset button sets count to 0
    if st.button("Reset"):
        st.session_state.count = 0
        
    st.snow()