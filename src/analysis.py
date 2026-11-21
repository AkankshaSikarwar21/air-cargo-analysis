import os
import pandas as pd

customer = pd.read_csv("data/sample/customer.csv")
tickets = pd.read_csv("data/sample/ticket_details.csv")
passengers = pd.read_csv("data/sample/passengers_on_flights.csv")

os.makedirs("results", exist_ok=True)

tickets.groupby("class_id")["price"].sum().reset_index(name="total_revenue") \
    .to_csv("results/revenue_by_class.csv", index=False)

passengers.groupby(["depart", "arrival"]).size().reset_index(name="total_passengers") \
    .sort_values("total_passengers", ascending=False).to_csv("results/busiest_routes.csv", index=False)

passengers.groupby("customer_id").size().reset_index(name="total_flights") \
    .sort_values("total_flights", ascending=False).to_csv("results/regular_customers.csv", index=False)

top = tickets.groupby("customer_id")["price"].sum().reset_index(name="total_spending") \
    .sort_values("total_spending", ascending=False)
top.merge(customer[["customer_id", "first_name"]], on="customer_id", how="left") \
    .to_csv("results/top_spenders.csv", index=False)

print("Analysis results saved in the 'results' folder.")