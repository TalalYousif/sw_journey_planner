
  
# sw-journey-planner

A command line tool for calculating the number of stops for resupply required to cover a given distance, for all SW star ships.

## Installation

### Windows requirements

 - Python 3 for Windows. Can be downloaded from [here](https://www.python.org/downloads/windows/).

### Linux requirements
- Pip. Can be downloaded from [here](https://pip.pypa.io/en/stable/installing/).
    
Once these requirement are met. The solution can be installed using pip by running this command on the shell or cmd:
    
    pip install sw-journey-planner 

## Usage

On a command line, run:
`sw-journey-planner (distance)` 

where (distance) is the distance in mega lights.

e.g,
`sw-journey-planner 1000000` 

## Running the source code without installation
After cloning the repository to your local machine. Then from the command line on the root of the repository, run:

    python3 sw_journey_planner/command_line.py (distance)
