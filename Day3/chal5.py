#
# Challenge 5
#
# Create a variable called `time`, a
# variable called `place_of_work` and
# a variable called `town_of_home`.
# Create an if statement that prints
# where someone is at times of the day.
#
# E.g. if the time is 7 I’m at home,
# at 8 I’m commuting, at 9 I’m at work.


def time_travel():
    time = int(input('Input an Hour of the day [17 for 5PM]'))
    place_of_work = 'Evil Corp.'
    town_of_home = 'Plesentville'

    planner = [
        {'time': 0,
         'location': town_of_home},
        {'time': 1,
         'location': town_of_home},
        {'time': 2,
         'location': town_of_home},
        {'time': 3,
         'location': town_of_home},
        {'time': 4,
         'location': town_of_home},
        {'time': 5,
         'location': town_of_home},
        {'time': 6,
         'location': town_of_home},
        {'time': 7,
         'location': town_of_home},
        {'time': 8,
         'location': town_of_home},
        {'time': 9,
         'location': place_of_work},
        {'time': 10,
         'location': place_of_work},
        {'time': 11,
         'location': place_of_work},
        {'time': 12,
         'location': place_of_work},
        {'time': 13,
         'location': place_of_work},
        {'time': 14,
         'location': place_of_work},
        {'time': 15,
         'location': place_of_work},
        {'time': 16,
         'location': place_of_work},
        {'time': 17,
         'location': place_of_work},
        {'time': 18,
         'location': town_of_home},
        {'time': 19,
         'location': town_of_home},
        {'time': 20,
         'location': town_of_home},
        {'time': 21,
         'location': town_of_home},
        {'time': 22,
         'location': town_of_home},
        {'time': 23,
         'location': town_of_home},
    ]
    for hour in planner:
        if hour["time"] == time:
            if hour["time"] > 12:
                pretty_time = f'{time - 12}PM'
            if hour["time"] == 12:
                pretty_time = f'{time}PM'
            if hour["time"] < 12:
                pretty_time = f'{time}AM'
            print(
                f'At {pretty_time} you will be located at {hour["location"]}')
