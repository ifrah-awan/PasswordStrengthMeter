import streamlit as st
import re
import random
import string
# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
        feedback.append("✅ Length is good (8+ characters).")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains uppercase & lowercase letters.")
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains at least one digit (0-9).")
    else:
        feedback.append("❌ Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
        feedback.append("✅ Contains at least one special character (!@#$%^&*).")
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Password Strength Rating
    if score == 4:
        strength = "🟢 Super Strong!"
    elif score == 3:
        strength = "🟡 Moderate Strength."
    elif score == 2:
        strength = "🟠 Weak Password!"
    else:
        strength = "🔴 Very Weak! Change it ASAP!"

    return strength, feedback


# Streamlit UI
st.title("🔐 Password Strength Meter")

# Taking input from the user
password = st.text_input("Enter your password:", type="password")

# Analyzing password when input is given
if password:
    strength, feedback = check_password_strength(password)

    st.subheader("📊 Password Analysis:")
    st.write(f"*🔒 Strength Level:* {strength}")

    if feedback:
        st.subheader("💡 Suggestions to Improve Generated Password:")
        for tip in feedback:
            st.write(f"- {tip}")
    #initalizing session state for generated password if not set
    if "generated_password"not in st.session_state:
        st.session_state["generated_password"]=None

#function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(length))

#ceating a button to generate a password
if st.button("Generate strong password"):
    st.session_state["password"] = generate_password()

#display the generated password
st.text_input("Generated password:",
    value=st.session_state.get("password", ""),
    key="password_display")
    
