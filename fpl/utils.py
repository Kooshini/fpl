def team_converter(team_id):
    """Converts a team's ID to their actual name."""
    team_map = {
        1: "Arsenal",
        2: "Bournemouth",
        3: "Brighton",
        4: "Burnley",
        5: "Cardiff",
        6: "Chelsea",
        7: "Crystal Palace",
        8: "Everton",
        9: "Fulham",
        10: "Huddersfield",
        11: "Leicester",
        12: "Liverpool",
        13: "Man City",
        14: "Man Utd",
        15: "Newcastle",
        16: "Southampton",
        17: "Spurs",
        18: "Watford",
        19: "West Ham",
        20: "Wolves"
    }
    return team_map[team_id] 


def position_converter(position):
    """Converts a player's `element_type` to their actual position."""
    if position == 1:
        return "Goalkeeper"
    elif position == 2:
        return "Defender"
    elif position == 3:
        return "Midfielder"
    else:
        return "Forward"
