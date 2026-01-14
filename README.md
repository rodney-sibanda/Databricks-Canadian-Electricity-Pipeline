# Databricks-Canadian-Electricity-Pipeline

This project demonstrates a full data analytics pipeline using Databricks Lakehouse architecture, leveraging Bronze, Silver, and Gold layers to transform raw electricity and emissions datasets into business-ready insights. The included notebook walks through the data cleaning, transformation, and aggregation steps, showcasing how multiple raw datasets can be standardized, joined, and curated into reusable tables that serve as the foundation for analysis and visualization.


Ingested Ember Electricity Data Explorer exports into their own Bronze Delta tables, then built Silver standardized datasets (units, dates, region keys) and Gold analytics tables for emissions intensity and other metrics related to electricity production. The datasets used include electricity generation, installed capacity, electricity demand, power sector emissions, and carbon emissions intensity — all focused on Canada at a national level. By combining these sources, this project captures the interplay between energy production, consumption, and environmental impact over tim
