import jieba


def getEnvNames():
    return list(envMap.keys())


def getSysNames():
    return list(sysNameMap.keys())


def display(tags):
    for i in tags:
        print(i)

def containsWord(tags, wantedWords):
    for i in tags:
        if i in wantedWords:
            return True
    return False

def isPublishApplication(tags):
    #必须包含  发布  单词
    #必须不包含 日志 单词
    if containsWord(tags, ['发布', '发下']) and not containsWord(tags, '日志') and not containsWord(tags, '？'):
        return True
    return False


def isGetPublishApplicationStatus(tags):
    if not containsWord(tags, '日志') and containsWord(tags, ['发','发布','发好','起来']):
        return True
    return False


def isLogRequest(tags):
    if containsWord(tags, '日志') and containsWord(tags, ['拿','看下','发']):
        return True
    return False


def parseChatType(tags):
    '''
    发布系统
    查发布状态
    要日志
    '''
    if isPublishApplication(tags):
        return 'PubApp';
    if isGetPublishApplicationStatus(tags):
        return 'GetPubAppStatus';
    if isLogRequest(tags):
        return 'GetLog';
    return 'UNKNOW'

def getAppName(words):
    for word in words:
        if word.lower() in getSysNames():
            return sysNameMap[word]
    return '未知系统'


def getEnv(words):
    for word in words:
        if word.lower() in getEnvNames():
            return envMap[word]
    return '未知环境'

def parse(sentence):
    result = list(jieba.cut(sentence))
    commandType = parseChatType(result)
    if commandType == 'PubApp':
        appName=getAppName(result)
        env=getEnv(result)
    print('{}-->{}/{} in {}({})'.format(sentence, commandType, appName, env, result))
    return {
                "command": commandType,
                "sentence": sentence,
                "appName": appName,
                "env": env,
                "tokens": result,
            }






'''
帮忙发布下sso
帮忙看下sso日志
sso是不是挂了
sso是不是挂了？
'''
#
# result=jieba.cut("运生，帮忙发布下SSO")
# print('===='.join(result))
# result=jieba.cut("帮忙看下sso日志")
# print('===='.join(result))
# result=jieba.cut("帮忙看下kxtx-sso日志")
# print('===='.join(result))
# result=jieba.cut("sso是不是挂了")
# print('===='.join(result))
# result=jieba.cut("sso是不是挂了？")
# print('===='.join(result))


# def test(sentence):
#     result = list(jieba.cut(sentence))
#     print('{}--->{}({})'.format(sentence, parseChatType(result), result))
#
#
# print('==================发布类型=========================')
# test('运生，发下SSO')
# test('你好，发下SSO')
# test('发下SSO')
# test('运生，发布下SSO')
# test('请发布下mship系统，测试已经通过了')
#
#
#
# print('==================要日志类型=========================')
# test('运生，帮忙看下SSO的日志')
# test('SSO是不是挂了，把日志发我下')
# test('sso没起来，发我下日志')
#
# print('==================询问发布状态=========================')
# test('sso发布好了吗？')
# test('SSO发好了吗')
# test('sso起来了吗？')
#
#
# jieba.add_word('test环境')
# print('===============解析==================')
# parse('运生，发下SSO,测试环境')
# parse('运生，发下SSO,test环境')
# parse('运生，test环境发下SSO')
# parse('SSO发下test环境')
# parse('SSO发下，test环境里')
# a=parse('SSO发下，test下')
# print(a["command"])
# print(a["env"])