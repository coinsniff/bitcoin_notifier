import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import time
from getAlerts import getActiveEmailAlerts

alerts = getActiveEmailAlerts(190, 'coinbase')
print alerts
print int(time.time())
