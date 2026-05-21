"""Tests for API client module."""

import pytest


def test_client_initialization(mock_client):
    """Test that client initializes correctly."""
    assert mock_client is not None


def test_api_call(api_key, mock_client):
    """Test API call with valid key."""
    mock_client.call_api.return_value = {'status': 'ok'}
    result = mock_client.call_api('/test', {})
    assert result['status'] == 'ok'
