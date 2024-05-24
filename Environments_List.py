###
### This file.py is a collection of all the rooms in Kythera.
### There will be daytime and nighttime flavors of any given room, as appropriate.
### Rooms also refer to areas outside, such as a dirt path surrounded by trees, or a verdant field.

### Test instance for 
roomsDaytime = {
    "shack interior":{
        "roomDescription": "This cramped home is dim - none of the sunlight seems to penetrate the many holes in the walls and ceiling.\nIt is completely silent, save for your breathing.\nThis room is musty and stale, as if it has been holding its breath for years.",
        "room_DC": 7,
        "roomUnseen": "You sense a rotten stench. It is faint, but persistent. Sometimes it fades away, but it returns.",
        "roomUnseen_DC": 9,
        "roomHidden": "You notice that this stench has been following you as you search this room.",
        "roomHidden_DC": 11,
        #Move choices
        "out": "northern shack",
        #Objects in the room
        "objects": [],
    },
    "northern shack": {
        "roomDescription": "You stand before a run-down, single-story shack. The grass is brown and dead in a 10 meter radius around it. A chill wraps around your body here.\nYou can go INto the shack.\nYou can also go south to the verdant fields.",
        "room_DC": 5,
        "roomUnseen": "Past the cracked windows, in the interior of this shack, the darkness seems to shift as if something is moving around inside. But there is nothing there... you can see the furthest inner wall just fine.",
        "roomUnseen_DC": 7,
        "roomUnheard": "The sounds of splintered glass shifting across dirt can be heard from within. Intermingled with it... raspy, irregular breathing, as if someone were in a panic.",
        "roomUnheard_DC": 8,
        "roomHidden": "",
        "roomHidden_DC": 999,
        #Move choices
        "south": "verdant field",
        "s": "verdant field",
        "into shack": "shack interior",
        #Objects in the room
        "objects": [],
    },
    "verdant field": {
        "roomDescription": "A beautiful, verdant field stretches in all directions. The grass reaches past your boots here.\nTo the north, you can see the outline of a dilapidated cottage.",
        "room_DC": 5,
        "roomUnseen": "A sapphire-encrusted brooch rests by an anthill.",
        "roomUnseen_DC": 7,
        "roomHidden": "A mushroom with legs is crouched in the dense grass!",
        "roomHidden_DC": 10,
        #Move choices
        "north": "northern shack",
        "n": "northern shack",
        #Objects in the room
        "objects": [],
    }
}