from flask import Flask
from flask import render_template
from utils import jenkinsUtil
from utils import robot

app = Flask(__name__)


@app.route('/task/<string:task_name>/<string:build_id>/')
def task_detail(task_name, build_id):
    return render_template("buildDetail.html", output=jenkinsUtil.getBuildResponse(task_name, int(build_id)))


robot._web_port = 8989
robot._web_dns = 'mckay.lab'
robot._monitor_group_name = 'SIT发布群'

robot.startWeChatrobot()


app.run(port = robot._web_port)