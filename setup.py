import setuptools

setuptools.setup(
    name="sw_journey_planner",
    version="1.0.5",
    description="A StarWars journey planner",
    packages=["sw_journey_planner"],
    entry_points={
        'console_scripts': ['sw-journey-planner=sw_journey_planner.command_line:main'],
    }
)