import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
plt.rcParams["font.family"] = "STIXGeneral"
plt.rcParams["text.antialiased"] = True
plt.rcParams["figure.dpi"] = 200

st.set_page_config(page_title="Global Statistics Dashboard", page_icon="🌍", layout="wide")

#Loading the CSV files and cleaing it up
df_br = pd.read_csv("birth_rate.csv", skiprows=3)

df_long_br = df_br.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year',
    value_name="birth_rate"
)
df_dr = pd.read_csv("death_rate.csv", skiprows=3)

df_long_dr = df_dr.melt(
    id_vars = ['Country Name', 'Country Code', 'Indicator Name', "Indicator Code"],
    var_name = 'year',
    value_name="death_rate"
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
    var_name = 'year',
    value_name="population" 
)

df_long_p = df_long_p[df_long_p["year"] != "Unnamed: 70"]
df_long_p["year"] = df_long_p["year"].astype(int)
df_long_p = df_long_p.dropna(subset=["population"])

countries = ["Aruba", "Africa Eastern and Southern", "Afghanistan", "Africa Western and Central", "Angola", "Albania", "Andorra", "Arab World", "United Arab Emirates", "Argentina", "Armenia", "American Samoa", "Antigua and Barbuda", "Australia", "Austria", "Azerbaijan", "Burundi", "Belgium", "Benin", "Burkina Faso", "Bangladesh", "Bulgaria", "Bahrain", "Bahamas, The", "Bosnia and Herzegovina", "Belarus", "Belize", "Bermuda", "Bolivia", "Brazil", "Barbados", "Brunei Darussalam", "Bhutan", "Botswana", "Central African Republic", "Canada", "Central Europe and the Baltics", "Switzerland", "Channel Islands", "Chile", "China", "Cote d'Ivoire", "Cameroon", "Congo, Dem. Rep.", "Congo, Rep.", "Colombia", "Comoros", "Cabo Verde", "Costa Rica", "Caribbean small states", "Cuba", "Curacao", "Cayman Islands", "Cyprus", "Czechia", "Germany", "Djibouti", "Dominica", "Denmark", "Dominican Republic", "Algeria", "East Asia & Pacific (excluding high income)", "Early-demographic dividend", "East Asia & Pacific", "Europe & Central Asia (excluding high income)", "Europe & Central Asia", "Ecuador", "Egypt, Arab Rep.", "Euro area", "Eritrea", "Spain", "Estonia", "Ethiopia", "European Union", "Fragile and conflict affected situations", "Finland", "Fiji", "France", "Faroe Islands", "Micronesia, Fed. Sts.", "Gabon", "United Kingdom", "Georgia", "Ghana", "Gibraltar", "Guinea", "Gambia, The", "Guinea-Bissau", "Equatorial Guinea", "Greece", "Grenada", "Greenland", "Guatemala", "Guam", "Guyana", "High income", "Hong Kong SAR, China", "Honduras", "Heavily indebted poor countries (HIPC)", "Croatia", "Haiti", "Hungary", "IBRD only", "IDA & IBRD total", "IDA total", "IDA blend", "Indonesia", "IDA only", "Isle of Man", "India", "Not classified", "Ireland", "Iran, Islamic Rep.", "Iraq", "Iceland", "Israel", "Italy", "Jamaica", "Jordan", "Japan", "Kazakhstan", "Kenya", "Kyrgyz Republic", "Cambodia", "Kiribati", "St. Kitts and Nevis", "Korea, Rep.", "Kuwait", "Latin America & Caribbean (excluding high income)", "Lao PDR", "Lebanon", "Liberia", "Libya", "St. Lucia", "Latin America & Caribbean", "Least developed countries: UN classification", "Low income", "Liechtenstein", "Sri Lanka", "Lower middle income", "Low & middle income", "Lesotho", "Late-demographic dividend", "Lithuania", "Luxembourg", "Latvia", "Macao SAR, China", "St. Martin (French part)", "Morocco", "Monaco", "Moldova", "Madagascar", "Maldives", "Middle East, North Africa, Afghanistan & Pakistan", "Mexico", "Marshall Islands", "Middle income", "North Macedonia", "Mali", "Malta", "Myanmar", "Middle East, North Africa, Afghanistan & Pakistan (excluding high income)", "Montenegro", "Mongolia","Northern Mariana Islands", "Mozambique", "Mauritania", "Mauritius", "Malawi", "Malaysia", "North America", "Namibia", "New Caledonia", "Niger", "Nigeria", "Nicaragua", "Netherlands", "Norway", "Nepal", "Nauru", "New Zealand", "OECD members", "Oman", "Other small states", "Pakistan", "Panama", "Peru", "Philippines", "Palau", "Papua New Guinea", "Poland", "Pre-demographic dividend", "Puerto Rico (US)", "Korea, Dem. People's Rep.", "Portugal", "Paraguay", "West Bank and Gaza", "Pacific island small states", "Post-demographic dividend", "French Polynesia", "Qatar", "Romania", "Russian Federation", "Rwanda", "South Asia", "Saudi Arabia", "Sudan", "Senegal", "Singapore", "Solomon Islands", "Sierra Leone", "El Salvador", "San Marino", "Somalia, Fed. Rep.", "Serbia", "Sub-Saharan Africa (excluding high income)", "South Sudan", "Sub-Saharan Africa", "Small states", "Sao Tome and Principe", "Suriname", "Slovak Republic", "Slovenia", "Sweden", "Eswatini", "Sint Maarten (Dutch part)", "Seychelles", "Syrian Arab Republic", "Turks and Caicos Islands", "Chad", "East Asia & Pacific (IDA & IBRD countries)", "Europe & Central Asia (IDA & IBRD countries)", "Togo", "Thailand", "Tajikistan", "Turkmenistan", "Latin America & the Caribbean (IDA & IBRD countries)", "Timor-Leste", "Middle East, North Africa, Afghanistan & Pakistan (IDA & IBRD)", "Tonga", "South Asia (IDA & IBRD)", "Sub-Saharan Africa (IDA & IBRD countries)", "Trinidad and Tobago", "Tunisia", "Turkiye", "Tuvalu", "Tanzania", "Uganda", "Ukraine", "Upper middle income", "Uruguay", "United States", "Uzbekistan", "St. Vincent and the Grenadines", "Venezuela, RB", "British Virgin Islands", "Virgin Islands (U.S.)", "Viet Nam", "Vanuatu", "World", "Samoa", "Kosovo", "Yemen, Rep.", "South Africa", "Zambia", "Zimbabwe"]

