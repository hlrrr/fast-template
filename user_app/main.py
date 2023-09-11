from fastapi    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware

from starlette_admin.contrib.sqla.admin import Admin
from starlette_admin.contrib.sqla.view  import ModelView

from .endpoints     import user
# from .configs     import origins

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(  
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},       # shrink schema section
    # title="ChimichangApp",
    # description=description,
    # summary="Deadpool's favorite app. Nuff said.",
    # version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    # contact={
    #     "name": "Deadpoolio the Amazing",
    #     "url": "http://x-force.example.com/contact/",
    #     "email": "dp@x-force.example.com",
    #     },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    #     },
    # openapi_tags=tags_metadata,
)      

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 리퀘스트는 정의한 미들웨어들을 역순으로 타고 들어옴.

app.include_router(user)

'''
for database
'''


'''
for starlette_admin
'''

# admin = Admin(engine)
# # admin.add_view(ModelView(m.User))
# admin.mount_to(app)

@app.get(path="/")
async def root():
    pass

