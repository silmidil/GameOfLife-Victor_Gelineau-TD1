Game of Life

This is a simple implementation of Conway's Game of Life in Python. The game simulates cellular automata on a grid, where each cell evolves based on the states of its neighbors according to predefined rules.

Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites

You need Python installed on your system. You can download it from python.org.

Install the required library:

pip install numpy

Installing

Clone this repository or download the game_of_life.py file.

Ensure numpy is installed (as mentioned in prerequisites).

Run the script using Python:

python game_of_life.py

Example:

python game_of_life.py

You will see the initial generation of the grid printed on the console. The program will then ask if you want to generate the next generation.

Input Y to continue or N to stop the program.

Running the Tests

There are no pre-built automated tests for this system, but you can manually test its functionality by:

Running the script and observing the grid evolution.

Verifying the Game of Life rules (e.g., a live cell with fewer than 2 neighbors dies).

Example Manual Test

Start the program.

Observe how the grid updates after each generation.

Verify if the changes conform to the rules of Conway's Game of Life.

Deployment

This script can be run on any machine with Python and NumPy installed. No additional deployment steps are required.

Built With

NumPy - Used for grid operations and calculations

Contributing

Feel free to fork this repository, make changes, and submit a pull request. Please ensure your contributions adhere to the coding style and include any necessary documentation.

Versioning

This project uses semantic versioning. The current version is 1.0.0.

Authors

Victor Gelineau - Initial implementation

See the list of contributors who participated in this project.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Thanks to John Conway for inventing the Game of Life.

Inspiration from cellular automata simulations.


