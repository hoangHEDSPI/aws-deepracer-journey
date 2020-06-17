def reward_function(params):
    import math
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    is_left_of_center = params['is_left_of_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    distance_from_border = (0.5*track_width) -distance_from_center
    if all_wheels_on_track and  distance_from_border >= 0.15:
        reward = 1.0
    else:
        reward = 1e-3

    # Punish heavily if not all_wheels_on_track
    if not all_wheels_on_track:
        reward *= -1

    return float(reward)
