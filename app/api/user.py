from app.libs.yellowprint import YellowPrint
from app.validators.forms import ClientForm
from app.models.user import User
from app.libs.error_code import ParameterException
from app.libs.error import NoException
from app.authorization.token_auth import creat_token

yp_user = YellowPrint('rp_user', url_prefix='/user')


@yp_user.route('/register', methods=['POST'])
def user_register():
    # data = request.json
    # account = data['account']
    # secret = data['secret']

    # 1、request.data 会自动传入ClientForm
    form = ClientForm()
    # 2、对ClientForm对实例进行校验
    if form.validate():
        # 3.1、查询用户名是否已经存在
        if User.query.filter_by(account=form.account.data).first():
            # 4、如果用户名存在返回报错601
            return ParameterException(error_code=601, msg='用户名已经存在')
        else:
            # 5、若用户名不存在，尝试注册用户
            User.add_user(account=form.account.data,
                          secret=form.secret.data)
            return NoException(msg='注册成功')

    else:
        # 若form不满足校验规则，返回报错600，后续可以细化
        return ParameterException()


@yp_user.route('/login', methods=['POST'])
def user_login():
    # data = request.json
    # account = data['account']
    # secret = data['secret']

    # 1、request.data 会自动传入ClientForm
    form = ClientForm()
    # 2、对ClientForm对实例进行校验
    if form.validate():
        account = form.account.data
        password = form.secret.data
        try:
            user = User.is_password_right(account=account, password=password)
            if user:
                token = creat_token(user.id)
                return NoException(data=token)
        except Exception:
            raise ParameterException(msg="登录失败", error_code=602)

    else:
        # 若form不满足校验规则，返回报错600，后续可以细化
        raise ParameterException()
