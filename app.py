import streamlit as st
from env.environment import StudentEnv
from env.models import Action

st.title("📚 Student Study Buddy")

env = StudentEnv()
obs = env.reset()

st.write("Initial State:", obs)

if st.button("Do Math"):
    action = Action(action_type="study", task="Math")
    obs, reward, done, info = env.step(action)
    st.write("After Action:", obs)
    st.write("Reward:", reward)

if st.button("Rest"):
    action = Action(action_type="rest")
    obs, reward, done, info = env.step(action)
    st.write("After Rest:", obs)
