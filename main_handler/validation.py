from datetime import datetime, timezone


READ_VALID_ARGS = ['pod','sDateTime','eDateTime']
WRITE_VALID_ARGA = ['pod_id','msg']
TODAY = datetime.now(timezone.utc)
eDateTime = TODAY
sDateTime = eDateTime - datetime(24)
retDict = {}
SDATETIME = 'sDateTime'
EDATETIME = 'eDateTime'
FAILURE_STATUS = 'Failure'
POD_ID = "pod_id"
MSG = "msg"
def readValidation(args):
    if  SDATETIME not in READ_VALID_ARGS or EDATETIME not in READ_VALID_ARGS:
        return FAILURE_STATUS,""


def writevalidation(args):
    if POD_ID not in WRITE_VALID_ARGA or MSG not in WRITE_VALID_ARGA:
        return FAILURE_STATUS,""
    