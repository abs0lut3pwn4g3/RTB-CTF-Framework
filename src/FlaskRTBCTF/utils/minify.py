from flask_minify import minify

static_minify = minify(html=True, js=True, cssless=True, caching_limit=0)
