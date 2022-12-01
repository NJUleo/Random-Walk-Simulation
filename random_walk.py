import numpy as np

sigma = 0.4935


# generate the result of a random walk of a cretain step.
def single_random_walk(start_point, step_num):
    # simulate a single random walk and return the value
    # num: number of steps taken

    # compute the steps by normal distribution by step_num times.
    rng = np.random.default_rng()  # a new generator, used to get a new normal distribution.
    steps = rng.normal(0, sigma, step_num)

    cur = start_point  # current location, initialized as x_0, which is 0
    x = [cur]  # x_i, i = 0...1000
    for step in steps:
        cur += step
        x.append(cur)

    # compute result
    return x


def compute_result_2(x):
    numerator = 0
    denominator = 0
    max_res = float('-inf')
    for i in range(len(x) - 1):
        numerator += x[i] * x[i + 1]
        denominator += x[i] ** 2
        cur = numerator / denominator
        max_res = max(max_res, cur)
    return max_res


def compute_result(x):
    x_average = sum(x) / len(x)
    numerator = 0
    denominator = 0
    for i in range(1, len(x)):
        numerator += (x[i] - x_average) * (x[i - 1] - x_average)
        denominator += (x[i] - x_average) ** 2
    return numerator / denominator


# return the top 1%, 5%, 10%
def get_top(x):
    return (
        x[len(x) * 1 // 100],
        x[len(x) * 5 // 100],
        x[len(x) * 10 // 100],
    )


def simulate(simulation_num, start_point, step_num, compute_func):
    # simulation_num: number of simulations
    # step_num: number of steps in each simulation
    simulation_res = []
    for _ in range(simulation_num):
        simulation_res.append(compute_func(single_random_walk(start_point, step_num)))
    simulation_res.sort(reverse=True)
    return (
        simulation_res[simulation_num * 1 // 100],
        simulation_res[simulation_num * 5 // 100],
        simulation_res[simulation_num * 10 // 100])


if __name__ == '__main__':
    res = simulate(100000, 4.849, 384, compute_result_2)
    print("1%: {}, 5%: {}, 10%: {}".format(res[0], res[1], res[2]))
