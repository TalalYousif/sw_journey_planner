"""
Load Star Wars star ships from Swapi API
"""
import requests
from http import HTTPStatus
import sw_journey_planner.starship as star_ship

# Dictionary used for time interval conversions
_interval_map = dict(year=365 * 24, month=30 * 24, week=7 * 24, day=24, hour=1)
_unknown_string = "unknown"
_swapi_property_names = dict(mglt="MGLT", consumables="consumables", name="name", results="results",
                             next="next")
_swapi_api_url = "https://swapi.co/api/starships"

_success_code = 200


def load_starships():
    """The public API to load star ships from Swapi API

    Returns:
        Generator object containing instances of Star ship
    """

    # Swapi pages the results and points to the urls of the next set of results in the response. This is the initial url
    url = _swapi_api_url

    # As long as the response contains a url for the next set of results, keep looping
    while url is not None:
        # Fetch this set of star ships from the api
        response = requests.get(url)

        # If request succeeds capture the response data
        if response.status_code == HTTPStatus.OK:
            data = response.json()
        else:
            # Otherwise raise an exception
            raise Exception(f"Unable to load star ships from Swapi. HTTP Error: {response.status_code}")

        # Update the url with the url of next page
        url = data["next"]

        # Loop through star ship objects from the response, create a StarShip instance and yield it to the generator
        for star_ship_object in data["results"]:
            yield _create_star_ship(star_ship_object)


def _create_star_ship(star_ship_object):
    """Creates an instance of Star ship from a json object

    Args:
        star_ship_object: a json object containing starship attributes

    Returns:
        a StarShip instance
    """
    # Parse the consumables from SWAPI's representation
    parsed_consumables = _parse_consumables(star_ship_object["consumables"])

    # If consumables could not be parsed set consumables in hours to None
    if parsed_consumables is None:
        consumables_in_hours = None
    else:
        # Unpack the parsed consumables into 2 variables
        increment, interval = parsed_consumables

        # Convert the increment and interval to hours
        consumables_in_hours = _convert_consumables_to_hours(increment, interval)

    # Set Mega lights to None if it's unknown, otherwise convert it to int
    mglt = None if star_ship_object["MGLT"] == _unknown_string else int(star_ship_object["MGLT"])

    # Create an instance of StarShip and return it
    return star_ship.StarShip(mglt, star_ship_object["name"], consumables_in_hours)


def _parse_consumables(consumables):
    """ Parses Swapi's string representation of consumables as an increment and an interval

    Args:
        consumables: string representing consumables, e.g, 3 weeks

    Returns:
        A tuple of increment and interval
    """
    # If consumables is unknown, it can't be parsed. Return None
    if consumables == _unknown_string:
        return None

    # Use string partitioning to separate interval from increment and save them in separate variables
    increment, _, interval = consumables.partition(" ")

    # If increment is not a number, this is an invalid consumables string, raise a value error
    if not str(increment).isdigit():
        raise ValueError("Consumables does not contain a numeric increment")

    # If interval is a plural, singularize it.
    interval = interval[:-1] if interval.endswith("s") else interval

    # Set interval to lower case
    interval = str(interval).lower()

    # Return a tuple of integer increment and string interval
    return int(increment), interval


def _convert_consumables_to_hours(increment, interval):
    """ converts a string representation of consumables to a number of hours

    Args:
        increment: A number incrementing a time interval, e.g, the 2 in 2 days
        interval: A time interval

    Returns:
        Consumables as a number
    """
    if interval not in _interval_map:
        raise KeyError("Consumables interval could not be determined")

    return increment * _interval_map[interval]
