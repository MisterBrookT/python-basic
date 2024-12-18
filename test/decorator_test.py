from decorator.dataclass import DecodingConfig
import pytest

def test_decoding_config_valid_backend():
    config = DecodingConfig(guided_decoding_backend='outlines')
    # to use the data in dataclass, just use the initialized object as a normal object
    assert config.guided_decoding_backend == 'outlines'

def test_decoding_config_invalid_backend():
    with pytest.raises(ValueError) as excinfo:
        DecodingConfig(guided_decoding_backend='invalid_backend')
    assert "Invalid guided_decoding_backend" in str(excinfo.value)
