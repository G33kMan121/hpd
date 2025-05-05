import streamlit as st

st.title("HPD Cut Calculator")

# Input section
donors = st.number_input("Expected number of donors", min_value=0, step=1)
hpd_goal = st.number_input("Center's HPD goal (e.g., 0.86)", min_value=0.0, step=0.01)
scheduled_hours = st.number_input("Total scheduled hours", min_value=0.0, step=1.0)
employees = st.number_input("Non-exempt employees", min_value=1, step=1)
days_open = st.number_input("Days center is open", min_value=1, step=1)

# Calculate button
if st.button("Calculate"):
    allowed_hours = donors * hpd_goal
    over_hours = scheduled_hours - allowed_hours

    if over_hours <= 0:
        st.success("You're already at or below your HPD goal. No cuts needed!")
    else:
        cut_hours = over_hours / employees
        daily_cut = cut_hours / days_open
        rounded = round(daily_cut * 4) / 4
        st.warning(f"You will need to cut approximately {rounded:.2f} hours from every employee per day to meet goal.")
