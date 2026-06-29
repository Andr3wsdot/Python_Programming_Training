import streamlit as st

st.title("Password Analyser")

password = st.text_input("Enter the Password", type="password")

# st.button("Validate")
if st.button("Validate"):
    upper = lower = digit = special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True
    if len(password) >= 8 and upper and lower and digit and special:
        st.success("Strong Password ...Thank You")
    else:
        st.error("Invalid Password ")


        if len(password)<8 :
            st.write("Password Must have 8 or more characters")
        if not upper :
            st.write("Must contain Upper Case")
        if not lower:
            st.write("Must contain Lower Case")
        if not digit  :
            st.write("Must contain Digits")
        if not special :
            st.write("Must contain Special Characters")