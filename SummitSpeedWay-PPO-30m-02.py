# Total lap time 02:46.194
# TODO more penalty , More training time, wawpoint and heading
# used in SummitSpeedWay-PPO-172m-02-clone-clone 02:44.333

def reward_function(params):

    # Read input parameters
    all_wheels_on_track =params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = abs(params['steering_angle']) 
    progress = params['progress']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.2 * track_width
    # marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if all_wheels_on_track:
        reward = 1.0
    # Give higher reward if the car is closer to center line and vice versa
        if (distance_from_center <= marker_1) and (steering_angle < 15) :
            reward = 1.0
        elif distance_from_center <= marker_3:
            reward = 0.3
        else:
            reward = 1e-2 # likely crashed/ close to off track
        if steering_angle > 20:
            reward *= 0.3
        if (distance_from_center <= marker_1) and (steering_angle < 15) and (progress> 95):
            reward = 1.0
    else:
        reward = 1e-2


    return float(reward)
