from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # Tworzenie instancji personelu i sali
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    # Tworzenie instancji klientów i sprzedaż produktów w barze
    customer_instances = []
    for cust_dict in customers:
        new_customer = Customer(cust_dict["name"], cust_dict["food"])
        customer_instances.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)

    # Rozpoczęcie seansu
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
