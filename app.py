"""
Main module to be executed when deployment
"""

from flask import Flask, render_template, request, flash
import backlog
import login


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

app.register_blueprint(backlog.bp)
app.register_blueprint(login.bp)

# Makes url_for('index') == url_for('login.index')
# In another app, you might define a separate main index here with
# app.route, while giving the blog blueprint an url_prefix
app.add_url_rule("/", endpoint="login")
