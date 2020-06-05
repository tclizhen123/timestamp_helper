# coding: utf-8
from workflow import Workflow, web, ICON_WEB
import sys
import time
import pyperclip
reload(sys)
sys.setdefaultencoding('utf8')


def main(wf):
    if len(sys.argv) == 1:
        timestampStr = str(pyperclip.paste())
        timestamp = float(pyperclip.paste())
    else:
        timestamp = sys.argv[1]
        timestampStr = str(sys.argv[1])

    
    if len(timestampStr) > 10:
        timestamp = float(timestamp) / 1000.0

    time_local = time.localtime(float(timestamp))
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    wf.add_item(title=dt,
                subtitle=timestampStr,
                valid=True,
                icon=ICON_WEB,
                arg=dt)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
