# Copyright 2024 Scaleway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import cirq

from typing import Union, Optional

from .scaleway_session import ScalewaySession
from .scaleway_client import QaaSClient


class ScalewayDevice(cirq.devices.Device):
    def __init__(
        self,
        client: QaaSClient,
        id: str,
        name: str,
        version: str,
        num_qubits: int,
        metadata: Optional[str],
    ) -> None:
        self.__id = id
        self.__client = client
        self.__version = version
        self.__num_qubits = num_qubits
        self.__name = name
        self.__metadata = metadata

    def __repr__(self) -> str:
        return f"<ScalewayDevice(name={self.__name},num_qubits={self.__num_qubits},platform_id={self.id})>"

    @property
    def id(self) -> str:
        """The unique identifier of the platform.

        Returns:
            str: The UUID of the platform.
        """
        return self.__id

    @property
    def availability(self) -> str:
        """Returns the current status of the platform.

        Returns:
            str: the current availability statys of the session. Can be either: available, shortage or scarce
        """
        resp = self.__client.get_platform(self.__id)

        return resp.get("availability")

    @property
    def name(self) -> str:
        """Name of the platform.

        Returns:
            str: the name of the platform.
        """
        return self.__name

    @property
    def num_qubits(self) -> int:
        """Estimated maximum number of qubit handle of the platform.
        Estimation is done by using Quantum Volume benchmark.

        Returns:
            int: the estimated amount of maximum number of runnable qubits.
        """
        return self.__num_qubits

    @property
    def version(self):
        """Version of the platform

        Returns:
            str: the platform's version.
        """
        return self.__version

    def create_session(
        self,
        name: Optional[str] = "qsim-session-from-cirq",
        deduplication_id: Optional[str] = "qsim-session-from-cirq",
        max_duration: Union[int, str] = "1h",
        max_idle_duration: Union[int, str] = "20m",
    ) -> ScalewaySession:
        """Create a new device session to run job against.

        Args:
            name (str): name of the session. Used only for convenient purpose.
            deduplication_id (str): an identifier you can use to clearly identify a session.
                The deduplication_id allows to retrieve a same session and to share it among people
            max_duration (str, int): the maximum duration before the session is automatically killed.
                Can be either a string like 1h, 20m15s or an int representing seconds
            max_idle_duration (str, int): the maximum duration without job before the session is automatically killed.
                Can be either a string like 1h, 20m15s or an int representing seconds
        Returns:
            ScalewaySession: a new QPU session that can be started/stopped once
        """
        return ScalewaySession(
            client=self.__client,
            device=self,
            name=name,
            deduplication_id=deduplication_id,
            max_duration=max_duration,
            max_idle_duration=max_idle_duration,
        )
