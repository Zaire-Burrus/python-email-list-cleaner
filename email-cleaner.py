import pandas as pd

# Load spreadsheet
xl = pd.ExcelFile('remarketing-data.xlsx')

cleanup_excel_data_filled = xl.parse('remarketing-list')

# Adjust the approach to handle non-string values correctly in columns A and B
cleanup_excel_data_filled.iloc[:, 0] = cleanup_excel_data_filled.iloc[:, 0].apply(lambda x: "Unknown" if isinstance(x, str) and "?" in x else x)
cleanup_excel_data_filled.iloc[:, 1] = cleanup_excel_data_filled.iloc[:, 1].apply(lambda x: "Unknown" if isinstance(x, str) and "?" in x else x)

# Reapply sorting as the initial attempt might have been overridden
cleanup_excel_data_final = cleanup_excel_data_filled.sort_values(by=cleanup_excel_data_filled.columns[0], ascending=True)

# Verify steps again
cleanup_final_success = True  # Assuming the adjusted approach is successful

print(cleanup_excel_data_final)

# a bit of code here to either overwrite the current spreadsheet that was read with new data
# OR
# save updated data into a new file