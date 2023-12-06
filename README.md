# EPL Prediction: Prediction Website


This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

1. Installation : follow the step in [Installation](https://github.com/TAGCH/EPL-Prediction/blob/main/Installation.md) 
2. Running : run by typing this code in your terminal, cmd or powershell.
```
python manage.py runserver
```
Explore the web application in your browser at **http://127.0.0.1:8000**.

## Setting Up Social Applications
To enable social login features, follow these steps to set up social applications in the Django admin site:

1. Login to the Django admin site. You can access it at **http://127.0.0.1:8000/admin/**.

2. In Site section, add the site **http://127.0.0.1:8000**.

3. Under the "Social applications" section, add social applications for the authentication providers you want to use (Google).

4. For each social application, you'll typically need to provide the following information:
   - Name
   - Client ID or Key
   - Secret Key
   - Sites (You can choose the default site or the site corresponding to your application's domain)

5. Save the social applications.

Now, your Application is set up to allow social logins through the configured social applications. Users can log in and register using their social media accounts.

## Demo Admin
| Username  | Password        | Email |
|-----------|-----------------|-------|
|   Test01        |       0123456          |       |

## Demo Users
| Username  | Password        |
|-----------|-----------------|
|   demo01        |      epl1234           |
|   demo02        |      epl5678          |

To load for the demo admin and users use the following command(make sure to migrate first)
```
python manage.py loaddata data/users.json
```

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [User Stories](../../wiki/User%20Stories)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development-Plan)
- [Iteration 1 Plan](../../wiki/Iteration-1-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/2)
- [Iteration 2 Plan](../../wiki/Iteration-2-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/3)
- [Iteration 3 Plan](../../wiki/Iteration-3-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/4)
- [Iteration 4 Plan](../../wiki/Iteration-4-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/5)
- [Iteration 5 Plan](../../wiki/Iteration-5-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/9)
- [Iteration 6 Plan](../../wiki/Iteration-6-Plan) and [Task Board](https://github.com/users/TAGCH/projects/4/views/10)
- [Domain Model](../../wiki/Domain%20Model)