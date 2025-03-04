class RailwayForm:
    formtype = "Railway Standard Form :"

    def init(self, name, age, station, adress):
        self.name = name
        self.age = age
        self.adress = adress
        self.station = station

    def form(self, signature):
        print(f"{self.formtype}")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Address :{self.adress}")
        print(f"You have reached {self.station}\n{signature}!")


rail = RailwayForm()
rail.name = "Harry"
rail.age = "12"
rail.adress = "Bhutan"
rail.station = "Seemanchal Station."
rail.form("ThankYou ")
rail.train_number = "12345"
rail.departure_time = "10:00 AM"
rail.arrival_time = "02:00 PM"
rail.ticket_price = "$50"

print(f"Train Number: {rail.train_number}")
print(f"Departure Time: {rail.departure_time}")
print(f"Arrival Time: {rail.arrival_time}")
print(f"Ticket Price: {rail.ticket_price}")
