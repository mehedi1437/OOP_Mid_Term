class Star_Cinema:
    _hall_list = []

    def __init__(self,rows,cols,hall_no):
        add_list = Hall(rows,cols,hall_no)
        self._hall_list.append(add_list)

    def entry_hall(self,hall):
        self._hall_list.append(hall)

class Hall:
    def __init__(self,rows,cols,hall_no):
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        for i in range(rows):
            for j in range(cols):
                self.__seats[(i,j)] = '0'
            

    def entry_show(self,show_id,movie_name,time):
        show_info = (show_id,movie_name,time)
        self.__show_list.append(show_info)

        allocated_seat = [['0' for _ in range(self._cols)] for _ in range(self._rows)]
        self.__seats[show_id] = allocated_seat

    def book_seat(self,show_id,seat_list):
        if show_id not in self.__seats:
            print('Show ID not found.')
            return
        for seat in seat_list:
            row,col = seat
            if row<0 or row >= self._rows or col<0 or col >= self._cols:
                print('Invalid seat position')
                continue

            if self.__seats[(row,col)] == "1":
                print(f"Seat at row {row}, col {col} is already booked.")
            else:
                self.__seats[(row,col)] = "1"
                print(f"Seat at row {row}, col {col} successfully booked.")

    def view_show_list(self):
        print("Shows running in this cinema:")
        for show in self.__show_list:
            print(f'Show ID: {show[0]},Movie: {show[1]},Time: {show[2]}')

    def view_available_seats(self,show_id):
        print(f'Available __seats for show {show_id}:')
        for row in range(self._rows):
            for col in range(self._cols):
                if self.__seats[(row,col)] == '0':
                    print(f'Row: {row}, Column: {col}')
        

