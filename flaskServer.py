from flask import Flask
from flask import render_template
from utils import jenkinsUtil
from utils import robot

app = Flask(__name__)


@app.route('/task/<string:task_name>/<string:build_id>/')
def task_detail(task_name, build_id):
    return render_template("buildDetail.html", output=jenkins_server.getBuildResponse(task_name, int(build_id)))


jenkins_server = jenkinsUtil.JenkinsOperator()
jenkins_server.connect('http://localhost:8080', 'mckay', '111111')

wx_robot = robot.ChatOpsRobot()
wx_robot.init(jenkins_server, 'mckay.lab', 8989, 'SIT发布群')

wx_robot.startWeChatrobot()


app.run(port=wx_robot.getPort())
