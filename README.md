

# <img src="images/spotify_img.png" alt="drawing" width="25"/> Spotify Genius Music Player <img src="images/genius_lyrics_image.png" alt="drawing" width="25"/> 
Spotify track app that utilizes Spotify and Genius Lyrics API to render our application in a website browser.

## Instructions

To run this app on your local machine, clone this repository using the command:
<br/>
```git clone https://github.com/csc4350-f21/project1-avenaktesh1.git```
<br/>
to the specified directory you want the project to be copied in.

### API's
This web application utilizes Spotify API and Genius lyrics API. You will need to setup an account for both of these platforms to get your **CLIENT_ID** and **CLIENT_SECRET** authentication to access the API which will need to placed in a **.env** file. 

*Note: For Genius API you will need to use a **CLIENT_ACCESS_TOKEN** to place in the **.env** file.*

More information found here about these sources on how to setup:
- [Getting started with Spotify API]("https://developer.spotify.com/documentation/web-api/quick-start/")
- [Getting started with Genius API]("https://docs.genius.com/#/getting-started-h1")

To create a **.env** file type the in terminal <code>touch .env</code> and <code>code .env</code> to open the file. This is where you will enter your environment variables as displayed:
- *export CLIENT_ID: {your-client-id}*
- *export CLIENT_SECRET: {your-client-secret}*
- *export CLIENT_ACCESS_TOKEN: {your-client-access-token}*

### Installations
This web application uses Flask framework for backend processes and Heroku for deployment.
- If you wish to run the app locally on your flask server you need to install flask. You can use the command <code>pip install flask</code> in your terminal and change the code to <code>app.run()</code> in the **app.py** file.
- If running on Heroku you wull need to install heroku as <code>sudo snap install --classic heroku</code> which should already be installed in this repository.
### Heroku Login
You will need to setup an account for Heroku in order to deploy your app on the web.
- [Create an account with Heroku]("https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true")

After creating your account in Heroku you will need to login to your account through terminal using the command <code>heroku login -i</code>. You will then be prompted to enter your username (email) and password (created when signing up on heroku).

Finally, you will need to enter your **CLIENT_ID**, **CLIENT_SECRET**, and **CLIENT_ACCESS_TOKEN** in your Heroku website in your account under configuration variables exactly as is in order to deploy the app in your local browser. Push your changes to heroku main branch by adding and committing your code and while pushing enter <code>git push heroku main</code> to finalize personal changes. 

Run <code>heroku open</code> in your terminal for your deployment step and it should open. You should be good to go!

## Technical Issues
Technical issues encountered during this project were:
- Heroku deployment error was an issue faced regarding the system logs. I fixed it by checking **Procfile** and **Requirements.txt**
- I had issues trying to figure out how to use the search endpoint for the Genius API since they give you an access_token (unlike spotify) which you could directly input into the URL directly.
    - This helped my issue with duplicate **CLIENT_ID** and **CLIENT_SECRET** when entering into the heroku configuration variable section. It saved space in my code and also removed the post request aspect.
- Figuring out how to use the API callbacks were bit of an issue due to the documentation not having the pythonic steps to detail how to use post requests to get the data from the URL like a normal API token.
    - For example: plugging in headers, parameters, authorization URL, and 

## Knowledge Problems
Knowledge problems that still persist are:
- The genius lyrics doesn't link to the actual song I want for the song displayed by the artist. Instead it displays a randomly picked song by the artist.
- The random function displays a different song each time the app is deployed. If page refreshed, it does not display a random new song.
- The artist ID's are hard coded and do not ask for any user input to randomly generate a song.
    - It does not properly access the entire spotify artist library randomly.

## Improvements
- Fixing the correct genius URL to display the exact song that is currently being played.
- Creating a shuffle option and search bar to let users be able to pick specific or random songs to make interactive instead of redeploying the app to get a different song each time.
