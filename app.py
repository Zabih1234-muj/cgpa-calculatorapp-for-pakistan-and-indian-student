import streamlit as st

# ------------------- PAGE SETTINGS -------------------
st.set_page_config(page_title="CGPA Calculator (India & Pakistan)", page_icon="🎓", layout="centered")

# ------------------- TITLE -------------------
st.title("🎓 CGPA Calculator for India 🇮🇳 & Pakistan 🇵🇰")

st.markdown("""
This app helps you calculate your **CGPA** based on your country's grading system.  
Select your country, enter subjects, grades, and credit hours, and see your CGPA instantly.
""")

# ------------------- COUNTRY SELECTION -------------------
country = st.selectbox("🌍 Select your country:", ["India", "Pakistan"])

# ------------------- GRADE TO POINT CONVERSION -------------------
def grade_to_point(grade, country):
    if country == "India":
        # Common Indian university grade scale (O/A+/A/B+/B/C/F)
        grade_scale = {
            "O": 10,
            "A+": 9,
            "A": 8,
            "B+": 7,
            "B": 6,
            "C": 5,
            "F": 0
        }
    else:
        # Pakistani university scale (A/A-/B+/B/C+/C/D/F)
        grade_scale = {
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "C+": 2.7,
            "C": 2.3,
            "D": 2.0,
            "F": 0.0
        }
    return grade_scale.get(grade.upper(), 0)

# ------------------- USER INPUTS -------------------
num_subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=20, step=1)

grades = []
credits = []

st.write("---")
st.subheader("📘 Enter Subject Details")

# Input loop for subjects
for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)

    with col1:
        if country == "India":
            grade = st.selectbox(
                f"Grade for Subject {i+1}",
                ["O", "A+", "A", "B+", "B", "C", "F"],
                key=f"grade_{i}"
            )
        else:
            grade = st.selectbox(
                f"Grade for Subject {i+1}",
                ["A", "A-", "B+", "B", "C+", "C", "D", "F"],
                key=f"grade_{i}"
            )

    with col2:
        credit = st.number_input(
            f"Credit Hour for Subject {i+1}",
            min_value=1.0,
            max_value=10.0,
            step=0.5,
            key=f"credit_{i}"
        )

    grades.append(grade)
    credits.append(credit)

# ------------------- CGPA CALCULATION -------------------
if st.button("Calculate CGPA"):
    total_points = sum(grade_to_point(g, country) * c for g, c in zip(grades, credits))
    total_credits = sum(credits)

    if total_credits == 0:
        st.error("⚠️ Total credit hours cannot be zero.")
    else:
        cgpa = total_points / total_credits

        # Adjust scale display based on country
        if country == "India":
            st.success(f"🇮🇳 Your CGPA is: **{cgpa:.2f} / 10**")
        else:
            st.success(f"🇵🇰 Your CGPA is: **{cgpa:.2f} / 4.0**")

        st.info(f"📗 Total Credit Hours: **{total_credits:.1f}**")

st.write("---")
st.caption("Made with ❤️ using Streamlit | Supports India 🇮🇳 & Pakistan 🇵🇰")
