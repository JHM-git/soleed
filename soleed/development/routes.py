from flask import Flask, render_template, url_for, request, redirect, g
from soleed import db
from soleed.development import bp
from soleed.helpers.hardData import schoolx, opinionsx, picturesx
from soleed.helpers.functions import oneRandomOpinion, twoRandomOpinions, schoolFundingLists
from soleed.helpers.keys import googleAPI
from flask_babel import _, get_locale


@bp.before_request
def before_request():
  g.locale = str(get_locale())


@bp.route('/schools/example')
def example_school():
  return render_template('school-example.html', googleAPI=googleAPI)


@bp.route('/schools/inProgress')
def schooldev():
  generalOpinionOne, generalOpinionTwo = twoRandomOpinions(opinionsx['opinions'], opinionsx['index_finders']['general'])
  return render_template('school-dev.html', school=schoolx, opinions=opinionsx, 
  pictures=picturesx, generalOpinionOne=generalOpinionOne, generalOpinionTwo=generalOpinionTwo,
  oneRandomOpinion=oneRandomOpinion, googleAPI=googleAPI)
