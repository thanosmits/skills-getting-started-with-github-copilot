import pytest
from httpx import AsyncClient
from fastapi import status
from src.app import app

import asyncio

@pytest.mark.asyncio
async def test_root_redirect():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/")
    # Assert
    assert response.status_code in (status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT)

@pytest.mark.asyncio
async def test_static_files_served():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/static/index.html")
    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert "<html" in response.text
