import pandas as pd
from pathlib import Path
from xlsxtpl.writerx import BookWriter


def get_payloads(df):
    # payload items are specified in a dict
    info = {}

    # add any static data needed for the sheet
    info.update(
        {
            'sheet_name': 'people',
        }
    )

    # add the DataFrame to the payload
    info['df'] = df

    # payload is returned as a list of dict
    return [info]


# Assume we have a pandas dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 18, 42],
    'Country': ['UK', 'USA', 'France', 'Germany']
})


# Creating a BookWriter instance using a template
writer = BookWriter(fname='template.xlsx')

# get the payload
payloads = get_payloads(df)

# render the workbook
writer.render_book(payloads=payloads)

# write output Excel file
file_name = f'my_output.xlsx'
report_path = Path(file_name)
writer.save(report_path)


