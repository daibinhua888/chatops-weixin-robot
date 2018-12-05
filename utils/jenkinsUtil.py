import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='mckay', password='111111')

def publish2Jenkins(taskName):
    server.build_job(taskName)
    last_build_number = server.get_job_info(taskName)['lastCompletedBuild']['number']
    return last_build_number

def getBuildResponse(task_name, build_id):
    output = server.get_build_console_output(task_name, int(build_id))
    return output



