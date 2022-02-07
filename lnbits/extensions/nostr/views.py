from http import HTTPStatus

from fastapi import Request
from fastapi.param_functions import Query
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.responses import HTMLResponse

from lnbits.core.crud import update_payment_status
from lnbits.core.models import User
from lnbits.core.views.api import api_payment
from lnbits.decorators import check_user_exists

from . import nostr_ext, nostr_renderer

templates = Jinja2Templates(directory="templates")


@nostr_ext.get("/", response_class=HTMLResponse)
async def index(request: Request, user: User = Depends(check_user_exists)):
    return nostr_renderer().TemplateResponse(
        "nostr/index.html", {"request": request, "user": user.dict()}
    )
