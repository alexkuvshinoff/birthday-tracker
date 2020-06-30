# Birthday Tracker (Python)

Sends a customized email the in the morning with the first, last name and age of friends on the day of their birthday so that you can remember to wish them happy birthday

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/birthday-tracker-py/
```

Create and activate a new Anaconda virtual environment, perhaps named "birthday-env":

```sh
conda create -n birthday-env python=3.7
conda activate birthday-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain API Keys from the [Open Weather](https://home.openweathermap.org/api_keys), and [SendGrid](https://app.sendgrid.com/settings/api_keys) services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

APP_ENV="production" 

Google sheet set up:

"https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
"https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.


SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"
MY_NAME="Alex Kuvshinoff"
```

> IMPORTANT: remember to save the ".env" file

## Usage

From within the virtual environment, ensure you can send an email

> NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")

## Schedule in Heroku

Use the scheduler option in Heroku website to send an email daily:

```sh
python -m app.birthday_tracker # note the module-syntax invocation
```

