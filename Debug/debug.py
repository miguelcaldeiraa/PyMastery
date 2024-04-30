from mypackage.stats import averages

data_fn = "data.csv"
avs = averages(data_fn)
print(f"Averages\t")
for col, av in avs.items():
    print(f"{col}\t{av :.2f}")