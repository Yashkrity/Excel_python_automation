import os
from data_cleaning import clean_sales_data
from report_gen import calculate_kpis
from email_report import send_email_report


RAW_DATA_FOLDER = "../data/raw/"
PROCESSED_DATA_FOLDER = "../data/processed/"
REPORTS_FOLDER = "../data/reports/"

def process_files():
    for file in os.listdir(RAW_DATA_FOLDER):
        if file.endswith(".xlsx") or file.endswith(".csv"):
            file_path = os.path.join(RAW_DATA_FOLDER, file)
            print(f"Processing {file}...")

            # cleaning data
            cleaned_df = clean_sales_data(file_path)
            output_path = os.path.join(PROCESSED_DATA_FOLDER, f"cleaned_{file.split('.')[0]}.xlsx")
            cleaned_df.to_excel(output_path, index=False)
            print(f"File saved after cleaning : {output_path}")

            # generating KPIs
            kpis = calculate_kpis(cleaned_df)
            print(f"KPIs: {kpis}")

            # saving KPIs to report generated
            report_path = os.path.join(REPORTS_FOLDER, f"report_{file.split('.')[0]}.txt")
            with open(report_path, "w") as f:
                for key, value in kpis.items():
                    f.write(f"{key}: {value}\n")
            print(f"Saved KPI report to {report_path}")

            #email
            #send_email_report("email_id", "password", "recipient_email_id", "Daily Sales Report", str(kpis))

if __name__ == "__main__":
    process_files()
    print("Data cleaned, KPIs calculated and reporting completed, sent over mail.")
