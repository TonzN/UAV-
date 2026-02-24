from typing import Any, Literal
from pydantic import BaseModel, Field    # v2
from typing import Callable, Any
from dataclasses import dataclass
import json

"""Schema for the server module 
   This module contains the data classes and models used in the server module.
   It includes the Packet class, which is used to represent packets of data sent
   between the server and clients
"""
# Packet og Return packet er like men separert idh at de ikke nødvendigvis vil være like, og for å unngå forvirring.


@dataclass
class Task: # For threading brukes Task class for enklere håndtering av funksjoner og deres resultater
    func: Callable[..., Any]
    args: tuple
    kwargs: dict
    result: Any = None
    error: Exception | None = None
    status: str = "pending"

class Packet(BaseModel): #standarisert packe format for å verifisere data som sendes fra klient til server
    """Packet schema for server communication.
    \n version: 1
    \n id: Unique identifier for the drone.
    \n action: The action to be performed.
    \n data: The data to be sent.
    \n tag: A tag for the packet.
    \n date: The date the packet was created.
    """
    v: Literal[1] = Field(default=1, description="Version of the packet")
    id: str = Field(..., description="Unique identifier for the drone")
    action: str = Field(..., description="Action to be performed")
    data: Any = Field(..., description="Data to be sent")
    tag: str | None = Field(None, description="Tag for internal filtering")
    date: str | None = Field(None, description="Date the packet was created")

class ResponsePacket(BaseModel): #standarisert packe format som skal benyttes for data som sendes fra server til klienter
    """Response packet schema for server to client communication.
    \n version: 1
    \n id: Unique identifier for the drone.
    \n action: The action that was performed.
    \n data: The data to be sent, 0: data, 1: tag
    \n tag: A tag for the packet.
    \n date: The date the packet was created.
    """
    v: Literal[1] = Field(default=1, description="Version of the packet")
    id: str = Field(..., description="Unique identifier for the drone")
    action: str = Field(..., description="Action to be performed")
    data: Any = Field(..., description="Data to be sent")
    tag: str | None = Field(None, description="Tag for internal filtering")
    date: str | None = Field(None, description="Date the packet was created")

def validate_packet(data, packet_type) -> Packet:
    try:
        return packet_type(**json.loads(data.strip()))
    except Exception as e:
        print(f"validate_packet->Error validating packet: {e}")
        return False
    
#Example usage:
test_packet = {"id": "drone1", "action": "takeoff", "data": {"altitude": 10}, "tag": "abc123"}
test_packet2 = {"action": "takeoff", "data": {"altitude": 10}, "tag": "abc123"} # Missing id field, should be invalid

validated_packet = validate_packet(json.dumps(test_packet), Packet)
if validated_packet:
    print("test Packet 1 is valid:", validated_packet)
else:    
    print("Packet is invalid")

validated_packet2 = validate_packet(json.dumps(test_packet2), Packet)
if validated_packet2:
    print("test Packet 2 is valid:", validated_packet2)
else:    
    print("Packet 2 is invalid")