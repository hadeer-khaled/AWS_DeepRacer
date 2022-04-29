# Total lap time 02:48.063

def reward_function(params):

    # Read input parameters
    all_wheels_on_track =params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering_angle = abs(params['steering_angle']) 
    progress = params['progress']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if all_wheels_on_track:
    # Give higher reward if the car is closer to center line and vice versa
        if (distance_from_center <= marker_1) and (steering_angle < 15) :
            reward = 1.0
            speed = 5 
        elif distance_from_center <= marker_2:
            reward = 0.5
        elif distance_from_center <= marker_3:
            reward = 0.1
            speed*=0.3
        else:
            reward = 1e-3 # likely crashed/ close to off track
        if (distance_from_center <= marker_1) and (steering_angle < 15) and (progress> 95):
            reward = 1.0
            speed = 5
    else:
        reward = 1e-2


    return float(reward)
