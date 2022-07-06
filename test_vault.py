from Password_vault import decrypt
import pytest

def test_decrypt():
    assert type(decrypt(b'qG3o2lV-nlJyKdQhdwrA-luHI7dQVX-Hbj0ovMvyuek=')) == type({})

pytest.main(["-v", "--tb=line", "-rN", __file__])