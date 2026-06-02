import csv

class PatientQuery:
    def __init__(self, data, stats):
        self.data = data
        self.stats = stats

    def smokers_with_hypertension(self):
        ages = [
            p["age"] for p in self.data
            if p["smoking_status"] in ["formerly smoked", "smokes"]
               and p["hypertension"] == 1
        ]

        if len(ages) == 0:
            return "No smokers with hypertension found."

        return self.stats.descriptive_stats(
            [{"age": a} for a in ages], "age"
        )

    def heart_disease_patients(self):
        ages=[p["age"] for p in self.data if p["heart_disease"]==1]
        glucose=[p["avg_glucose_level"] for p in self.data if p["heart_disease"]==1]
        return {
            "Age Stats": self.stats.descriptive_stats([{"age":x} for x in ages],"age"),
            "Average Glucose": sum(glucose)/len(glucose)
        }

    def export_csv(self, records, filename):
        keys=records[0].keys()
        with open(filename,'w',newline='') as f:
            writer=csv.DictWriter(f,keys)
            writer.writeheader()
            writer.writerows(records)
