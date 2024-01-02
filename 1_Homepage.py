import streamlit as st
import calendar

st.set_page_config(
    page_title="Academic Dashbaord",
    page_icon="📖",
    layout="wide"
)

# HEADER
st.title("Julia's Academic Dashboard")

# COURSES
with st.container():
    courses_column, marks_column, image_column = st.columns((1, 1, 2))
    with courses_column:
        st.header("Courses")
        st.write("[MPM2DZ-3 : Principles of Mathematics](Math.py)")
        st.write("[CHC2DZ-1 : Canadian History](History.py)")
        st.write("[ICS3U1-4 : Computer and Information Science](CompSci.py)")
        st.write("[SNC2DZ-4 : Science](Science.py)")
        st.write("[AMR2O1-2 : Music - Repertoire](Rep.py)")

    with marks_column:
        st.header("Mark")
        st.write("92%")
        st.write("83%")
        st.write("99%")
        st.write("95%")
        st.write("90%")

    with image_column:
        st.write("##")
        st.image("https://i.pinimg.com/564x/fe/f3/c1/fef3c1f6d27730f48b1f65689ec8b847.jpg")

st.write("---")
st.header("To-Do Lists")
# CALENDAR
with st.container():
    math_column, history_column, compsci_column, science_column, rep_column = st.columns(5)
    with math_column:
        st.subheader("Math")
        st.write("**Pages 127-128**")
        st.checkbox("Questions 1-8")
        st.write("**Page 180**")
        st.checkbox("Question 10")

    with history_column:
        st.subheader("History")
        st.write("**Canada on the World Stage**")
        st.checkbox("Write a paragraph on how Canada was present during WWII")

    with compsci_column:
        st.subheader("Comp Sci")
        st.write("**ISU**")
        st.checkbox("Finish academic dashboard")

    with science_column:
        st.subheader("Science")
        st.write("**Write Notes**")
        st.checkbox("3.10")
        st.checkbox("3.11")
        st.checkbox("3.12")
        st.checkbox("3.13")
        st.checkbox("3.14")
        st.checkbox("3.15")
        st.checkbox("3.16")
        st.checkbox("3.17")
        st.checkbox("3.18") 

    with rep_column:
        st.subheader("Repertoire")
        st.write("**Mother of a Revolution**")
        st.checkbox("Practice runs at bar 48")    
        st.write("**Ross Roy**")
        st.checkbox("Practice 16th note runs and scales")