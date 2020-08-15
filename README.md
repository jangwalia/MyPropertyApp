#Property App Project
In this App User can serarch the property by entering the price range . Our App uses the Realtor CA's API and Google Map's API to get the desired results.
#INITIAL SETUP
1.Install VS Code which is the most populer Free IDE available for developers.
1.Then Create The project folder in your Workspace Folder and name in Property App. All the folders will be inside this root folder from now.
Setting up a Python Virtual Environment
When you create a Python application, it will use packages and modules that do NOT come as part of the standard Python library (e.g. csv or os).

Additionally, different applications may use different versions of Python. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and will lead to an application not able to run.

We resolve this by using virtual environments which are self-contained directories of a particular Python installation and their packages. This is a nice, clean way to have your application only use what it needs without "polluting" other applications.

We create virtual environments by using the venv module as follows:

python -m venv <name of the virtual environment folder>
A good way to start is to simply call your virtual environment folder venv as well so that your command from the Terminal looks like:

python -m venv venv
This will create a venv/ directory and store all the Python related dependencies that you install.

Once the virtual environment folder is created, you have to activate the virtual environment.

On Windows, run:

venv\Scripts\activate
Your virtual environment is active if you see the name venv prefixed to your terminal prompt like in the following:


