from app.libs.yellowprint import YellowPrint

yp_token = YellowPrint('rp_token', url_prefix='/token')


@yp_token.route('/get', methods=['POST'])
def get_token():
    # data = request.json
    return 'here\'s your token'