#Streamlit Code
st.title("Global Statistics Dashboard")
#Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Rankings", "Compare", "Insights"])
with tab1:
    st.sidebar.title("Select filters")
    br_dr = st.sidebar.radio("Birth Rate or Death Rate", ["Birth Rate", "Death Rate"])
    countries_filtered = st.sidebar.multiselect("Select the countries (type World for world stats)", countries)
    if len(countries_filtered) > 5:
        st.sidebar.warning("Please select a maximum of 5 countries.")
        st.stop()

    if br_dr == "Birth Rate":
        country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(data=country_df_br, x="year", y="birth_rate", hue="Country Name", ax=ax)
        ax.set_title("Birth Rate over Time", fontsize=12)
        ax.set_xlabel("Year")
        ax.set_ylabel("Birth Rate (per 1,000 people per year)")
        st.pyplot(fig, use_container_width=True)
        plt.clf()
    else:
        if filter:
            year = st.sidebar.number_input("Filter by year", min_value=1960, max_value=2025, step=1)
            result = df_long_dr[(df_long_dr["Country Name"].isin(countries_filtered)) & (df_long_dr["year"] == year)]
            if year:
                st.write(f"The death rate for {countries_filtered} in the year {year} is {result['death_rate'].values[0]}")

        country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(data=country_df_dr, x="year", y="death_rate", hue="Country Name", ax=ax)
        ax.set_title("Death Rate over Time", fontsize=12)
        ax.set_xlabel("Year")
        ax.set_ylabel("Death Rate (per 1,000 people per year)")
        st.pyplot(fig, use_container_width=True)
        plt.clf()

    country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
    country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
    country_df_p = df_long_p[df_long_p["Country Name"].isin(countries_filtered)]
    br_avg = country_df_br["birth_rate"].mean()
    dr_avg = country_df_dr["death_rate"].mean()
    p_avg = country_df_p["population"].mean()

    #Metric Stats

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Birth Rate", f"{br_avg:.2f}")
    col1.caption("per 1,000 people per year")
    col2.metric("Avg Death Rate", f"{dr_avg:.2f}")
    col2.caption("per 1,000 people per year")
    col3.metric("Avg Population", f"{p_avg:,.0f}")
    col3.caption("average across selected countries & years")

#Top 10 Highest Birth / Death Rate Countries for a specific year with a bar graph

