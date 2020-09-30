import jinja2
import os
from core import app

print('Init startpage')

my_loader = jinja2.ChoiceLoader(
    [app.jinja_loader,
     jinja2.FileSystemLoader([os.path.abspath(os.path.dirname(__file__)) + '/templates'])]
)
app.jinja_loader = my_loader
