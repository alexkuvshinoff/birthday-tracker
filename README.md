# Daily Briefings Service (Python)

Sends you a customized email every morning, with information of interest such as the upcoming weather forecast.

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/daily-briefings-py/
```

Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":

```sh
conda create -n briefings-env python=3.7
conda activate briefings-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain API Keys from the [Open Weather](https://home.openweathermap.org/api_keys), and [SendGrid](https://app.sendgrid.com/settings/api_keys) services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

APP_ENV="development" # or set to "production" on Heroku server

OPEN_WEATHER_API_KEY="___________"
MY_ZIP="10017"

SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"

MY_NAME="Jon Snow"
```

> IMPORTANT: remember to save the ".env" file :-D

## Usage

From within the virtual environment, ensure you can run each of the following files and see them produce their desired results of: printing today's weather forecast, and sending an example email, respectively.

```sh
python -m app.weather_service # note the module-syntax invocation
#> TODAY'S WEATHER FORECAST IS ...
```

```sh
python -m app.email_service # note the module-syntax invocation
#> SENDING EMAIL TO ...
```

> NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")
>
> ![](https://user-images.githubusercontent.com/1328807/77856232-c7a0ff80-71c3-11ea-9dce-7a32b88701c6.png)

As long as each of those scripts works by itself, you can send the daily briefing email:

```sh
python -m app.daily_briefing # note the module-syntax invocation
```

![](https://user-images.githubusercontent.com/1328807/77860069-173ef580-71db-11ea-83c6-5897bb9f4f51.png)
