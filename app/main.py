from app.bar.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()

    customer_instances = []
    for cust_dict in customers:
        new_customer = Customer(cust_dict["name"], cust_dict["food"])
        customer_instances.append(new_customer)
        bar_instance.sell_product(new_customer.food, new_customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
