# Business Problem

Cury Company is a tech firm that developed an app connecting restaurants, couriers, and customers in a marketplace model.

With this app, users can order a meal from any registered restaurant and have it delivered to their doorstep by a registered courier.

A lot of data is generated, and the CEO lacks a clear view of the company's KPIs.

As a Data Scientist, I created solutions to meet the company's needs by developing key strategic KPIs organized in a single tool. This allows the CEO to easily access important information and make simple yet impactful decisions.

To monitor business growth, the CEO would like to see the following metrics:

**Company View:**

1. Number of orders per day
2. Number of orders per week
3. Order distribution by traffic type
4. Comparison of order volume by city and traffic type
5. Number of orders per courier per week
6. Central location of each city by traffic type

**Courier View:**

1. Youngest and oldest couriers
2. Best and worst vehicle condition
3. Average rating per courier
4. Average rating and standard deviation by traffic type
5. Average rating and standard deviation by weather conditions
6. Top 10 fastest couriers by city
7. Top 10 slowest couriers by city

**Restaurant View:**

1. Number of unique couriers.
2. Average distance from restaurants to delivery locations
3. Average delivery time and standard deviation by city
4. Average delivery time and standard deviation by city and order type
5. Average delivery time and standard deviation by city and traffic type
6. Average delivery time during festivals

# Assumptions for the Analysis

1. The analysis was conducted with data from 02/11/2022 to 04/06/2022
2. The business model assumed was a marketplace
3. The three main business views were: Company View, Courier View, and Restaurant View

# Solution Strategy

The strategic dashboard was developed using metrics reflecting the three main views of the company's business model.

Each view is represented by the following set of metrics:

### Company Growth View

- Orders per day
- Percentage of orders by traffic conditions
- Number of orders by type and city
- Orders per week
- Number of orders by delivery type
- Number of orders by traffic conditions and city type

### Restaurant Growth View

- Number of unique orders
- Average distance traveled
- Average delivery time during festivals and normal days
- Standard deviation of delivery time during festivals and normal days
- Average delivery time by city
- Distribution of average delivery time by city
- Average delivery time by order type

### Courier Growth View

- Oldest and youngest couriers
- Best and worst vehicle rating
- Average rating per courier
- Average rating by traffic conditions
- Average rating by weather conditions
- Average time of the fastest courier
- Average time of the fastest courier by city

# Top 3 Data Insights

1. Order quantity shows daily seasonality, with approximately 10% variation in the number of orders on consecutive days
2. Semi-urban cities do not experience low traffic conditions
3. The greatest variations in delivery time occur during sunny weather

# Project's Final Product

Online dashboard, hosted on the cloud, accessible from any internet-connected device.

Access the dashboard via this link: [Project CuryCompany](https://curry-company-data-science-project.streamlit.app/)

# Conclusion

The goal of this project is to create a set of charts and tables displaying these metrics in the best possible way for the CEO.

From the Company View, we can conclude that the number of orders increased between week 06 and week 13 of 2022.
