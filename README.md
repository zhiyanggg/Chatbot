# NTU Foodchatbot

Foodchatbot for NTU NorthSpine Canteen A

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. 

### A.1 Install Python 3 
You may install the latest Python 3 version from Python’s download page (https://www.python.org/downloads/). The Python package manager pip is included in Python 3.4 and above by default. The python version used for development in this project is version 3.6.4. The application will work perfectly fine with the latest version of python from the download page.

### A.2 Creating a Git Repository

### A.2.1 Installing Git 
Visit Git’s download page (https://git-scm.com/downloads) and install the latest version of Git.

### A.2.2 Cloning Project from GitHub 
Open command line and navigate to the directory where you wish to clone the repository. Next, run the command:
```
git clone https://github.com/zhiyanggg/Chatbot.git  
```
The source code is now cloned into your local directory. 

### A.3 Cloud Service Provider Heroku
To create a new app named “example” in Heroku, install the Heroku CLI from the page, https://devcenter.heroku.com/articles/heroku-cli and run the following commands:
```
$ mkdir example
$ cd example
$ git init
$ heroku apps:create example
```

After running the above commands, the system will output:
```
Creating ⬢ example... done
https://example.herokuapp.com/ | https://git.heroku.com/example.git
Git remote heroku added
```

The command’s output shows that the app will be available at http://example.herokuapp.com. The second URL, https://git.heroku.com/example.git, is the remote git repository URL; by default, the Heroku create command automatically adds a git remote named “heroku” pointing at this URL.

Next, extract all the contents in the folder “Chatbot”, obtained from section A.2.1. Copy and paste all the extracted contents into the directory “example” where the git was initialised in this section.

### A.4 Installing Required Python Packages 
Before you are ready to go, you will need to install all the required python packages speciﬁed in requirements.txt. These are the packages necessary for the installation of technology stack mentioned in Section 3.5. Whenever you work on the project, make sure you are in the Python virtual environment created in Step B.3.3. You can go to the virtual environment by running the workon command, as mentioned earlier. After going to the environment, navigate to the project home directory myfyp/ by using cd command in PyCharm Terminal. Next, install all required packages by running the following command:

```
pip install -r requirements.txt
```

You may list all unused dependencies by running the command below and remove them using pip uninstall.
```
pip-autoremove –list
```

### A.5. Database ClearDB 

### A.5.1 ClearDB Add-On for Heroku
Run the following command to add ClearDB to your application:

```
$ heroku addons:create cleardb:ignite
-----> Adding cleardb to sharp-mountain-4005... done, v18 (free)
Retrieve your database URL by issuing the following command:
$ heroku config | grep CLEARDB_DATABASE_URL
CLEARDB_DATABASE_URL => mysql://adffdadf2341:adf4234@us-cdbr-east.cleardb.com/heroku_db?reconnect=true
```

Copy the value of the CLEARDB_DATABASE_URL config variable.

Based on the database url config variable, we can obtain the login credentials for usage in Mysql workbench. The login credentials are formatted as shown below.

CLEARDB_DATABASE_URL => mysql://[username]:[password]@[host]/[database name]?reconnect=true

### A.5.2 Cloning of Database
Install MySql WorkBench and login using the credentials obtain in Section A.5.1. 
After logging into the server, head to the “Server” tab and select “Data Import”. Choose the option “Import from Self-Contained File” and change the directory of this option to the directory where the chatbot.sql file is at. This .sql file should by right, be at the directory where the git was initialized in section A.2.1. Once the directory has been set, click on "Start Import" and it should start uploading the file.

### A.6. Creating an App in Dialogflow
```
1.	Go to the Actions on Google Developer Console.
2.	Click on Add/import project, enter “YourAppName” for the project name, and click Create Project.
3.	Click on Skip in the upper-right corner.
4.	Click Build > Actions in the left nav.
5.	Click Add your first Action
6.	On the Custom intent card, click Build.
7.	The Dialogflow console appears with information automatically populated in an agent. Click Create to save the agent.
```

After finishing the above 7 steps to create your agent, in the left navigation, click on the gear icon to the right of the agent name. Next, click on the Export and Import tab. Click RESTORE FROM ZIP and select the FoodOrder.zip file which is found when extracting the contents in section A.2.1.

Following that, type RESTORE in the text box, click RESTORE, then DONE. When the restoration is finished, the following screen evident below, appears. Take note of your Action project's ID; you'll need it to deploy the sample's fulfillment in the future.
 

### A.7 Deploying Scripts to Cloud Service Provider
Open Command line and change the directory to the folder where the git was initialized in section A.2.1. Next, type the following commands in sequence to deploy the scripts to the Heroku Server. 

Firstly, to add all the relevant files to Git, run the command below. 
```
git add .
```

Next, to save the changes to the local repository, run the command below.
```
git commit -m “first commit”
```

Lastly, to deploy the app to Heroku, we can push the code from the local repository’s master branch to your Heroku remote with the command below.
```
git push heroku master
 ```

### Authors

* **Lim Zhi Yang** 
