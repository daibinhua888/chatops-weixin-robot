import jenkins


class JenkinsOperator:
    jenkins_server = None

    def connect(self, url, username, password):
        self.jenkins_server = jenkins.Jenkins(url, username=username, password=password)

    def publish2Jenkins(self, taskName):
        self.jenkins_server.build_job(taskName)
        last_build_number = self.jenkins_server.get_job_info(taskName)['lastCompletedBuild']['number']
        return last_build_number

    def getBuildResponse(self, task_name, build_id):
        output = self.jenkins_server.get_build_console_output(task_name, int(build_id))
        return output



