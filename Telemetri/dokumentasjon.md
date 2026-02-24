# Data formatering -> data pakker 
Generer pakker med return packet schema klassen
Pakker kan lages manuelt som dictionary med dette skal unngås i utgangspunktet 
Packet klassen er en klasse som benyttes for å verifisere pakker fra klienten

#Example usage:

    test_packet = ResponsePacket(id="drone1", action="takeoff", data={"altitude": 10}, tag="abc123", date="2024-06-01T12:00:00Z") # Valid packet, formatert som ResponsePacket
    test_packet2 = {"v": 1, "action": "land", "data": {"altitude": 0}, "tag": "def456", "date": "2024-06-01T12:05:00Z"} # Missing 'id' field, should be invalids
    test_packet3 = {"v": 1, "id": "drone2", "action": "hover", "data": {"altitude": 5}, "tag": "ghi789", "date": "2024-06-01T12:10:00Z"} # Valid packet, formatert som dict

    validated_packet = validate_packet(test_packet, ResponsePacket)
    if validated_packet:
        print(f"\n Validated packet: {validated_packet}")

    validated_packet2 = validate_packet(json.dumps(test_packet2), ResponsePacket)
    if validated_packet2:
        print(f"\n Validated packet: {validated_packet2}")

    validated_packet3 = validate_packet(test_packet3, Packet)
    if validated_packet3:
        print(f"\n Validated packet: {validated_packet3}")

Skal returnere:
     Validated packet: v=1 id='drone1' action='takeoff' data={'altitude': 10} tag='abc123' date='2024-06-01T12:00:00Z'

    validate_packet->Error validating packet: 1 validation error for ResponsePacket
    id
    Field required [type=missing, input_value={'v': 1, 'action': 'land'... '2024-06-01T12:05:00Z'}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.11/v/missing

    Validated packet: v=1 id='drone2' action='hover' data={'altitude': 5} tag='ghi789' date='2024-06-01T12:10:00Z'

# Request manager
    Alle serverside request funksjoner skal være her for seperasjon og strukturens skyld. 

# Network manager
    Nettverks relater kode her

# Server manager
    Driver serveren og kontroller bruk av moduler

# Utils
    støtte/hjelpe funksjoner

    