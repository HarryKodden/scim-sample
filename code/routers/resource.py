# routers/schema.py

from fastapi import APIRouter, HTTPException

from routers import BASE_PATH
from typing import Any
from schema import SCIM_API_MESSAGES, ListResponse, resourceTypes

import logging
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix=BASE_PATH+"/ResourceTypes",
    tags=["SCIM Resource Types"],
)


@router.get("")
async def get_resource_types() -> ListResponse:
    """ Return Resource Types """

    resources = []

    for r in resourceTypes:
        logger.debug(r)
        resources.append(r.dict(by_alias=True))

    return ListResponse(
        Resources=resources,
        itemsPerPage=len(resources),
        schemas=[
            SCIM_API_MESSAGES+":ListResponse"
        ],
        startIndex=1,
        totalResults=len(resources)
    )


@router.get("/{id}")
async def get_resource(id: str) -> Any:
    """ Return Resource Type """

    for resource in resourceTypes:
        if resource.id == id:
            return resource.dict(by_alias=True)

    raise HTTPException(status_code=404, detail=f"Resource {id} not found")
