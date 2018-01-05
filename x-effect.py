import optparse
import pickle
import datetime


def main():

    """Initializes and Parses the commandline arguments."""
    p = optparse.OptionParser()
    p.add_option('--show', '-s', action="store_true", default=False,
                 help="Display the calendar")
    p.add_option('--tick', '-t', action="store_true", default=False,
                 help="Tick the current day off")
    options, arguments = p.parse_args()

    if options.tick:
        calendar = load_calendar()
        if not calendar:
            new_calendar()
            calendar = load_calendar()
        tick_calendar(calendar)
        save_calendar(calendar)
        draw_calendar(calendar)

    if options.show:
        calendar = load_calendar()
        if calendar:
            draw_calendar(calendar)
        else:
            print("No calendar available.")


def draw_calendar(calendar):
    """Prints the current calendar to the terminal"""
    for i in range(7):
        print('|', end='')
        for j in range(7):
            print(calendar[i*7 + j+1], end='|')
        print("\n", end='')


def save_calendar(calendar):
    """Saves the current calendar at calendar.p"""
    pickle.dump(calendar, open("calendar.p", "wb"))


def load_calendar():
    """Loads calendar.p and returns as calendar."""
    try:
        calendar = pickle.load(open("calendar.p", "rb"))
    except OSError:
        return False
    return calendar


def new_calendar():
    """Creates a new calendar by filling a list with blanks containing a space"""
    calendar = [" " for i in range(49 + 1)]
    calendar[0] = datetime.datetime.now()
    pickle.dump(calendar, open("calendar.p", "wb"))


def tick_calendar(calendar):
    """Adds a tick mark to the array at current date."""
    today = datetime.datetime.now()
    day_diff = compare_date(today, calendar[0])
    if len(calendar) > day_diff + 1:
        calendar[day_diff + 1] = "✓"
    else:
        print("You have passed the 49 day mark.")


def compare_date(today, start_date):
    """Compares the start date and current date and returns the difference in days."""
    difference = today - start_date
    return difference.days


if __name__ == '__main__':
    main()
