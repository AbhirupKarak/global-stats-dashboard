import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Statistics Dashboard", page_icon="🌍", layout="wide")

#Loading the CSV files and cleaning it up
df_br = pd.read_csv("birth_rate.csv", skiprows=3)
df_long_br = df_br.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year', value_name="birth_rate"
)
df_dr = pd.read_csv("death_rate.csv", skiprows=3)
df_long_dr = df_dr.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year', value_name="death_rate"
)
df_long_br = df_long_br[df_long_br["year"] != "Unnamed: 70"]
df_long_br["year"] = df_long_br["year"].astype(int)
df_long_br = df_long_br.dropna(subset=["birth_rate"])
df_long_dr = df_long_dr[df_long_dr["year"] != "Unnamed: 70"]
df_long_dr["year"] = df_long_dr["year"].astype(int)
df_long_dr = df_long_dr.dropna(subset=["death_rate"])
df_p = pd.read_csv("population.csv", skiprows=3)
df_long_p = df_p.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year', value_name="population"
)
df_long_p = df_long_p[df_long_p["year"] != "Unnamed: 70"]
df_long_p["year"] = df_long_p["year"].astype(int)
df_long_p = df_long_p.dropna(subset=["population"])

countries = ["Aruba", "Africa Eastern and Southern", "Afghanistan", "Africa Western and Central", "Angola", "Albania", "Andorra", "Arab World", "United Arab Emirates", "Argentina", "Armenia", "American Samoa", "Antigua and Barbuda", "Australia", "Austria", "Azerbaijan", "Burundi", "Belgium", "Benin", "Burkina Faso", "Bangladesh", "Bulgaria", "Bahrain", "Bahamas, The", "Bosnia and Herzegovina", "Belarus", "Belize", "Bermuda", "Bolivia", "Brazil", "Barbados", "Brunei Darussalam", "Bhutan", "Botswana", "Central African Republic", "Canada", "Central Europe and the Baltics", "Switzerland", "Channel Islands", "Chile", "China", "Cote d'Ivoire", "Cameroon", "Congo, Dem. Rep.", "Congo, Rep.", "Colombia", "Comoros", "Cabo Verde", "Costa Rica", "Caribbean small states", "Cuba", "Curacao", "Cayman Islands", "Cyprus", "Czechia", "Germany", "Djibouti", "Dominica", "Denmark", "Dominican Republic", "Algeria", "East Asia & Pacific (excluding high income)", "Early-demographic dividend", "East Asia & Pacific", "Europe & Central Asia (excluding high income)", "Europe & Central Asia", "Ecuador", "Egypt, Arab Rep.", "Euro area", "Eritrea", "Spain", "Estonia", "Ethiopia", "European Union", "Fragile and conflict affected situations", "Finland", "Fiji", "France", "Faroe Islands", "Micronesia, Fed. Sts.", "Gabon", "United Kingdom", "Georgia", "Ghana", "Gibraltar", "Guinea", "Gambia, The", "Guinea-Bissau", "Equatorial Guinea", "Greece", "Grenada", "Greenland", "Guatemala", "Guam", "Guyana", "High income", "Hong Kong SAR, China", "Honduras", "Heavily indebted poor countries (HIPC)", "Croatia", "Haiti", "Hungary", "IBRD only", "IDA & IBRD total", "IDA total", "IDA blend", "Indonesia", "IDA only", "Isle of Man", "India", "Not classified", "Ireland", "Iran, Islamic Rep.", "Iraq", "Iceland", "Israel", "Italy", "Jamaica", "Jordan", "Japan", "Kazakhstan", "Kenya", "Kyrgyz Republic", "Cambodia", "Kiribati", "St. Kitts and Nevis", "Korea, Rep.", "Kuwait", "Latin America & Caribbean (excluding high income)", "Lao PDR", "Lebanon", "Liberia", "Libya", "St. Lucia", "Latin America & Caribbean", "Least developed countries: UN classification", "Low income", "Liechtenstein", "Sri Lanka", "Lower middle income", "Low & middle income", "Lesotho", "Late-demographic dividend", "Lithuania", "Luxembourg", "Latvia", "Macao SAR, China", "St. Martin (French part)", "Morocco", "Monaco", "Moldova", "Madagascar", "Maldives", "Middle East, North Africa, Afghanistan & Pakistan", "Mexico", "Marshall Islands", "Middle income", "North Macedonia", "Mali", "Malta", "Myanmar", "Middle East, North Africa, Afghanistan & Pakistan (excluding high income)", "Montenegro", "Mongolia","Northern Mariana Islands", "Mozambique", "Mauritania", "Mauritius", "Malawi", "Malaysia", "North America", "Namibia", "New Caledonia", "Niger", "Nigeria", "Nicaragua", "Netherlands", "Norway", "Nepal", "Nauru", "New Zealand", "OECD members", "Oman", "Other small states", "Pakistan", "Panama", "Peru", "Philippines", "Palau", "Papua New Guinea", "Poland", "Pre-demographic dividend", "Puerto Rico (US)", "Korea, Dem. People's Rep.", "Portugal", "Paraguay", "West Bank and Gaza", "Pacific island small states", "Post-demographic dividend", "French Polynesia", "Qatar", "Romania", "Russian Federation", "Rwanda", "South Asia", "Saudi Arabia", "Sudan", "Senegal", "Singapore", "Solomon Islands", "Sierra Leone", "El Salvador", "San Marino", "Somalia, Fed. Rep.", "Serbia", "Sub-Saharan Africa (excluding high income)", "South Sudan", "Sub-Saharan Africa", "Small states", "Sao Tome and Principe", "Suriname", "Slovak Republic", "Slovenia", "Sweden", "Eswatini", "Sint Maarten (Dutch part)", "Seychelles", "Syrian Arab Republic", "Turks and Caicos Islands", "Chad", "East Asia & Pacific (IDA & IBRD countries)", "Europe & Central Asia (IDA & IBRD countries)", "Togo", "Thailand", "Tajikistan", "Turkmenistan", "Latin America & the Caribbean (IDA & IBRD countries)", "Timor-Leste", "Middle East, North Africa, Afghanistan & Pakistan (IDA & IBRD)", "Tonga", "South Asia (IDA & IBRD)", "Sub-Saharan Africa (IDA & IBRD countries)", "Trinidad and Tobago", "Tunisia", "Turkiye", "Tuvalu", "Tanzania", "Uganda", "Ukraine", "Upper middle income", "Uruguay", "United States", "Uzbekistan", "St. Vincent and the Grenadines", "Venezuela, RB", "British Virgin Islands", "Virgin Islands (U.S.)", "Viet Nam", "Vanuatu", "World", "Samoa", "Kosovo", "Yemen, Rep.", "South Africa", "Zambia", "Zimbabwe"]

