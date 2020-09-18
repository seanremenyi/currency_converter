# Currency Converter APP

This is a terminal currency converter application that I have created that consumes an API.

### __Purpose__

The purpose of this application is to give the user a way to convert from one currency to another any amount of money they input. The API has dozens of currencies available.

### __Target Audience__

Developers and other versed in using terminal applications who would like to just convert money from one currency to another.
### __Outside Resources__

This application an API which can be found at 
https://exchangeratesapi.io/ which uses data published from the European Central Bank.


### __Set Up__

This application uses python3.8 and some python3.8 modules

##### For the App,

1. Create a directory to clone the git repo into
2. Clone git repo
3. If not running python 3.8, run the following bash commands
    1. `sudo apt update`
    2. `sudo apt install python3.8`
4. Create a virtual enviornment
    1. `sudo apt-get install python3-pip`
    2. `sudo apt-get install python3-venv`
    3. `python3 -m venv venv`
5. Install the modules in requirements.txt


### __Running the APP__

The application can be ran by using the following bash command

`python3.8 main.py`

From here the app will ask you for the currency you are converting from. 

The Application expects the format of three capitalized letters. For example

`AUD`

You will then be asked for the currency you are converting to, in the same format.

You can input 1 to receive all the available currencies the API has access to.

You will then be prompted for the amount to convert and you will get the results.


# Hope you enjoy!
