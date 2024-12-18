from dataclasses import dataclass


@dataclass
class DecodingConfig:
    """Dataclass which contains the decoding strategy of the engine"""
    # I use the example in source code of vllm to demonstrate the usage of dataclass. 
    # The reason to use data class: 1) when you have a bunch of variables that you want to group together. 
    # 2) avoid the boilerplate code of __init__ and __repr__. 3) clearly point out the role of the class as data container.
    # 4) many other reasons like immutability, etc.
    # also note that the __post_init__ is a special method that is called after the instance has been created, 
    # which allows for further initializaion or validation logic after the built-in __init__ method.

    # Which guided decoding algo to use.
    # 'outlines' / 'lm-format-enforcer' / 'xgrammar'
    guided_decoding_backend: str = 'xgrammar'

    def __post_init__(self):
        valid_guided_backends = ['outlines', 'lm-format-enforcer', 'xgrammar']
        backend = self.guided_decoding_backend
        if backend not in valid_guided_backends:
            raise ValueError(f"Invalid guided_decoding_backend '{backend},"
                             f"must be one of {valid_guided_backends}")