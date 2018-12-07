import itchat
from utils import textparser


class ChatOpsRobot:
    _web_port = 0
    _web_dns = 'localhost'
    _monitor_group_name = ''
    _operator = None


    def init(self, operator, host, port, group_name):
        self._operator = operator
        self._web_dns = host
        self._web_port = port
        self._monitor_group_name = group_name

    def startWeChatrobot(self):
        itchat.auto_login()
        itchat.run(blockThread=False)

        @itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
        def text_reply(msg):
            if msg.User.NickName != self._monitor_group_name:
                return

            print('发言者:', msg.ActualNickName)
            print('内容:', msg.Content)
            print(msg)

            cmd = textparser.parse(msg.Content)

            cmdType = cmd["command"]

            if cmdType == 'PubApp':
                appName = cmd["appName"]
                env = cmd["env"]
                taskName = '{}-{}'.format(appName, env)
                buildNumber = self._operator.publish2Jenkins(taskName)

                msg = 'http://{}:{}/task/{}/{}/'.format(self._web_dns, self._web_port, taskName, buildNumber)
                print(msg)
                msg = '已提交Jenkins构建，请稍等。点击以下url查看构建详情：\n{}'.format(msg)

                msg = '命令类型：{}\n应用：{}\n环境：{}\n构建编号：{}\n机器人回复：{}'.format(cmdType, appName, env, buildNumber, msg)

                rooms = itchat.search_chatrooms(self._monitor_group_name)
                monitor_group = rooms[0]
                monitor_group.send(msg)

