# Flask-API-Demonstration
A simple, functional flask API for demonstration purpose. It includes a flask API, rate limiter, JWT user authentication, session timeout, etc. This can be greatly improved with more updates in future.
<h3>1. User Login:</h3>
<p>This page asks for login credentials as set in app.py. If you want to change the login, set it manually there. Default login is: ```username: admin1``` and ```password: admin1```</p>

![Default Login-Upload Portal](https://github.com/dasabhijeet/Flask-API-Demonstration/assets/143497155/ef4280fa-834a-451d-b8dc-930f5ebe8336)


<h3>2. Index / Upload Page:</h3>
<p>This page shows the upload interface after successful login by the user. You can either upload or reset.</p>

![index](https://github.com/dasabhijeet/Flask-API-Demonstration/assets/143497155/4929af4a-c7dd-4f6d-be0f-304d0d8760db)

<h3>3. Upload Success:</h3>
<p>This page shows the uploaded image filename along with the upload successful notification. The user has an option to render that image, which redirects the user to a new webpage.</p>

![Upload-success](https://github.com/dasabhijeet/Flask-API-Demonstration/assets/143497155/f954ca16-313c-49ee-8e54-e6b39b20fc90)

<h3>4. Render Image:</h3>
<p>This page shows the rendered image with a zoom functionality. This can be much improved.</p>

![render-img](https://github.com/dasabhijeet/Flask-API-Demonstration/assets/143497155/4d8ee4c4-4b1f-42c4-a943-9a2653ee2732)

<h2>How to run this app?</h2>
<strong>Step 1:</strong><p>Install the python libraries as imported on the app.py file. Just be careful of JWT library imports because if JWT and PyJWT are both imported in the same environment, it raises an error that is hard to fix and identify. I have faced this error and wasted 3 hours, so you don't have to. :) </p>

<strong>Step 2:</strong><p>Change directory to app directory and open terminal, then type: ```python app.py```</p>

<strong>Step 3:</strong><p>Check the CMD interface and if you see something similar, then the app is running. :)</p>
![cmd_CwcIdheFfk](https://github.com/dasabhijeet/Flask-API-Demonstration/assets/143497155/533426b1-62a0-4d4a-bddb-abe147301a93)

<strong>Step 4:</strong><p>Open any web browser and type: ```http://127.0.0.1:5000/```. You will see the login page.</p>

<br><br>
<h3>I am open to suggestions on if it can be improved. :)</h3>

