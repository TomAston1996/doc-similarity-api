'''
Module to register middleware
Author: Tom Aston
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


def register_middleware(app: FastAPI) -> None:
    """
    Register middleware
    """
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add TrustedHostMiddleware
    # This middleware checks the Host header of the request against a list of allowed hosts.
    # * At the moment trusted hosts are set to just localhost
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])
