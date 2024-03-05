from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os, sqlite3 as sq

import google.generativeai as ai

ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question: str, prompt: str) -> str:
    model = ai.GenerativeModel("gemini-pro")
    resp = model.generate_content([prompt, question])
    return resp.text

def read_sql_query(sql: str, db: str) -> None:
    conn = sq.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
    rows = cur.fetchall()
    for i in rows:
        print(i)
    
    return rows

prompt = ["""You are an expert in converting English questions to SQL code!
    The SQL database has name STUDENT and has the following columns - NAME, CLASS, SECTION

    For example, 
    Example 1 - How many entries of records are present?
    The SQL command will be something like this SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class?
    The SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output (i.e output should be plane text without markdown)
    """,
    """You are an expert in generating markdown for SQL data!
    The SQL database has name STUDENT and has the following columns - NAME, CLASS, SECTION

    For example, 
    Example 1 - If you get input like ('Paul', 'Data Science', 'A'), ('Joshua', 'Data Science', 'A')
    The markdown output will be a table like 
    |Name|Class|Section|
    |---|---|---|
    |Paul|Data Science|A|
    |Joshua|Data Science|A|
    """]

st.set_page_config(page_title="Having trouble writing SQL query?")
st.header("Retrieve SQL data without having to write SQL queries, just write it in English!")

question = st.text_input("Input: ", key="input", placeholder="Tell me what to do in English!")
submit = st.button("Ask")

if submit:
    sql_response = get_gemini_response(question, prompt[0])
    response = read_sql_query(sql_response, "student.db")
    print(response)

    md_resp = get_gemini_response(" ".join(str(response)), prompt[1])

    st.subheader("SQL: ")
    st.markdown(f"```sql\n{sql_response}\n```")

    st.subheader("Output: ")
    st.markdown(md_resp)
