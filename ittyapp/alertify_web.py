import json # Yes, we're using this instead of a DB. I know.
import itty3 # Should be installed already, as indicated by requirements.txt, https://itty3.readthedocs.io
# import alertify (previously was import bitscripter) This is how we'll reference the functions of the main scripting logic, such as it is
import os # This is to show filenames and shit like that.

bsapp = itty3.App() # Object creation function for itty3

url_prefix_alertify = '/alertify' # Michael adding alertify randomly

@bsapp.get(url_prefix_alertify + '/')
def index_alertify(request):
    with open('alertify_index.html') as alertify_index_file:
        template = alertify_index_file.read()
    return bsapp.render(request, template)

# This just makes sure that we can still import this as
# a library or run it standalone.
if __name__ == "__main__":

    # -------- Logging Setup -------- #
    # We're going to use the logger from
    # the bsapp object, which it has because
    # the itty3 class creates a logger upon
    # instantiation.
    LOGGER = bsapp.get_log()
    LOGGER.setLevel('INFO')
    LOGGER.info(os.path.basename(__file__))
    # -------- End Logging Setup ---- #

    # This runs the app. This won't be run if
    # web_app gets imported.
    bsapp.run(addr="0.0.0.0",
        port=8000,
        debug=None,
        static_url_path=None,
        static_root=None
    )
