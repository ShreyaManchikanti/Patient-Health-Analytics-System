import csv

class PatientDataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        try:
            patient_data = []

            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                # Normalize headers
                reader.fieldnames = [
                    h.strip().lower().replace(" ", "_")
                    for h in reader.fieldnames
                ]

                for row in reader:
                    record = {
                        "id": row["id"],
                        "age": int(row["age"]),
                        "gender": row["gender"],
                        "hypertension": int(row["hypertension"]),
                        "heart_disease": int(row["heart_disease"]),
                        "residence_type": row["residence_type"],
                        "smoking_status": row["smoking_status"],
                        "physical_activity": row["physical_activity"],
                        "bmi": float(row["bmi"]),
                        "avg_glucose_level": float(row["average_glucose_level"]),
                        "sleep_hours": float(row["sleep_hours"]),
                        "dietary_habits": row["dietary_habits"],
                        "stroke_risk": float(row["stroke_risk_score"]),
                        "region": row["region"],
                        "stroke": int(row["stroke_occurrence"])
                    }

                    patient_data.append(record)

            return patient_data

        except FileNotFoundError:
            raise Exception("data.csv file not found.")
        except ValueError:
            raise Exception("Invalid numeric value in dataset.")
        except KeyError as e:
            raise Exception(f"Missing column in dataset: {e}")
        except Exception as e:
            raise Exception(f"Error loading dataset: {e}")
