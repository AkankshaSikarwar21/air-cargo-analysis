-- Revenue by class
SELECT class_id, COUNT(*) AS tickets, ROUND(SUM(price)) AS revenue, ROUND(AVG(price)) AS avg_price
FROM ticket_details GROUP BY class_id ORDER BY revenue DESC;

-- Monthly revenue
SELECT substr(travel_date, 1, 7) AS month, ROUND(SUM(price)) AS revenue, COUNT(*) AS tickets
FROM ticket_details GROUP BY month ORDER BY month;

-- Busiest routes
SELECT depart, arrival, COUNT(*) AS passengers
FROM passengers_on_flights GROUP BY depart, arrival ORDER BY passengers DESC LIMIT 10;

-- Top 10 spenders
SELECT c.first_name, t.customer_id, ROUND(SUM(t.price)) AS spending
FROM ticket_details t JOIN customer c ON c.customer_id = t.customer_id
GROUP BY t.customer_id ORDER BY spending DESC LIMIT 10;

-- Most frequent flyers
SELECT customer_id, COUNT(*) AS flights
FROM passengers_on_flights GROUP BY customer_id ORDER BY flights DESC LIMIT 10;

-- Revenue per flight
SELECT flight_num, COUNT(*) AS tickets, ROUND(SUM(price)) AS revenue
FROM ticket_details GROUP BY flight_num ORDER BY revenue DESC LIMIT 10;