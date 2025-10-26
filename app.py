
import streamlit as st
import pandas as pd

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="ENERGY PREDICTOR", layout="centered")
st.title("⚡ ENERGY PREDICTOR ⚡")

# ------------------ CUSTOM CSS ------------------
st.markdown(
"""
<style>
/* Dark multicolor gradient background */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Headings and labels white, bold, uppercase, large */
.stText, .stMarkdown, .stNumberInput label, .stSelectbox label, .stSlider label {
    color: white !important;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 18px;
}

/* Input boxes text white and smaller width */
input[type="number"], .stSlider>div>div>div>input, .stSelectbox>div>div>div>div>input {
    color: white !important;
    background-color: #333333 !important;
    width: 80px !important;
    border-radius: 5px;
    padding: 5px;
}

/* Buttons styling */
.stButton>button {
    font-weight: bold;
    text-transform: uppercase;
    font-size: 18px;
}

/* Subheaders white */
.stSubheader {
    color: white;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True
)

# ------------------ USER INPUTS ------------------
st.header("INPUT APPLIANCE USAGE & TEMPERATURE")

# Temperature and day
col_temp, col_day = st.columns([2,1])
with col_temp:
    temp = st.number_input("TEMPERATURE (°C)", value=30.0)
with col_day:
    day = st.selectbox("DAY", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

# Appliance inputs: count and hours side by side
st.subheader("APPLIANCES USAGE")
appliances = ["AC", "FRIDGE", "TV", "LIGHT", "FAN"]
default_counts = [1, 1, 1, 5, 2]
default_hours = [4.0, 20.0, 3.0, 5.0, 6.0]
min_counts = [0,0,0,0,0]
max_counts = [5,5,5,20,10]
min_hours = [0.0]*5
max_hours = [24.0]*5

counts = []
hours = []

for i, app in enumerate(appliances):
    col_count, col_hour = st.columns([1,1])
    with col_count:
        count = st.number_input(f"{app} COUNT", min_value=min_counts[i], max_value=max_counts[i], value=default_counts[i])
        counts.append(count)
    with col_hour:
        hour = st.number_input(f"{app} HOURS", min_value=min_hours[i], max_value=max_hours[i], value=default_hours[i])
        hours.append(hour)

# Assign to variables
ac_count, fridge_count, tv_count, light_count, fan_count = counts
ac_hours, fridge_hours, tv_hours, light_hours, fan_hours = hours

# ------------------ REDUCTION SLIDERS ------------------
st.header("💡 REDUCE USAGE (HOURS) TO SEE POTENTIAL SAVINGS")
reduce_ac = st.slider("REDUCE AC HOURS BY", 0.0, ac_hours, 0.0, step=0.5)
reduce_fridge = st.slider("REDUCE FRIDGE HOURS BY", 0.0, fridge_hours, 0.0, step=0.5)
reduce_tv = st.slider("REDUCE TV HOURS BY", 0.0, tv_hours, 0.0, step=0.5)
reduce_light = st.slider("REDUCE LIGHT HOURS BY", 0.0, light_hours, 0.0, step=0.5)
reduce_fan = st.slider("REDUCE FAN HOURS BY", 0.0, fan_hours, 0.0, step=0.5)

# ------------------ HELPER FUNCTION ------------------
def get_energy_level(kwh):
    if kwh < 5:
        return "LOW ⚡", "green"
    elif kwh <= 19:
        return "MODERATE ⚡", "orange"
    else:
        return "HIGH ⚡", "red"

# ------------------ PREDICTION ------------------
if st.button("PREDICT CONSUMPTION"):
    # ------------------ MANUAL DAILY CONSUMPTION BASED ON COUNT AND HOURS ------------------
    P_ac, P_fridge, P_tv, P_light, P_fan = 1.4, 0.15, 0.1, 0.06, 0.05
    pred = (
        ac_hours * P_ac * ac_count +
        fridge_hours * P_fridge * fridge_count +
        tv_hours * P_tv * tv_count +
        light_hours * P_light * light_count +
        fan_hours * P_fan * fan_count
    )

    st.success(f"PREDICTED DAILY CONSUMPTION: **{pred:.2f} kWh**")

    # Energy level before reductions
    level, color = get_energy_level(pred)
    st.markdown(f"**ENERGY CONSUMPTION LEVEL:** <span style='color:{color}; font-weight:bold'>{level}</span>", unsafe_allow_html=True)

    # ------------------ APPLIANCE CONTRIBUTION ------------------
    ac_kwh = ac_hours * P_ac * ac_count
    fridge_kwh = fridge_hours * P_fridge * fridge_count
    tv_kwh = tv_hours * P_tv * tv_count
    light_kwh = light_hours * P_light * light_count
    fan_kwh = fan_hours * P_fan * fan_count

    st.subheader("APPLIANCE CONTRIBUTION (kWh)")
    st.write(f"AC: {ac_kwh:.2f} kWh")
    st.write(f"FRIDGE: {fridge_kwh:.2f} kWh")
    st.write(f"TV: {tv_kwh:.2f} kWh")
    st.write(f"LIGHT: {light_kwh:.2f} kWh")
    st.write(f"FAN: {fan_kwh:.2f} kWh")

    # ------------------ POTENTIAL SAVINGS ------------------
    st.subheader("💰 POTENTIAL ENERGY SAVINGS & UPDATED LEVEL")
    total_reduction = 0
    savings_info = []

    if reduce_ac > 0:
        saved = reduce_ac * P_ac * ac_count
        savings_info.append(f"Reducing AC by {reduce_ac:.1f} h → saves {saved:.2f} kWh")
        total_reduction += saved
    if reduce_fridge > 0:
        saved = reduce_fridge * P_fridge * fridge_count
        savings_info.append(f"Reducing FRIDGE by {reduce_fridge:.1f} h → saves {saved:.2f} kWh")
        total_reduction += saved
    if reduce_tv > 0:
        saved = reduce_tv * P_tv * tv_count
        savings_info.append(f"Reducing TV by {reduce_tv:.1f} h → saves {saved:.2f} kWh")
        total_reduction += saved
    if reduce_light > 0:
        saved = reduce_light * P_light * light_count
        savings_info.append(f"Reducing LIGHT by {reduce_light:.1f} h → saves {saved:.2f} kWh")
        total_reduction += saved
    if reduce_fan > 0:
        saved = reduce_fan * P_fan * fan_count
        savings_info.append(f"Reducing FAN by {reduce_fan:.1f} h → saves {saved:.2f} kWh")
        total_reduction += saved

    for info in savings_info:
        st.info(info)

    # New total
    new_total = max(pred - total_reduction, 0)
    st.success(f"TOTAL CONSUMPTION AFTER REDUCTIONS: **{new_total:.2f} kWh**")

    # Updated energy level
    new_level, new_color = get_energy_level(new_total)
    st.markdown(f"**UPDATED ENERGY LEVEL:** <span style='color:{new_color}; font-weight:bold'>{new_level}</span>", unsafe_allow_html=True)
