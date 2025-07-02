def add_time(start, duration, starting_day=None):
    # Days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parsing start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0 

    # Parsing duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Adding minutes and handle carry over to hours
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60 # Calculate how many hours to carry over
    final_minute = total_minutes % 60

    # Adding hours and handle carry over to days
    total_hours = start_hour + duration_hour + extra_hour
    days_passed = total_hours // 24 # Calculate how many days to carry over
    final_hour_24 = total_hours % 24

    # converting back to 12-hour format
    period = 'AM' if final_hour_24 < 12 else 'PM'
    final_hour_12 = final_hour_24 % 12
    final_hour_12 = 12 if final_hour_12 == 0 else final_hour_12

    #construct time string
    new_time = f'{final_hour_12}:{final_minute:02d} {period}'

    # Add day of week if starting_day is provided
    if starting_day:
        start_day_index = days.index(starting_day.capitalize())
        new_day_index = (start_day_index + days_passed) % 7
        new_day = days[new_day_index]
        new_time += f', {new_day}'
    
    # Add days passed if more than 0
    if days_passed == 1:
        new_time += '(next day)'
    elif days_passed > 1:
        new_time += f'({days_passed} days later)'
    
    return new_time