st.title("Global Statistics Dashboard")
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Rankings", "Compare", "Insights"])

st.sidebar.title("Select filters")
br_dr = st.sidebar.radio("Birth Rate or Death Rate", ["Birth Rate", "Death Rate"])
countries_filtered = st.sidebar.multiselect("Select countries (type World for world stats)", countries)
if len(countries_filtered) > 5:
    st.sidebar.warning("Please select a maximum of 5 countries.")
    st.stop()

with tab1:
    if br_dr == "Birth Rate":
        country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
        fig = px.line(country_df_br, x="year", y="birth_rate", color="Country Name",
                      title="Birth Rate over Time",
                      labels={"birth_rate": "Birth Rate (per 1,000 people per year)", "year": "Year"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
        fig = px.line(country_df_dr, x="year", y="death_rate", color="Country Name",
                      title="Death Rate over Time",
                      labels={"death_rate": "Death Rate (per 1,000 people per year)", "year": "Year"})
        st.plotly_chart(fig, use_container_width=True)

    country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
    country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
    country_df_p = df_long_p[df_long_p["Country Name"].isin(countries_filtered)]
    br_avg = country_df_br["birth_rate"].mean()
    dr_avg = country_df_dr["death_rate"].mean()
    p_avg = country_df_p["population"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Birth Rate", f"{br_avg:.2f}")
    col1.caption("per 1,000 people per year")
    col2.metric("Avg Death Rate", f"{dr_avg:.2f}")
    col2.caption("per 1,000 people per year")
    col3.metric("Avg Population", f"{p_avg:,.0f}")
    col3.caption("average across selected countries & years")

with tab2:
    yr_b = st.sidebar.number_input("Choose the year for Birth Rates", min_value=1960, max_value=2023, step=1)
    top_br = df_long_br[df_long_br["year"] == yr_b].sort_values("birth_rate", ascending=False).head(10)
    fig = px.bar(top_br, x="Country Name", y="birth_rate",
                 title=f"Top 10 Highest Birth Rates in {yr_b}",
                 labels={"birth_rate": "Birth Rate (per 1,000 people per year)", "Country Name": "Country"})
    st.plotly_chart(fig, use_container_width=True)

    yr_d = st.sidebar.number_input("Choose the year for Death Rates", min_value=1960, max_value=2023, step=1)
    top_dr = df_long_dr[df_long_dr["year"] == yr_d].sort_values("death_rate", ascending=False).head(10)
    fig = px.bar(top_dr, x="Country Name", y="death_rate",
                 title=f"Top 10 Highest Death Rates in {yr_d}",
                 labels={"death_rate": "Death Rate (per 1,000 people per year)", "Country Name": "Country"})
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
    country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
    
    combined_rows = []
    for country in countries_filtered:
        for _, row in country_df_br[country_df_br["Country Name"] == country].iterrows():
            combined_rows.append({"year": row["year"], "rate": row["birth_rate"], "type": f"{country} (Birth)"})
        for _, row in country_df_dr[country_df_dr["Country Name"] == country].iterrows():
            combined_rows.append({"year": row["year"], "rate": row["death_rate"], "type": f"{country} (Death)"})
    
    if combined_rows:
        df_compare = pd.DataFrame(combined_rows)
        fig = px.line(df_compare, x="year", y="rate", color="type",
                      title="Birth and Death Rates over Time",
                      labels={"rate": "Rate (per 1,000 people per year)", "year": "Year"})
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    br_1960 = df_long_br[(df_long_br["Country Name"] == "World") & (df_long_br["year"] == 1960)]["birth_rate"].values[0]
    br_2020 = df_long_br[(df_long_br["Country Name"] == "World") & (df_long_br["year"] == 2020)]["birth_rate"].values[0]
    st.info(f"🌍 Global birth rates have nearly halved — from {br_1960:.2f} in 1960 to {br_2020:.2f} in 2020.")
    world_br = df_long_br[df_long_br["Country Name"] == "World"]
    fig = px.line(world_br, x="year", y="birth_rate", title="World Birth Rate over Time",
                  labels={"birth_rate": "Birth Rate (per 1,000 people per year)", "year": "Year"})
    st.plotly_chart(fig, use_container_width=True)

    st.info("🌍 Sub-Saharan Africa has the highest birth rates globally.")
    ssa = df_long_br[df_long_br["Country Name"].isin(["Sub-Saharan Africa", "Sub-Saharan Africa (excluding high income)", "World"])]
    fig = px.line(ssa, x="year", y="birth_rate", color="Country Name", title="Sub-Saharan Africa vs World Birth Rate",
                  labels={"birth_rate": "Birth Rate (per 1,000 people per year)", "year": "Year"})
    st.plotly_chart(fig, use_container_width=True)

    st.info("🇰🇷 Korea has one of the lowest birth rates in the world.")
    korea_br = df_long_br[df_long_br["Country Name"] == "Korea, Rep."]
    fig = px.line(korea_br, x="year", y="birth_rate", title="Korea Birth Rate over Time",
                  labels={"birth_rate": "Birth Rate (per 1,000 people per year)", "year": "Year"})
    st.plotly_chart(fig, use_container_width=True)