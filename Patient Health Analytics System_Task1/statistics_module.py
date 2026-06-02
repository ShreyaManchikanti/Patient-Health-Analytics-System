import math
from collections import Counter

class StatisticsCalculator:

    def mean(self, values):
        return sum(values) / len(values)

    def median(self, values):
        values.sort()
        mid = len(values)//2
        return values[mid] if len(values)%2!=0 else (values[mid-1]+values[mid])/2

    def mode(self, values):
        return Counter(values).most_common(1)[0][0]

    def variance(self, values):
        m = self.mean(values)
        return sum((x-m)**2 for x in values)/len(values)

    def std_dev(self, values):
        return math.sqrt(self.variance(values))

    def data_range(self, values):
        return max(values)-min(values)

    def descriptive_stats(self, data, feature):
        if len(data) == 0:
            return "No records found for this query."

        vals = [p[feature] for p in data]

        return {
            "Mean": self.mean(vals),
            "Median": self.median(vals),
            "Mode": self.mode(vals),
            "Min": min(vals),
            "Max": max(vals),
            "Variance": self.variance(vals),
            "StdDev": self.std_dev(vals),
            "Range": self.data_range(vals)
        }

