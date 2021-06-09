#Params for everything except 100 and 200 free

distance_norm = 2
bonuses = [6, 5, 4, 3, 2, 1]
constant_boost = 63
team_boost = 8
distance_cap = 4
place_cap = 9
non_finalist = 3
mult_cap = 30

def score_event(results, guess):
    score = constant_boost
    
    # Deductions and Place Bonus
    for athlete in guess: 
        multiplier = (mult_cap - guess.index(athlete))/mult_cap
        bonus = 0
        real_distance = abs((guess.index(athlete) - results.index(athlete)))
        capped_distance = max(abs((guess.index(athlete) - place_cap)), distance_cap)
        distance = min(real_distance, capped_distance)
        penalty = int(math.ceil(distance**distance_norm * multiplier))
        if distance == 0:
            bonus = bonuses[guess.index(athlete)]
        score += (bonus - penalty)
        if results.index(athlete) > 7:
            score -= non_finalist
        
    # Olympic berth bonus (this is pretty much just to help with swaps)
    for athlete in guess[0:2]:
        if athlete in results[0:2]:
            score += team_boost
    
    return score


#Params for 100 and 200 free

distance_norm_r = 1.5
bonuses_r = [6, 5, 4, 3, 2, 1]
constant_boost_r = 71
team_boost_r = 4
distance_cap_r = 5
place_cap_r = 9
non_relay = 25
mult_cap_r = 60

def score_event_relay(results, guess):
    score = constant_boost_r
    
    # Deductions and Place Bonus
    for athlete in guess: 
        multiplier = (mult_cap_r - guess.index(athlete))/mult_cap_r
        bonus = 0
        real_distance = abs((guess.index(athlete) - results.index(athlete)))
        capped_distance = max(abs((guess.index(athlete) - place_cap_r)), distance_cap_r)
        distance = min(real_distance, capped_distance)
        penalty = int(math.ceil(distance**distance_norm_r * multiplier))
        if distance == 0:
            bonus = bonuses_r[guess.index(athlete)]
        score += (bonus - penalty)
        if results.index(athlete) > 5:
            score -= non_relay
        
    # Olympic berth bonus (this is pretty much just to help with swaps)
    for athlete in guess[0:2]:
        if athlete in results[0:2]:
            score += team_boost_r
    
    return score
