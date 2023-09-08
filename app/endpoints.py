from fastapi    import APIRouter

rtr = APIRouter()

@rtr.get()
def get():
    pass


@rtr.post()
def post():
    pass


@rtr.put()
def put():
    pass