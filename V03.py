# Same as SummitSpeedWay-PPO-30m-02.py But Control Speed
# Used In RogueCircuit-PPO-60m-V03-01
def reward_function(params):

    # Read input parameters
    all_wheels_on_track =params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = abs(params['steering_angle']) 
    progress = params['progress']
    speed = params['speed']
    speed_threshold = 3

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.2 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if all_wheels_on_track:
        reward = 5.0
        if speed > speed_threshold:
            reward = 5.0
        else:
            reward = reward*0.75 

    # Give higher reward if the car is closer to center line and vice versa
        if (distance_from_center <= marker_1) and (steering_angle < 15) :
            reward = reward*1.9
            if speed > speed_threshold:
                reward = reward*1.5
            else:
                reward = reward*0.8 
        elif distance_from_center <= marker_2:
            reward = reward*1.4
        elif distance_from_center <= marker_3:
            reward = reward*1.1
        else:
            reward = 1e-2 # likely crashed/ close to off track
        if steering_angle > 20:
            reward *= 0.3
        if (distance_from_center <= marker_1) and (steering_angle < 15) and (progress> 95):
            if speed > speed_threshold:
                reward = reward*1.9
            else:
                reward = reward*0.7          
    else:
        reward = 1e-2


    return float(reward)
