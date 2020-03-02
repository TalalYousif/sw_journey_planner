#!/usr/bin/env python3

"""
Program entry point
"""

import sys
# Swapi api is imported as loader to serve as an exchangeable interface.
# Any class or module can replace Swapi, as long as it implements a load_starships function
import sw_journey_planner.swapi as loader

# Constant for unknown number of  stops
_unknown_string = "Unknown"


def main():

    # user input
    distance = sys.argv[1]

    # Validate the input
    if not distance.isdigit():
        raise ValueError("Distance should be an integer number")

    # ensure distance is an integer
    distance = int(distance)

    # Loop through the star ships and plan their journeys
    for star_ship in loader.load_starships():
        # Ask the star ship to plan the journey
        stops = star_ship.plan_journey(distance)

        # Print the name of star ship and the number of stops required to make the journey.
        # Print Unknown if the number of stops could not be determined
        print(f"{star_ship.name}: {_unknown_string if stops is None else stops}")


if __name__ == "__main__":
    main()
