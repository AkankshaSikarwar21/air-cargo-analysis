
# Air Cargo Analysis

An end-to-end analysis of airline ticket sales, route demand and customer behaviour using Python, SQL and an interactive Streamlit dashboard.


> Note: the data is a **synthetic practice dataset** generated with `src/generate_dataset.py`. It is not real airline data, so the findings are illustrative.

## Problem Statement
An airline wants to know where its revenue comes from, which routes and flights perform best, and which customers matter most, so it can decide where to add capacity, change pricing and run loyalty offers.

## Dataset
Five related tables (Jan to Oct 2024):

| Table | Rows | Contents |
|---|---|---|
| `customer` | 50 | customer details and registration date |
| `route_details` | 10 | routes with distance in miles |
| `flight_details` | 10 | flights with departure and arrival times |
| `ticket_details` | 300 | ticket price, class and travel date per customer |
| `passengers_on_flights` | 300 | departure, arrival, seat and class per passenger |

## Approach
1. Generated and checked the five tables with Python.
2. Analysed revenue, routes, customers and flights with pandas (`src/analysis.py`).
3. Wrote six SQL queries (`sql/analysis.sql`) and ran them on SQLite (`src/run_sql.py`).
4. Built an interactive Streamlit dashboard with a class filter (`app/app.py`).

## Key Insights
- Total revenue is **3.09M** from **300 tickets** (average ticket about 10.3K).
- **Economy is 72% of tickets but only 46% of revenue.** Business and First are 28% of tickets but **54% of revenue**.
- Revenue peaks in **June** (484K, 16% of total) and drops **57% in July**.
- **Bangalore to Delhi** is the busiest route (41 passengers). **62%** of passengers fly on a route touching Delhi.
- Routes are imbalanced: Delhi to Mumbai has only 15 passengers vs 32 for Mumbai to Delhi.
- The top 10 customers (20% of customers) bring **35%** of revenue, so revenue is spread fairly evenly.
- Flight **AI104** earns 14% of revenue; **AI101** earns the least (135K from 15 tickets).

## Recommendations
1. **Upsell premium cabins:** Business and First give over half the revenue from under a third of tickets.
2. **Plan for the June peak** and run offers to soften the July drop.
3. **Review Delhi to Mumbai** schedule and pricing, since it flies much emptier than the return leg.
4. **Review flight AI101:** reprice, reschedule or reassign the aircraft.
5. **Start a loyalty programme** for the top spenders and most frequent flyers.

## Dashboard Screenshots

### Revenue
![Revenue](images/01_revenue.png)

### Routes
![Routes](images/02_routes.png)

### Customers
![Customers](images/03_customers.png)

### Flights
![Flights](images/04_flights.png)

## Tech Stack
Python, pandas, Plotly, SQL (SQLite), Streamlit, Git and GitHub.

## Project Structure
```
air-cargo-analysis/
├── app/app.py              # Streamlit dashboard
├── data/sample/            # the 5 CSV tables
├── images/                 # dashboard screenshots
├── results/                # CSV outputs of the analysis
├── sql/analysis.sql        # SQL queries
├── src/analysis.py         # pandas analysis
├── src/run_sql.py          # runs the SQL file on SQLite
├── src/generate_dataset.py # creates the synthetic data
└── requirements.txt
```

## Run Locally
```
git clone https://github.com/AkankshaSikarwar21/air-cargo-analysis.git
cd air-cargo-analysis
pip install -r requirements.txt
python src/analysis.py
python src/run_sql.py
streamlit run app/app.py
```

## Author
**Akanksha Sikarwar**, Data Analyst | AI & Data Science
[GitHub](https://github.com/AkankshaSikarwar21) | [LinkedIn](https://linkedin.com/in/akanksha-sikarwar) | sikarwarakanksha21@gmail.com
