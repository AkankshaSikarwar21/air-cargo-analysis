import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Air Cargo Analysis", layout="wide")


@st.cache_data
def load():
    t = pd.read_csv("data/sample/ticket_details.csv", parse_dates=["travel_date"])
    p = pd.read_csv("data/sample/passengers_on_flights.csv")
    c = pd.read_csv("data/sample/customer.csv")
    return t, p, c


tickets, pax, cust = load()
st.title("Air Cargo Analysis")
st.caption("Synthetic dataset generated for practice.")

classes = sorted(tickets.class_id.unique())
sel = st.sidebar.multiselect("Class", classes, default=classes)
t = tickets[tickets.class_id.isin(sel)]
p = pax[pax.class_id.isin(sel)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", f"{t.price.sum():,.0f}")
c2.metric("Tickets", f"{len(t):,}")
c3.metric("Customers", f"{t.customer_id.nunique():,}")
c4.metric("Avg ticket price", f"{t.price.mean():,.0f}")

t1, t2, t3, t4 = st.tabs(["Revenue", "Routes", "Customers", "Flights"])

with t1:
    a, b = st.columns(2)
    rc = t.groupby("class_id").price.sum().reset_index()
    a.plotly_chart(px.bar(rc, x="class_id", y="price", title="Revenue by class"))
    m = t.assign(month=t.travel_date.dt.to_period("M").astype(str)).groupby("month").price.sum().reset_index()
    b.plotly_chart(px.line(m, x="month", y="price", markers=True, title="Monthly revenue"))

with t2:
    r = p.groupby(["depart", "arrival"]).size().reset_index(name="passengers")
    r["route"] = r.depart + " to " + r.arrival
    r = r.nlargest(10, "passengers")
    st.plotly_chart(px.bar(r, x="passengers", y="route", orientation="h",
                           title="Busiest routes").update_yaxes(autorange="reversed"))

with t3:
    sp = t.groupby("customer_id").price.sum().reset_index(name="spending")
    sp = sp.merge(cust[["customer_id", "first_name"]], on="customer_id", how="left").nlargest(10, "spending")
    sp["customer"] = sp.first_name + " (" + sp.customer_id.astype(str) + ")"
    a, b = st.columns(2)
    a.plotly_chart(px.bar(sp, x="spending", y="customer", orientation="h",
                          title="Top 10 spenders").update_yaxes(autorange="reversed"))
    fl = p.groupby("customer_id").size().reset_index(name="flights").nlargest(10, "flights")
    fl["customer_id"] = fl.customer_id.astype(str)
    b.plotly_chart(px.bar(fl, x="customer_id", y="flights", title="Most frequent flyers"))

with t4:
    f = t.groupby("flight_num").price.agg(["count", "sum"]).reset_index()
    f.columns = ["flight_num", "tickets", "revenue"]
    st.plotly_chart(px.bar(f.nlargest(10, "revenue"), x="flight_num", y="revenue",
                           title="Top 10 flights by revenue"))
    st.dataframe(f.sort_values("revenue", ascending=False))