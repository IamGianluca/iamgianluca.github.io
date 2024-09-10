import arrow
from fasthtml import common as fh

app, rt = fh.fast_app(live=True)


def baby_age():
    present = arrow.utcnow()
    birthday = arrow.get(2024, 3, 25)
    return birthday.humanize(present)


@rt("/")
def home():
    return fh.Titled(
        "Gianluca Rossi",
        fh.Img(src="https://avatars.githubusercontent.com/u/4025968"),
        fh.Div(
            fh.Img(src=""),
            fh.P(
                f"Ciao! My name is Luca and I'm passionate about machine learning and software engineering. I live in Brooklyn with my beautiful wife, our {baby_age()} old daughter, and our dog London."
            ),
        ),
        fh.Div(fh.P()),
        fh.Div(
            fh.H3("Career"),
            fh.Ul(
                fh.Li(
                    fh.A("Tripadvisor", href="https://www.tripadvisor.com/"),
                    " (2023-Present): I lead the AI team, focusing on building AI products to enhance the traveling experience for millions of travelers every month.",
                ),
                fh.Li(
                    fh.A("Ontra", href="https://www.ontra.ai/"),
                    " (2022-2023): I led the AI team, focusing on build safe AI to accelerate legal workflows and automate routine contract negotiations.",
                ),
                fh.Li(
                    fh.A("Farfetch", href="https://www.farfetch.com/"),
                    " (2016-2022): I was one of the founding members of the ML team in London, and later moved to New York to start the US charter. Fo:cused on working on Real-Time Bidding, Recommendation, and predictive modeling.",
                ),
                fh.Li(
                    fh.A("Quantcast", href="https://www.quantcast.com/"),
                    " (2014-2016): I joined Quantcast as part of the Struq acquisition, and continued to work on Real-Time Bidding and Recommendation Systems.",
                ),
                fh.Li(
                    fh.A("Struq", href="https://www.crunchbase.com/organization/struq"),
                    " (2013-2014): I was a Data Scientist and worked on Real-Time Bidding and Personalized Recommendations to serve million of requests/hour with less than 100ms latency.",
                ),
            ),
        ),
        fh.Div(
            fh.H3("Contact Me"),
            fh.P(
                "If you have an offer, opportunity, or introduction that might make my life more interesting, e-mail me at gr.gianlucarossi@gmail.com. For the reason stated above, I'll only respond to those proposals that are a good match for my schedule and interests."
            ),
        ),
    )


fh.serve()
