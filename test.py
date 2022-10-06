import requests

def http_method(sub_url: str, method: str, token: str, data=None):
    if data is None:
        data = dict()

    headers = dict()
    headers['Content-Type'] = "application/json"

    if sub_url == '/start':
        headers['X-Auth-Token'] = token
    else:
        headers['Authorization'] = token

    if method == 'GET':
        response = requests.get(BASE_URL + sub_url, headers=headers)
    elif method == 'POST':
        response = requests.post(BASE_URL + sub_url, headers=headers, json=data)
    elif method == 'PUT':
        response = requests.put(BASE_URL + sub_url, headers=headers, json=data)
    else:
        return {}

    res = {}
    if response.status_code == 200:
        res = response.json()
    else:
        print(f"=== api_{sub_url[1:]} of status_code : {response.status_code} ===")

    return res


def api_start(problem_number, X_Auth_Token) -> dict:
    return http_method('/start', 'POST', X_Auth_Token, {'problem' : problem_number})


def api_waiting_line():
    return http_method('/waiting_line', 'GET', AUTHORIZATION)


def api_game_result():
    return http_method('/game_result', 'GET', AUTHORIZATION)


def api_user_info():
    return http_method('/user_info','GET', AUTHORIZATION)


def api_match(data):
    param = {'pairs' : data}
    return http_method('/match', 'PUT', AUTHORIZATION, param)


def api_change_grade():
    commands = [{ "id": 1, "grade": 1900 }]
    param = commands
    return http_method('/change_grade', 'PUT', AUTHORIZATION, param)


def api_score():
    return http_method('/score', 'GET', AUTHORIZATION)


PROBLEM = {1: {"user_count" : 30, "frequency" : 1},
           2: {"user_count" : 900, "frequency": 45}}

MINSKILL = 1000
MAXSKILL = 100000
SKILL_AVG = 40000
SKILL_STD = 20000
MAXIMUM_MATCHTIME = 15
X_AUTH_TOKEN = '90130fb413144a36f12943d325af397c'
BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
AUTHORIZATION = ""


if __name__ == "__main__":
    response = api_start(1, X_AUTH_TOKEN)
    AUTHORIZATION = response.get('auth_key')
    # print(api_gameresult())
    for i in range(3):
        game_result = api_gameresult()
        print(api_waitingline())
        api_match([])
    # print(api_changegrade())
    # print(api_userinfo())


    # print(api_score())


