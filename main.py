from datetime import datetime

import arrow
from fasthtml import common as fh

app, rt = fh.fast_app(live=True)


def get_ginny_age():
    present = arrow.utcnow()
    ginny_bday = arrow.get(2024, 3, 25)
    return ginny_bday.humanize(present)


def current_time():
    now = datetime.now()
    date_string = now.strftime("%m/%d/%Y")
    time_string = now.strftime("%H:%M")
    return date_string, time_string


@rt("/")
def get():
    date, time = current_time()
    return fh.Titled(
        "Personal website",
        fh.Div(
            fh.P(
                "Ciao, and welcome to my website. My name is Luca and I'm passionate about machine learning and software engineering."
            )
        ),
        fh.Div(
            fh.P(
                f"I live in Brooklyn with my beautiful wife, our {get_ginny_age()} old daughter, and our dog London."
            )
        ),
        fh.Div(fh.P(f"FYI, today is {date} and time {time}.")),
        fh.P(fh.A("Link", href="/change")),
    )


@rt("/change")
def get():
    return fh.Titled(
        "About me",
        fh.Div(fh.P("Ciao Brig!")),
        fh.Ul(
            fh.Li("Ciao"),
            fh.Li("Hello"),
            fh.Li("Hola"),
        ),
        fh.P(fh.A("Home", href="/")),
    )


fh.serve()
