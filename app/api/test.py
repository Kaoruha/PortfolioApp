from app.libs.yellowprint import YellowPrint

yp_test = YellowPrint('rp_user', url_prefix='/test')


@yp_test.route('/table')
def table_generation():
    return 'table'


@yp_test.route('/table1')
def table_generation1():
    return 'table1'


from app.authorization.token_auth import login_required



@yp_test.route('/token')
# @login_required
def t_get_token():
    from app.authorization.token_auth import creat_token, verify_token
    s = creat_token('1')
    a = verify_token(s)
    print(s)
    print(a)
    return a
