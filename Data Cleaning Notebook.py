# Databricks notebook source
# MAGIC %sql
# MAGIC --- Silver Layer Creation
# MAGIC -- Ember data is largely analysis-ready, so transformations are minimal
# MAGIC CREATE OR REPLACE TABLE energy.silver.carbon_intensity_clean AS
# MAGIC SELECT *
# MAGIC FROM energy.bronze.carbon_intensity_raw;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE energy.silver.electricity_demand_clean AS
# MAGIC SELECT *
# MAGIC FROM energy.bronze.electricity_demand_raw;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE energy.silver.electricity_generation_clean AS
# MAGIC SELECT *
# MAGIC FROM energy.bronze.electricity_generation_raw;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE energy.silver.power_sector_clean AS
# MAGIC SELECT *
# MAGIC FROM energy.bronze.power_sector_emissions_raw;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE energy.silver.yearly_electricity_clean AS
# MAGIC SELECT *
# MAGIC FROM energy.bronze.yearly_electricity_capacity_raw;
# MAGIC
# MAGIC --- DATA CLEANING
# MAGIC
# MAGIC DELETE FROM energy.silver.electricity_generation_clean
# MAGIC WHERE series IN ('Total generation', 'Other renewables', 'Other fossil');
# MAGIC
# MAGIC DELETE FROM energy.silver.power_sector_clean
# MAGIC WHERE series IN ('Total generation', 'Other renewables', 'Other fossil')
# MAGIC
# MAGIC
# MAGIC -- Note: Ember datasets are pre-standardized and validated.
# MAGIC -- Cleaning focuses on removing aggregate series to prevent double counting.
# MAGIC
# MAGIC
# MAGIC --- GOld Layer -  This section creates business-ready aggregated tables and metrics
# MAGIC
# MAGIC
# MAGIC
# MAGIC --- Carbon Emissions vs the Amount of Electricity Demanded
# MAGIC
# MAGIC ---- This Table is would help show whether growth been decoupled from emissions growth
# MAGIC CREATE OR REPLACE TABLE energy.gold.emissions_vs_demand AS
# MAGIC SELECT 
# MAGIC   d.demand_twh,
# MAGIC   d.date,
# MAGIC   c.emissions_intensity_gco2_per_kwh
# MAGIC FROM energy.silver.electricity_demand_clean d
# MAGIC LEFT JOIN energy.silver.carbon_intensity_clean c
# MAGIC   ON d.date = c.date
# MAGIC
# MAGIC
# MAGIC --- Electricity Generation vs Electricity Capacity
# MAGIC
# MAGIC --- This table shows the level of energy utilization where it looks at amount capacity that is presently available and comapres with the amount of electricity that is generated
# MAGIC CREATE OR REPLACE TABLE energy.gold.generation_vs_capacity AS
# MAGIC
# MAGIC SELECT 
# MAGIC   MAKE_DATE(CAST(i.date AS INT), 1, 1) AS year_date,
# MAGIC   i.capacity_gw,
# MAGIC   i.series,
# MAGIC   g.generation_twh
# MAGIC FROM energy.silver.yearly_electricity_clean i
# MAGIC LEFT JOIN energy.silver.electricity_generation_clean g 
# MAGIC ON YEAR(g.date) = CAST(i.date AS INT);
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC