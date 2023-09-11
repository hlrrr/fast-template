from fastapi    import APIRouter

user = APIRouter()

@user.get()
def get():
    pass


@user.post()
def post():
    pass


@user.put()
def put():
    pass