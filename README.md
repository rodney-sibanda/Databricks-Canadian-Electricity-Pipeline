# Databricks-Canadian-Electricity-Pipeline

This project demonstrates a full data analytics pipeline using Databricks Lakehouse architecture, leveraging Bronze, Silver, and Gold layers to transform raw electricity and emissions datasets into business-ready insights. The [notebook](https://github.com/rodney-sibanda/Databricks-Canadian-Electricity-Pipeline/blob/main/Data%20Cleaning%20Notebook.py) that is included inside of this repository walks through the data cleaning, transformation, and aggregation steps, showcasing how multiple raw datasets can be standardized, joined, and curated into reusable tables that serve as the foundation for analysis and visualization.


Ingested Ember Electricity Data Explorer exports into their own Bronze Delta tables, then built Silver standardized datasets (units, dates, region keys) and Gold analytics tables for emissions intensity and other metrics related to electricity production. The datasets used include electricity generation, installed capacity, electricity demand, power sector emissions, and carbon emissions intensity — all focused on Canada at a national level. By combining these sources, this project captures the interplay between energy production, consumption, and environmental impact over tim

Screenshots of the final dashboard are included below to illustrate the key metrics and trends derived from the curated Gold tables, but if you have a databricks account you can access the dashboard [here](https://dbc-b32ccdc2-a378.cloud.databricks.com/dashboardsv3/01f0f0c4d5811ec080eb0c84cfedaf71/published?o=7474654132810972)


## Key Findings
- **Total generation, demand, and emissions:** Over the period analyzed, Canada produced a total of 6,897.7 TWh of electricity, with total demand of 6,708.5 TWh, and total power sector emissions of 1,159.4 megatonnes of CO₂.

- **Demand vs generation trends:** Electricity demand generally tracks closely with the amount generated. Early in the dataset, demand occasionally exceeded generation, but for the majority of the period, generation and demand followed a near-parallel trend, with generation slightly exceeding demand in several instances.

- **Dominant energy source:** Hydropower consistently accounts for approximately 60–65% of total electricity generation, reflecting Canada’s leadership in hydroelectric production.

- **Emissions by sector:** The top three contributors to CO₂ emissions are Gas (611.61 Mt), Coal (412.49 Mt), and Hydro (99.39 Mt) over the analyzed period. While hydro contributes to emissions, its total impact is small relative to gas and coal despite producing the majority of electricity.

- **Emissions trends over time:** Time series analysis shows that gas and coal have historically dominated emissions. Coal emissions declined steadily after 2018, while gas emissions have risen linearly, accounting for much of the current total. Other sectors have significantly lower emissions, closer to hydro than to coal.






## Screenshots of the Final Dashboard
<img width="2846" height="1096" alt="image" src="https://github.com/user-attachments/assets/c6fee725-b3b7-4b7f-b5ae-b4cf6a17553c" />

<img width="2825" height="1294" alt="image" src="https://github.com/user-attachments/assets/390e44d2-9152-487f-85c0-402585bfa7e1" />