with tab2:
    yr_b = st.sidebar.number_input("Choose the year for Birth Rates", min_value=1960, max_value= 2023, step=1)
    sns.barplot(data=df_long_br[df_long_br["year"] == yr_b].sort_values("birth_rate", ascending=False).head(10), x="Country Name", y="birth_rate")
    plt.title(f"Top 10 Highest Birth Rates in {yr_b}")
    plt.ylabel("Birth Rate (per 1,000 people per year)")
    plt.xlabel("Country")
    plt.xticks(rotation=45, ha='right', fontsize=8)
    #plt.figure(figsize=(12, 5))
    st.pyplot(plt)
    plt.clf()

    yr_d = st.sidebar.number_input("Choose the year for Death Rates", min_value=1960, max_value= 2023, step=1)

    sns.barplot(data=df_long_dr[df_long_dr["year"] == yr_d].sort_values("death_rate", ascending=False).head(10), x="Country Name", y="death_rate")
    plt.title(f"Top 10 Highest Death Rates in {yr_d}")
    plt.ylabel("Death Rate (per 1,000 people per year)")
    plt.xlabel("Country")
    plt.xticks(rotation=45, ha='right', fontsize=8)
    #plt.figure(figsize=(12, 5))
    st.pyplot(plt)
    plt.clf()

with tab3:
    df_combined = pd.merge(df_long_br, df_long_dr, on=["Country Name", "Country Code", "year"])
    country_df_br = df_long_br[df_long_br["Country Name"].isin(countries_filtered)]
    country_df_dr = df_long_dr[df_long_dr["Country Name"].isin(countries_filtered)]
    fig, ax = plt.subplots(figsize=(12, 5))
    for country in countries_filtered:
        data_br = country_df_br[country_df_br["Country Name"] == country]
        data_dr = country_df_dr[country_df_dr["Country Name"] == country]
        sns.lineplot(data=data_br, x="year", y="birth_rate", ax=ax, linestyle="solid", label=f"{country} (Birth)")
        sns.lineplot(data=data_dr, x="year", y="death_rate", ax=ax, linestyle="dashed", label=f"{country} (Death)")
    ax.set_title("Birth and Death Rates over Time", fontsize=12)
    ax.set_xlabel("Year")
    ax.set_ylabel("Birth/Death Rate (per 1,000 people per year)")
    st.pyplot(fig, use_container_width=True)
    plt.clf()

with tab4:
    #World Birth Rate halved
    br_1960 = df_long_br[(df_long_br["Country Name"] == "World") & (df_long_br["year"] == 1960)]["birth_rate"].values[0]
    br_2020 = df_long_br[(df_long_br["Country Name"] == "World") & (df_long_br["year"] == 2020)]["birth_rate"].values[0]
    st.info(f"🌍 Global birth rates have nearly halved — from {br_1960:.2f} in 1960 to {br_2020:.2f} in 2020.")
    country_df_br = df_long_br[df_long_br["Country Name"]== 'World']
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=country_df_br, x="year", y="birth_rate", hue="Country Name", ax=ax)
    ax.set_title("World Birth Rate over Time", fontsize=12)
    ax.set_xlabel("Year")
    ax.set_ylabel("Birth Rate (per 1,000 people per year)")
    st.pyplot(fig, use_container_width=True)
    plt.clf()

    #Sub-Saharan Africa Birth Rate
    
    st.info("🌍 Sub-Saharan Africa has the highest birth rates")
    country_df_br_ssa = df_long_br[df_long_br["Country Name"]== "Sub-Saharan Africa (excluding high income)"]
    country_df_br_ssa_c = df_long_br[df_long_br["Country Name"]== "Sub-Saharan Africa"]
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=country_df_br_ssa, x="year", y="birth_rate",label = "Sub-Saharan Africa (excluding high income)", ax=ax)
    sns.lineplot(data=country_df_br_ssa_c, x="year", y="birth_rate", label = "Sub-Saharan Africa", ax=ax)
    sns.lineplot(data=country_df_br, x="year", y="birth_rate", label = "World", ax=ax)
    ax.set_title("Birth Rate over Time", fontsize=12)
    ax.set_xlabel("Year")
    ax.set_ylabel("Birth Rate (per 1,000 people per year)")
    st.pyplot(fig, use_container_width=True)
    plt.clf()

    #Korea Birth Rate
    st.info("Korea has very low birth rates")
    country_df_br_sk = df_long_br[df_long_br["Country Name"]== 'Korea, Rep.']
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=country_df_br_sk, x="year", y="birth_rate", hue="Country Name", ax=ax)
    ax.set_title("Birth Rate over Time", fontsize=12)
    ax.set_xlabel("Year")
    ax.set_ylabel("Birth Rate (per 1,000 people per year)")
    st.pyplot(fig, use_container_width=True)
    plt.clf()