# -*- coding: utf-8 -*-
"""Test the author api routes."""
from unittest.mock import MagicMock, patch

import pytest


# The fixtures from conftest.py will be automatically available
@pytest.mark.usefixtures("db")
class TestAuthorRoutes:
    """Test suite for author routes."""

    @patch("backend.database.db.session")
    def test_get_all_authors(self, mock_db_session, testapp):
        """Test retrieving all authors."""
        mock_author = MagicMock()
        mock_author.id = 1
        mock_author.name = "Mock Author"
        mock_author.info = "Mock Info"

        mock_db_session.scalars().all.return_value = [mock_author]

        response = testapp.get("/authors/")
        assert response.status_code == 200
        assert b"Mock Author" in response.body

    @patch("backend.database.db.session")
    def test_get_author(self, mock_db_session, testapp):
        """Test retrieving a single author by ID."""
        mock_author = MagicMock()
        mock_author.id = 1
        mock_author.name = "Mock Author"
        mock_author.info = "Mock Info"

        mock_db_session.scalars().all.return_value = [mock_author]

        response = testapp.get("/authors/1")
        assert response.status_code == 200
        assert b"Mock Author" in response.body

    @patch("backend.database.db.session")
    def test_create_author(self, mock_db_session, testapp):
        """Test creating a new author."""
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None

        author_data = {"name": "New Author", "info": "Some Info"}
        response = testapp.post_json("/authors/", author_data)
        assert (
            response.status_code == 201
        )  # Changed from 200 to 201 for resource creation

    @patch("backend.database.db.session")
    def test_update_author(self, mock_db_session, testapp):
        """Test updating an existing author."""
        mock_author = MagicMock()
        mock_author.id = 1
        mock_author.name = "Mock Author"

        mock_db_session.scalars().all.return_value = [mock_author]

        author_update_data = {"name": "Updated Author"}
        response = testapp.put_json("/authors/1", author_update_data)
        assert response.status_code == 200

    @patch("backend.database.db.session")
    def test_delete_author(self, mock_db_session, testapp):
        """Test deleting an author by ID."""
        mock_author = MagicMock()
        mock_author.id = 1
        mock_author.name = "Mock Author"

        mock_db_session.scalars().all.return_value = [mock_author]

        response = testapp.delete("/authors/1")
        assert response.status_code == 200
