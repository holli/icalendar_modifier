# A small django/python/heroku app to add modifiers to icalendar feeds

This django/python/heroku app is a basic example to get ical from one address, modify
the events and render the output again. See
https://github.com/holli/icalendar_modifier/blob/master/modifiers/views.py#L56

I'm having all my Facebook events in my Google calendar. Works fine except some
people make events like "winter practices" that clutter calendar view. So now I route
some of my calendar imports through this app to change multiday events to singleday.

Live at https://icalendar-modifier.herokuapp.com/

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ pip install -r requirements.txt
$ foreman start web
$ python manage.py runserver
  or
$ python manage.py runserver

```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
$ heroku logs --tail
```

## Documentation

