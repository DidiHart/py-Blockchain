**Activate the virtual environment**
'''
source venv/Scripts/activate
'''

**Install all packages**
'''
pip install -r requirements.txt
'''

**Run the test**

Make sure to activate virtual environment

'''
python -m pytest backend/tests
'''

**Run the app and API**

Make sure to activate virtual environment

'''
python -m backend.app

'''

**Run a peer instance**

Make sure to activate virtual environment

'''
export PEER=True && python -m backend.app
'''

**Run the frontend**

'''
npm run start
'''

**Seed Backend with data**

Make sure to activate virtual environment

'''
export SEED_DATA=True && python -m backend.app
'''
**Improvement phase-1**

'''
Synchronization is dependent on root node and dependent on an instance of the
app to be running on port 3000
'''
