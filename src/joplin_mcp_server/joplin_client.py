"""
joplin_client.py
A client for interacting with the Joplin API.

This module provides a simple asynchronous client to interact with the Joplin API.
"""

from typing import Any, Literal

import httpx


class JoplinClient:
    """
    A client for interacting with the Joplin API.
    """

    def __init__(
        self, base_url: str = "http://localhost:41184", token: str = ""
    ) -> None:
        self.base_url: str = base_url.rstrip("/")
        self.token: str = token

    def _url(self, path: str) -> str:
        sep: Literal["&", "?"] = "&" if "?" in path else "?"
        return f"{self.base_url}{path}{sep}token={self.token}"

    async def get_folders(self) -> dict[str, Any]:
        """
        Fetches the list of folders from the Joplin API.

        Returns:
            dict[str, Any]: A dictionary containing the folders.
        """

        async with httpx.AsyncClient() as client:
            resp: httpx.Response = await client.get(url=self._url(path="/folders"))
            resp.raise_for_status()
            return resp.json()
