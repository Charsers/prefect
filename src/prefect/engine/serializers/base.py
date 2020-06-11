import json
from typing import Any, Union

import cloudpickle


class Serializer:
    """
    Serializers are used by Results to handle the transformation of
    Python objects to and from bytes.
    """

    def __eq__(self, other: Any) -> bool:
        return type(self) == type(other)

    def serialize(self, value: Any) -> bytes:
        """
        Serialize an object to bytes.

        Args:
            - value (Any): the value to serialize

        Returns:
            - bytes: the serialized value
        """
        return cloudpickle.dumps(value)

    def deserialize(self, value: Union[bytes, str]) -> Any:
        """
        Deserialize an object from bytes.

        Args:
            - value (Union[bytes, str]): the value to deserialize

        Returns:
            - Any: the deserialized value
        """
        return cloudpickle.loads(value)


class JSONSerializer(Serializer):
    """
    JSONSerializers serialize objects to and from JSON
    """

    def serialize(self, value: Any) -> bytes:
        """
        Serialize an object to JSON

        Args:
            - value (Any): the value to serialize

        Returns:
            - bytes: the serialized value
        """
        return json.dumps(value).encode()

    def deserialize(self, value: Union[bytes, str]) -> Any:
        """
        Deserialize an object from JSON

        Args:
            - value (Union[bytes, str]): the value to deserialize

        Returns:
            - Any: the deserialized value
        """
        return json.loads(value)