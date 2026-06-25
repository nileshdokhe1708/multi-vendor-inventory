from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    ItemNotFoundException,
    VendorNotFoundException,
    VendorItemMappingException
)

async def item_not_found_handler(
        request: Request,
        exc: ItemNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        }
    )

async def vendor_not_found_handler(
        request: Request,
        exc: VendorNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        }
    )

async def vendor_mapping_handler(
        request: Request,
        exc: VendorItemMappingException
):

    return JSONResponse(
        status_code=400,
        content={
            "message": str(exc)
        }
    )


