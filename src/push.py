#!/usr/bin/env python

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('../keys/utep-news-c881f8506849.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://utep-news.firebaseio.com'
})

ref = db.reference('')

posts_ref = ref.child('posts')

posts_ref.push().set({
    'added': int(time.time()),
    'author': 'Tomas Patro',
    'description': 'Eli Greenbaum, Ph.D., an associate professor of biological sciences at The University of Texas at El Paso, is the lead author of a study recently published in the Journal of Natural History that explores a newly discovered natural defense against predation displayed by the Congolese giant toad.',
    'file_hash': '4488a0a6-7392-4cf6-8ee0-ccd7e991cc75',
    'heading': 'UTEP In the Spotlight: Newsweek'
})
