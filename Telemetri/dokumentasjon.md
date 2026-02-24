# Data formatering -> data pakker 
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

Skal returnere:
test Packet 1 is valid: v=1 id='drone1' action='takeoff' data={'altitude': 10} tag='abc123'
validate_packet->Error validating packet: 1 validation error for Packet
id
  Field required [type=missing, input_value={'action': 'takeoff', 'da...': 10}, 'tag': 'abc123'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
Packet 2 is invalid

# Request manager
    Alle serverside request funksjoner skal være her for seperasjon og strukturens skyld. 

# Network manager
    Nettverks relater kode her

# Server manager
    Driver serveren og kontroller bruk av moduler

# Utils
    støtte/hjelpe funksjoner

    