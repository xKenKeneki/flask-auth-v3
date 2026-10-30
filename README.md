# Flask Auth Practice

A small project I built to learn the basics of Flask: user registration, login with sessions, password hashing and a protected profile page.

> ⚠️ **This is a learning project, not meant for production.** It has known flaws (listed below) that I left on purpose to fix in my next project. Please don't use a real password.

> 📝 **A note on authorship:** I did not write the HTML interface (the files in `templates/`); it was generated with AI. My part in this project was the Python/Flask side: the routes, sessions, password hashing, JSON storage, form validation, and connecting the templates to the backend (`render_template`, Jinja variables, form fields and links).

## Features

- Register with username, email, password and date of birth (18+ only)
- Login / logout using Flask sessions
- Passwords stored as hashes (Werkzeug), never in plain text
- Profile page only accessible to logged-in users
- Users saved in a local `data.json` file

## Project structure
```
.
├── app.py              # creates the Flask app and registers the routes
├── data.json           # "database" (starts as an empty list: [])
├── routes/
│   ├── __init__.py     # register_routes(): registers all blueprints
│   ├── homepage.py
│   ├── login.py
│   ├── logout.py
│   ├── profile.py
│   └── register.py
└── templates/
    ├── homepage.html
    ├── login.html
    ├── profile.html
    └── register.html

```

## How to run

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv

   # Linux / macOS
   source venv/bin/activate

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

   ```
2. Install the dependencies:
   ```bash
   pip install flask

   ```
3. Set the `SECRET_KEY` environment variable (required for sessions to work):
   ```bash
   # Linux / macOS
   export SECRET_KEY="any-random-text-here"

   # Windows (PowerShell)
   $env:SECRET_KEY="any-random-text-here"

   ```
4. Run the app and open [http://127.0.0.1:5000](http://127.0.0.1:5000):
   ```bash
   flask run

   ```

Make sure `data.json` exists and contains `[]` before registering the first user.

## What I learned

- How to structure a Flask app with **Blueprints** and a `register_routes()` function
- How **sessions** work and how to protect a route (redirecting to login when there is no `username` in the session)
- How to hash and check passwords with `generate_password_hash` and `check_password_hash`
- How to read form data with `request.form` and handle `GET` vs `POST`
- How to render pages with **Jinja2** templates (`{% if %}`, `{{ variable }}`)
- How to read and write a JSON file with Python
- How to keep secrets out of the code using environment variables

## Known limitations

I know this project has flaws. I left them here on purpose, as a checklist of what to fix in my next project (Flask + SQL).

| Problem                                          | Why it matters                                                              | How I plan to fix it                                 |
| ------------------------------------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------- |
| No CSRF protection on forms                      | Another site could trick a logged-in user into sending a POST request       | Use Flask-WTF (`CSRFProtect`)                        |
| `data.json` used as database                     | Two requests at the same time can corrupt the file; no real queries         | Migrate to SQL (SQLite/PostgreSQL + SQLAlchemy)      |
| No error message on wrong login                  | The user can't tell if the password was wrong                               | Pass an `error` to `login.html`                      |
|                                                  |                                                                             |                                                      |
| Age check logic is wrong in some edge cases      | Some users near their 18th birthday may be accepted or rejected incorrectly | Calculate age with `(month, day)` comparison         |
| Empty birth date crashes the page                | `strptime` runs before the empty-field check, causing a 500 error           | Validate empty fields before converting the date     |
| Error messages reveal if a username/email exists | Allows user enumeration                                                     | Use generic messages                                 |
| Maximum password length of 20                    | Limits security for no technical reason                                     | Remove the upper limit                               |
| `flash()` messages are never displayed           | Feedback is lost                                                            | Render `get_flashed_messages()` in the templates     |
| `SECRET_KEY` is `None` if not set                | Sessions break with a confusing error                                       | Fail with a clear message or use a dev-only fallback |

## Next steps

- [ ] Next project: Flask + SQL
- [ ] Add CSRF protection
- [ ] Add more security practices (input validation, rate limiting, secure cookies)

## Tech

- Python 3
- Flask
- Werkzeug (password hashing)
- HTML (no frameworks, interface generated with AI)



For my next learning project, I intend to make things much more organized, clean, and compact, and to learn a great deal more—for instance, by delving deeper into HTML and CSS.
