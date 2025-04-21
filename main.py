import streamlit as st
import string

# ------------------------------
# Helper Function to Analyze Password
# ------------------------------
def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    length_ok = len(password) >= 8
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in "!@#$%^&*" for c in password)

    # Add score
    score += length_ok
    score += upper_ok
    score += lower_ok
    score += digit_ok
    score += special_ok

    # Feedback
    if not length_ok:
        feedback.append("➤ Use at least 8 characters.")
    if not upper_ok:
        feedback.append("➤ Add uppercase letters.")
    if not lower_ok:
        feedback.append("➤ Add lowercase letters.")
    if not digit_ok:
        feedback.append("➤ Include numbers (0-9).")
    if not special_ok:
        feedback.append("➤ Use special characters (!@#$%^&*).")

    return score, feedback

# ------------------------------
# UI with Streamlit
# ------------------------------
def main():
    st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
    st.title("🔐 Password Strength Meter")
    st.write("Check how secure your password is and get suggestions to make it stronger.")

    password = st.text_input("Enter your password", type="password")

    if password:
        score, feedback = check_password_strength(password)

        # Determine strength label
        if score <= 2:
            st.error("🟥 Weak Password (Score: {}/5)".format(score))
        elif 3 <= score < 5:
            st.warning("🟨 Moderate Password (Score: {}/5)".format(score))
        else:
            st.success("🟩 Strong Password! (Score: 5/5) 🎉")

        # Show suggestions
        if score < 5:
            st.subheader("Suggestions to Improve:")
            for tip in feedback:
                st.write(tip)

if __name__ == "__main__":
    main()
