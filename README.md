# A small app to add modifiers to icalendar feeds

- E.g. you want to change multiday events to singleday events

I'm having all my Facebook events in my Google calendar. Works fine except some
people make events like "winter practices" that clutter calendar view. This app
includes a small modifiers for your icalendar feeds to switch multiday events
to take only couple hours.

See live at https://icalendar-modifier.herokuapp.com/

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ pip install -r requirements.txt
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```

## Documentation

