class manage_number_of_people:

    def __init__(self):
        self.now_people = 0
        self.max_people = 0
        self.count_warning = 0
        self.total_people_list = []
        self.max_people_list = []
        self.count_warning_list = []

        self.total_people = 0
        self.standard = 50
        self.n = 0

    def serial(self):
        import serial
        ser = serial.Serial('microbitの名前', 9600, timeout = None)
        i = ser.readline()
        ser.close()

    def now_time():
        import datetime
        d_now = datetime.datetime.now

    def now_people(self):
        if self.i == 1:
            self.now_people += 1
        elif self.i == 2:
            self.now_people -= 1

    def total_people(self):
        if self.i == 1:
            self.total_people += 1

    def max_people(self):
        if self.max_people < self.now_people:
            self.max_people = self.now_people

    def count_warning(self):
        if self.now_people >= self.standard:
            self.count_warinig += 1

    def total_people_list(self):
        if self.d_now.minute == 59 & self.d_now.second == 59:
            self.total_people_list[self.n] = self.total_people
            self.total_people = 0

    def max_people_list(self):
        if self.d_now.minute == 59 & self.d_now.second == 59:
            self.max_people_list[self.n] = self.max_people
            self.max_people = 0

    def count_warning_list(self):
        if self.d_now.minute == 59 & self.d_now.second == 59:
            self.count_warning_list[self.n] = self.count_warning
            self.count_warning = 0

    def n_add(self):
        self.n += 1
