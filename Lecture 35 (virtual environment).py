# Virtual environment:-
"""Create a virtual environment:-
python -m venv myenv

Activate the virtual environment (Windows):-
myenv\Scripts\activate.bat

Deactivate the virtual environment:-
deactivate

Output the list of installed packages and their versions to a file:-
pip freeze > requirements.txt

Install the packages listed in the requirements.txt file:-
pip install -r requirements.txt"""

"""Install pandas:-
pip install pandas"""

# Verifying the Installation of pandas
import pandas as pd
print(pd.__version__)

