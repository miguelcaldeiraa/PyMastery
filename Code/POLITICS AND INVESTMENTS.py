parties = ["PS", "PSD", "BE", "PCP", "L", "PAN", "IL", "CH"]
rois = [0.02, 0.03, 0.005, 0.0005, 0.02, 0.01, 0.05, 0.1]
investment = 1000

sims = [[investment] for party in parties ]

for year in range(8):
    for i, party in enumerate(parties):
        party_roi = rois[i]
        new_value = sims[i][-1] * (1 + party_roi)
        sims[i].append(new_value)

sims