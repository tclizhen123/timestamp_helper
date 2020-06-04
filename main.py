# coding: utf-8
from workflow import Workflow, web, ICON_WEB
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def main(wf):
    wf.add_item(title=sys.argv[1],
                subtitle=u"测试副标题",
                valid=True,
                icon=ICON_WEB)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
