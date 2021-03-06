import numpy as np

# observation analysis
for a in range(0):
    logs_dir = '../Data-13/results/'
    ob_ls = np.load(logs_dir + '{}'.format('ob_ls') + '.npy')
    ob_ls = np.squeeze(ob_ls)
    ob_mean = np.mean(ob_ls, axis=0)
    ob_std = np.std(ob_ls, axis=0)
    ob_max = np.max(ob_ls, axis=0)
    ob_min = np.min(ob_ls, axis=0)
    print("")

    obs_mean = np.array([4.83868269e+01, 9.26671424e+01, 6.41770269e+02, -3.11372911e+02,
                         6.78844516e-02, 1.27067008e-02, 1.46767778e+02])
    obs_std = np.array([9.87342636e+00, 1.13743122e+02, 1.30954515e+02, 3.87827102e+02,
                        5.11422102e-02, 6.47789938e-02, 2.07343922e+02])

    ob_test = ob_ls[110:120, :]
    obs_normalized = (ob_test - obs_mean) / obs_std

# reward original analysis
for a in range(0):
    logs_dir = '../Data-13/results/'
    reward = np.load(logs_dir + '{}'.format('reward_np') + '.npy')
    reward_mean = np.mean(reward, axis=0)
    reward_std = np.std(reward, axis=0)

    r_mean = -6707.54
    r_std = 7314.15
    r = reward / r_std
    reward_sum = np.sum(reward)  # -25595967.36
    r_sum = np.sum(r)  # r_sum = -3499.51
    print("")


# reward random action analysis
for a in range(0):
    logs_dir = '../Data-13/results/'
    reward = np.load(logs_dir + '{}'.format('reward_ls') + '.npy')
    reward_mean = np.mean(reward, axis=0)
    reward_std = np.std(reward, axis=0)

    r_mean = -6755.76
    r_std = 7331.19
    r = reward / r_std
    reward_sum = np.sum(reward)  # -25779975.89
    r_sum = np.sum(r)  # r_sum = -3524
    print("")


# speed tracking analysis
for a in range(1):
    logs_dir = '../Data-13/results/'
    v_mph = np.load(logs_dir + '{}'.format('v_mph_ls') + '.npy')
    target_speed = np.load(logs_dir + '{}'.format('target_speed_ls') + '.npy')
    spd_err = target_speed - v_mph
    print("")