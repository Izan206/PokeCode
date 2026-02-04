<img width="21" height="21" alt="image" src="https://github.com/user-attachments/assets/83de77a3-1c5f-4f27-ac37-55d319a9b6fa" /> # PokeCode 

PokeCode is a project that we made for the Server Environment signature where we built a small platform to simulate battles and display results of the combats of the Pokemons.

## Description
This repository was created as an exercise to understand client/server architectures and turn-based battle logic using the Flask framework (Python). We used FlaskSession and Jinja templates to render the backend into the front-end.

We also gave the project our own style, both visually with a retro Nintendo-like look and functionally (for example, background music similar to the original games).

## Views 

- Initial screen (Welcome)

![Initial View](app/static/images/readme/image.png)

- PokeDex (Pokemon selection)

![PokeDex View](app/static/images/readme/image2.png)

- Pokemon Details 

![Pokemon Details View](app/static/images/readme/image4.png)

-Profile page

![Profile Details View](app/static/images/readme/image8.png)

- Battle Details Page

![Battle Details page](app/static/images/readme/image9.png)

- Main Battle screen

![Battle View](app/static/images/readme/image3.png)

- Logs and battle details

![Battle details](app/static/images/readme/image6.png)

- Final Page (Winner and loser)

![Final Page](app/static/images/readme/image7.png)


Others: 

- Error page

![Error Page](app/static/images/readme/image5.png)

## Installation (using virtual environment)
**1. Clone repository:**
```
git clone https://github.com/Izan206/PokeCode.git
```
**2. Create a virtual environment:**
```
python -m venv .venv
```

**3. Install dependencies:**
```
./venv/Scripts/pip.exe install -r requirements.txt
```

**4. Create the database**
```
./venv/Scripts/flask.exe --app app.main create-tables
```
**5. Run the app**
With the virtual environment activated, start the app:
```
./.venv/Scripts/python.exe -m app.main
```

Typical development output:
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!

Open your browser at http://127.0.0.1:8080 (or the shown address).



## API: PokeAPI 
<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/a3e456f3-1f4f-4207-ae22-17649155515a" />


For this project, we used the PokeAPI public API. We worked with it to obtain different data and adapt it to the needs of our projects. We ensured that the information was received correctly and optimized the code by using caching for request processing and website speed.

To accomplish this, we created a client-side section where we handle the aforementioned tasks.

Link to the API: https://pokeapi.co/

## License
MIT License.

## Authors
Made by: 

- Izan Álvarez Varela
- Axel Cartaya Delgado

