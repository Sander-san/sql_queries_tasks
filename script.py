from dotenv import dotenv_values
from models import DatabaseConnector


config = dotenv_values(".env")

connector = DatabaseConnector(dbname=config['dbname'],
                              user=config['user'],
                              password=config['password'],
                              host=config['host'],
                              port=config['port'])

connector.connect()

queries = [
    '''select name, count(film_id) as count
from film_category
join category using(category_id)
group by name
order by count desc;''',
    '''Select name
From (
select concat(first_name, ' ', last_name) as name,  count(rental_date) as count 
from actor right join film_actor using(actor_id)
Join film using(film_id)
Join inventory using(film_id)
Join rental using(inventory_id)
group by name
Order by count Desc
Limit 10
) as t;''',
    '''Select name
From (
Select name, sum(amount) as total_sum
From category 
Join film_category using(category_id)
Join film using(film_id)
Join inventory using(film_id)
Join rental using(inventory_id)
Join payment using(rental_id)
Group by name
Order by total_sum desc
Limit 1
) as t;''',
    '''Select distinct title
From film
Left Join inventory using(film_id)
Where inventory_id is null;''',
    '''With temp_table as (
Select first_name, last_name, count(actor_id) as count
From actor
Join film_actor using(actor_id)
Join film using(film_id)
Join film_category using(film_id)
join category using(category_id)
Where category.name = 'Children'
Group by first_name, last_name
Order by count desc
)

Select concat(first_name, ' ', last_name) as name
From temp_table
Where count in (
select distinct count 
from temp_table
Order by count desc
limit 3
);''',
    '''Select city,
COUNT(CASE WHEN customer.active = 1 THEN 1 END) AS active_customers, 
COUNT(CASE WHEN customer.active = 0 THEN 1 END) AS inactive_customers
From customer
Join address using(address_id)
Join city using(city_id)
Group by city
Order by inactive_customers desc;''',
    '''With rental_hours as (
Select category.name, sum(DATE_PART('hour', return_date - rental_date)) as  total_rental_hours
From customer c
Join address a on c.address_id = a.address_id
Join city on a.city_id = city.city_id
Join rental r on c.customer_id = r.customer_id
Join inventory using(inventory_id)
Join film using(film_id)
Join film_category on film.film_id = film_category.film_id
Join category on film_category.category_id = category.category_id
where city.city like '%-%'
Group by category.name
UNION
Select category.name, sum(DATE_PART('hour', return_date - rental_date)) as  total_rental_hours
From customer c
Join address a on c.address_id = a.address_id
Join city on a.city_id = city.city_id
Join rental r on c.customer_id = r.customer_id
Join inventory using(inventory_id)
Join film using(film_id)
Join film_category on film.film_id = film_category.film_id
Join category on film_category.category_id = category.category_id
where title like 'A%'
Group by category.name
)

Select name from rental_hours
Where total_rental_hours = (
Select max(total_rental_hours)
From rental_hours
);'''
]

with open('queries.sql', 'w') as f:
    for num, query in enumerate(queries):
        f.write(f"Query №{num+1}\n" + query + '\n\n')

for el in queries:
    res = connector.fetch_data(el)
    with open('result.txt', 'w') as r:
        r.write(f'{res}\n')

connector.close()
