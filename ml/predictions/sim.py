
# This module has logic for simulating an investment over x years


def investment_simulator(years, investment, roi):
    sim = [investment]
    for year in range(years):
        new_value = sim[-1] * (1 + roi)
        sim.append(new_value)
    return sim
