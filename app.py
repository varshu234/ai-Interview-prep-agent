import os
import time
import streamlit as st
from langchain_groq import ChatGroq

# ---------------- SETUP ---------------- #

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=200
)

st.set_page_config(page_title="Interview Prep AI", page_icon="🎯")
st.title("🎯 Interview Preparation Agent")

# ---------------- INPUT ---------------- #

role = st.text_input("Enter Job Role")
company = st.text_input("Enter Company Name")

# ---------------- SESSION STATE ---------------- #

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# ---------------- GENERATE QUESTIONS ---------------- #

if st.button("Start Preparation"):

    if role.strip() == "" or company.strip() == "":
        st.warning("Please enter both role and company")
    else:
        with st.spinner("Generating interview questions..."):

            try:
                prompt = f"""
                Generate exactly 3 interview questions for a {role} role at {company}.

                Rules:
                - Only return questions
                - No introduction text
                - No explanations
                - Each question on a new line
                """

                response = llm.invoke(prompt)

                raw_questions = response.content.split("\n")

                # ✅ Clean questions (remove numbers, empty lines)
                questions = []
                for q in raw_questions:
                    q = q.strip()
                    if q:
                        q = q.replace("1.", "").replace("2.", "").replace("3.", "").strip()
                        questions.append(q)

                st.session_state.questions = questions
                st.session_state.current_q = 0

            except Exception as e:
                st.error("⚠️ Server busy. Trying again...")
                time.sleep(2)

                response = llm.invoke(prompt)
                raw_questions = response.content.split("\n")

                questions = []
                for q in raw_questions:
                    q = q.strip()
                    if q:
                        q = q.replace("1.", "").replace("2.", "").replace("3.", "").strip()
                        questions.append(q)

                st.session_state.questions = questions
                st.session_state.current_q = 0

# ---------------- DISPLAY QUESTIONS ---------------- #

if len(st.session_state.questions) > 0:

    st.subheader("🧪 Mock Interview")

    current_index = st.session_state.current_q

    if current_index < len(st.session_state.questions):

        question = st.session_state.questions[current_index]

        # ✅ SHOW QUESTION
        st.write(f"### Question {current_index + 1}")
        st.info(question)

        # Answer input
        answer = st.text_area("Your Answer", key=f"answer_{current_index}")

        if st.button("Submit Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer before submitting")
            else:
                with st.spinner("Evaluating your answer..."):

                    eval_prompt = f"""
                    Evaluate this interview answer.

                    Question: {question}
                    Answer: {answer}

                    Give:
                    - Score out of 10
                    - 2 improvement tips
                    """

                    feedback = llm.invoke(eval_prompt)

                    st.success("✅ Evaluation Result:")
                    st.write(feedback.content)

                    # Move to next question
                    st.session_state.current_q += 1

    else:
        st.success("🎉 Interview Completed!")