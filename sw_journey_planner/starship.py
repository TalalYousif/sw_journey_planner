class StarShip:
    """Star wars star ship that can plan journeys between planets """

    def __init__(self, mglt, name, consumables):
        """Initialize a Star ship instance.

        Args:
            mglt: Max speed of the spaceship in Mega lights per hour
            name: Name of the spaceship
            consumables: Number of hour the spaceship can travel without needing resupply
        """

        self._mglt = mglt
        self._name = name
        self._consumables = consumables

    @property
    def name(self):
        """ Star ship name property

        Returns:
            Name of the star ship
        """
        return self._name

    def plan_journey(self, distance):
        """ Plan a journey with a given distance.

        Args:
            distance: Journey distance in Mega lights.

        Returns:
            The number of stops required to make the journey.
        """
        # Calculate the duration of the journey
        journey_duration = self._journey_duration(distance)

        # If the duration could not be calculated, return None
        if journey_duration is None:
            return None

        # If consumables are unknown set consumables variable to 0, else convert it to an integer
        self._consumables = 0 if self._consumables is None else int(self._consumables)

        # If consumables equal 0, return None.
        if self._consumables == 0:
            return None

        # Return the number of stops required as the quotient of duration in hours and consumables.
        return int(journey_duration / self._consumables)

    def _journey_duration(self, distance):
        """ Calculate the duration of a journey

        Args:
            distance: The distance of the journey in mega lights

        Returns:
            Duration of the journey in hours
        """

        # If max speed is unknown then the duration can't be determined. Return none
        if self._mglt is None or self._mglt == 0:
            return None

        # Assuming the ship always travels at max speed. Duration is distance divided by speed
        return distance / self._mglt
