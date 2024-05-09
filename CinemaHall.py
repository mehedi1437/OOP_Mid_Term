class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self,hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        for i in range(rows):
            for j in range(cols):
                self._seats[(i,j)] = '0'
            

    def entry_show(self,show_id,movie_name,time):
        show_info = (show_id,movie_name,time)
        self._show_list.append(show_info)

        allocated_seat = [['0' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = allocated_seat

    def book_seat(self,show_id,row,col):
        if show_id not in {show[0] for show in self._show_list}:
            print('Show ID not found.')
            return
        if(row,col) not in self._seats:
            print("Invalid seat position. ")
            return

        if self._seats[(row,col)] == "1":
            print(f"Seat at row {row}, col {col} is already booked.")
        else:
            self._seats[(row,col)] = "1"
            print(f"Seat at row {row}, col {col} successfully booked.")

        print("Updated Seats view :")
        for i in range(self._rows):
            for j in range(self._cols):
                seat_status = self._seats.get((i, j), "0") 
                print(seat_status, end=" ") 
            print()
            

    def view_show_list(self):
        print("Shows running in this hall :")
        for show in self._show_list:
            print(f'Movie: {show[1]}({show[0]}),Show ID: {show[0]},Time: {show[2]}')

    def view_available_seats(self,show_id):
        print(f'Available _seats for show {show_id}:')
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[(row,col)] == '0':
                    print(f'Row: {row}, Column: {col}')


starCineplex = Star_Cinema()

hall_1 = Hall(9,9,111)
# hall_2 = Hall(8,8,123)
# hall_3 = Hall(9,9,303)

starCineplex.entry_hall(hall_1)
# starCineplex.entry_hall(hall_2)
# starCineplex.entry_hall(hall_3)

hall_1.entry_show(111,"Jawan","2024-05-09 18:00:00")
hall_1.entry_show(111,"Surongo", "2024-05-10 15:30:00")
hall_1.entry_show(111,"Animal","2024-05-11 20:00:00")

# hall_2.entry_show(123,"12th Fail","2024-05-09 18:00:00")
# hall_2.entry_show(123,"Leo", "2024-05-10 15:30:00")
# hall_2.entry_show(123,"Alienoid","2024-05-11 20:00:00")

# hall_3.entry_show(303,"The Peison","2024-05-09 18:00:00")
# hall_3.entry_show(303,"Badland Hunters", "2024-05-10 15:30:00")
# hall_3.entry_show(303,"Master","2024-05-11 20:00:00")



while True:
    print("Welcome to our Cinema Hall !")
    print("1. ALL SHOW LIST ")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        starCineplex._hall_list[0].view_show_list()
    elif choice == 2:
        id = int(input("Enter Your Show ID : "))
        starCineplex._hall_list[0].view_available_seats(id)
    elif choice == 3:
        show_id = int(input("Enter your show ID : "))
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        starCineplex._hall_list[0].book_seat(show_id,row,col)
    elif choice == 4:
        break
    else:
        print("Invalid input")


        

