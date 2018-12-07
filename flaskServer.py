from flask import Flask
from flask import render_template
from utils import jenkinsUtil
from utils import robot
from utils import textparser
from utils import configloader

config = configloader.load_config("configs/jenkins-config.json")
textparser.sysNameMap = configloader.load_config("configs/sysNameMap.json")
textparser.envMap = configloader.load_config("configs/envMap.json")


app = Flask(__name__)


@app.route('/task/<string:task_name>/<string:build_id>/')
def task_detail(task_name, build_id):
    return render_template("buildDetail.html", title='{}-{}'.format(task_name, build_id), output=jenkins_server.getBuildResponse(task_name, int(build_id)))


jenkins_server = jenkinsUtil.JenkinsOperator()
jenkins_server.connect(config.get("jenkins_url"), config.get("jenkins_username"), config.get("jenkins_password"))

wx_robot = robot.ChatOpsRobot()
wx_robot.init(jenkins_server, config.get("web_url"), config.get("web_port"), config.get("monitoring_wx_chat_group_name"))

wx_robot.startWeChatrobot()


app.run(port=config.get("web_port"))
