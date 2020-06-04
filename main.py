# coding: utf-8
from workflow import Workflow, web, ICON_WEB
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')


def main(wf):
    timestamp = int(sys.argv[1])
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    wf.add_item(title=dt,
                subtitle=u"测试副标题",
                valid=True,
                icon=ICON_WEB,
                arg=dt)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
