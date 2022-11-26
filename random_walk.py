import numpy as np

sigma = 0.712022


def single_random_walk(step_num):
    # simulate a single random walk and return the value
    # num: number of steps taken

    # compute the steps by normal distribution by step_num times.
    rng = np.random.default_rng()  # a new generator, used to get a new normal distribution.
    steps = rng.normal(0, sigma, step_num)

    cur = 0  # current location, initialized as x_0, which is 0
    x = [cur]  # x_i, i = 0...1000
    for step in steps:
        cur += step
        x.append(cur)

    # compute result
    x_average = sum(x) / 1000
    numerator = 0
    denominator = 0
    for i in range(1, 1001):
        numerator += (x[i] - x_average) * (x[i - 1] - x_average)
        denominator += (x[i] - x_average) ** 2
    return numerator / denominator


def simulate(simulation_num, step_num):
    # simulation_num: number of simulations
    # step_num: number of steps in each simulation
    simulation_res = []
    for _ in range(simulation_num):
        simulation_res.append(single_random_walk(step_num))
    simulation_res.sort(reverse=True)
    return (
        simulation_res[simulation_num * 1 // 100],
        simulation_res[simulation_num * 5 // 100],
        simulation_res[simulation_num * 10 // 100])


if __name__ == '__main__':
    res = simulate(10000, 1000)
    print("1%: {}, 5%: {}, 10%: {}".format(res[0], res[1], res[2]))
