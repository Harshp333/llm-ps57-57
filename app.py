"""PS57 - Mental Wellness Journal Companion
Run: pip install streamlit groq pandas python-dotenv
     streamlit run app.py
Put GROQ_API_KEY=your_key in a .env file (never upload .env).
"""
import os
import json
import datetime
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"
FILE = "journal_entries.csv"

SYSTEM_PROMPT = """You are a warm, supportive journaling companion for students.
Rules:
- Reflect the person's feelings in 2-4 sentences, then offer one gentle reflection question.
- Do NOT diagnose, give medical advice, or claim to be a therapist.
- Never encourage self-harm. If the entry mentions self-harm or hopelessness, respond with care
  and encourage reaching out to a trusted person or a helpline.
Return ONLY JSON: {"reply": "...", "mood": "happy|neutral|stressed|sad|anxious|distressed",
"distress": true/false}  (distress = true if the entry hints at self-harm, suicide or severe crisis)"""

# Backup keyword check so helplines still appear if the LLM misses it
DISTRESS_WORDS = ["suicide", "kill myself", "end my life", "want to die",
                  "self harm", "hurt myself", "no reason to live", "can't go on"]


def analyse(entry: str) -> dict:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": entry}],
        temperature=0.6,
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    if any(w in entry.lower() for w in DISTRESS_WORDS):
        data["distress"] = True
    return data


def save(entry, mood, reply):
    row = pd.DataFrame([{"date": datetime.date.today().isoformat(),
                         "entry": entry, "mood": mood, "reply": reply}])
    row.to_csv(FILE, mode="a", header=not os.path.exists(FILE), index=False)


st.set_page_config(page_title="Wellness Journal", page_icon="🌱")
st.title("🌱 Mental Wellness Journal Companion")
st.info("This is an AI journaling tool, not medical advice or therapy. "
        "If you need help, please talk to a trusted person or a professional.")

entry = st.text_area("How was your day? Write whatever you feel.", height=180)

if st.button("Reflect with me") and entry.strip():
    with st.spinner("Reading your entry..."):
        try:
            result = analyse(entry)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()
    if result.get("distress"):
        st.error("💙 You're not alone. Free, confidential support in India:\n\n"
                 "- **Tele-MANAS: 14416** (24x7, many languages)\n"
                 "- **Emergency: 112**\n\n"
                 "Please consider reaching out to someone you trust right now.")
    st.success(result["reply"])
    st.caption(f"Detected mood: {result['mood']}")
    save(entry, result["mood"], result["reply"])

if os.path.exists(FILE):
    st.subheader("Your past entries")
    df = pd.read_csv(FILE)
    st.dataframe(df[["date", "mood", "entry"]], use_container_width=True)
    st.bar_chart(df["mood"].value_counts())
