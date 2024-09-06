from fasthtml import common as fh
from datetime import datetime

app, rt = fh.fast_app(live=True)

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
    fh.Div(fh.P("Ciao, and welcome to my website. My name is Luca and I'm passionate about machine learning and software engineering.")),
    fh.Div(fh.P("I live in Brooklyn with my beautiful wife, our 5-month old daughter, and our dog London.")),
    fh.Div(fh.P(f"FYI, today is {date} and time {time}.")),
    fh.P(fh.A("Link", href="/change"))

)

@rt("/change")
def get(): 
    return fh.Titled(
       "About me", 
            fh.Div(fh.P("Ciao Brig!")),
            fh.P(fh.A("Home", href="/"))
    )                 

fh.serve()
