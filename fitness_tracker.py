# a fitness tracker project using OOps
from dateutil import parser
import time
class workout(object):
    """A workout class"""
    cal_hr = 200
    def __init__(self,start_time,end_time,calories = None):
        self.start = start_time
        self.end = end_time
        self.icon = '😰'
        self.type = 'workout'
        self.calories = calories
    def __str__(self):
        return f'{self.type} {self.icon} \n start: {self.start} \n end: {self.end} \n cal🔥: {self.calories} kcal'
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_calories(self):
        if self.calories != None:
            return self.calories
        else:
            return workout.cal_hr*((parser.parse(self.end)-parser.parse(self.start)).total_seconds()/3600)
    def set_start(self, input):
        self.start = input
    def  set_end(self,input):
        self.end = input
    def set_calories(self,input):
        self.calories = input 
    def total_calories(self,workouts):
        total = 0
        for i in workouts:
            total += i.get_calories()
        return total




class run(workout):
    def __init__(self, start_time, end_time,elev = 0, calories=None):
        super().__init__(start_time, end_time, calories)
        self.icon = '🏃‍♂️'
        self.type = 'running'
        self.elevation = elev
    def get_elevation(self):
        return self.elevation
    def set_elevation(self,input):
        self.elevation = input
l1 = workout("11:00 PM","11:30 PM")
l2 = workout("11:00 PM","11:30 PM")
l3 = workout("11:00 PM","11:30 PM")


class swim(workout):
    def __init__(self, start_time, end_time,style = None, calories=None):
        super().__init__(start_time, end_time, calories)
        self.kind = "swimming"
        self.icon = "🏊"
        self.style = style
        self.duration = parser.parse(end_time) - parser.parse(start_time)
    def get_duration(self):
        return self.duration
    def set_style(self,input):
        self.style = input
    def __str__(self):
        post = f' {19*"_"}\n'
        post += f'|{self.icon} {" "*16}|\n'
        post += f'| type: {self.kind} {" "*(10-len(self.kind))} | \n'
        post += f'| start: {self.start} {" "*(9-len(self.start))} | \n'
        post += f'| end: {self.end} {" "*(11-len(self.end))} | \n'
        post += f'| style: {self.style} {" "*(9-len(self.style))} | \n'
        if self.calories != None:
            post += f'| cal🔥: {self.calories} kcal {" "*(4-len(str(self.calories)))} | \n'
        else:
            post += f'| cal🔥: {self.calories} {" "*(13-len(self.end))} | \n'
        post += f' {19*"_"}'
        return post
t = time.perf_counter()
l1= swim("12:00 AM","1:47 PM","stroke")
l1.get_calories()
dt = time.perf_counter() - t
print(dt)
# print(l1.get_calories())