import json
import os

# Load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Generate HTML for attributes
def generate_attributes_html(attributes):
    html = "<h2>Attributes</h2>\n<ul>\n"
    for attribute in attributes:
        html += f"<li>{attribute['name']}: {attribute['value']}</li>\n"
    html += "</ul>\n"
    return html

# Generate HTML for tables
def generate_tables_html(tables):
    html = ""
    for table in tables:
        html += f"<h2>{table['title']}</h2>\n"
        html += "<table>\n<thead>\n<tr>\n"
        for column in table['columns']:
            html += f"<th>{column['header']}</th>\n"
        html += "</tr>\n</thead>\n<tbody>\n"

        rows = zip(*[column['values'] for column in table['columns']])
        for row in rows:
            html += "<tr>\n"
            for cell in row:
                html += f"<td>{cell}</td>\n"
            html += "</tr>\n"

        html += "</tbody>\n</table>\n"
    return html

# Generate HTML for plot groups
def generate_plotgroups_html(plotGroups):
    html = ""
    for plotGroup in plotGroups:
        html += f"<h2>{plotGroup['title']}</h2>\n"
        for plot in plotGroup['plots']:
            if plot['title'] == None or plot['title'] == plotGroup['title']:
                html += f"<img src='{plot['image']}' alt='{plot['caption']}' />\n"
            else:
                html += f"<h3>{plot['title']}</h3>" #these titels eithe dont exixt or repeat the previous title
                html += f"<img src='{plot['image']}' alt='{plot['caption']}' />\n"
    return html

# Main function to generate HTML report
def generate_html_report(json_data):
    title = json_data.get('title', 'Report')
    attributes = json_data.get('attributes', [])
    tables = json_data.get('tables', [])
    plotGroups = json_data.get('plotGroups', [])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                font-size: 2rem; /* Use rem for scalability */
                max-width: 100vw; /* Ensure body doesn't exceed viewport width */
            }}
            h1 {{
                color: #333;
                font-size: 3rem; /* Use rem for scalability */
            }}
            h2 {{
                font-size: 2.8rem;
            }}
            h3 {{
                font-size: 2.6rem;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                font-size: 0.8rem;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
                word-wrap: break-word; /* Allow text to wrap within cells */
            }}
            th {{
                background-color: #f4f4f4;
            }}
            img {{
                max-width: 100%;
                height: auto;
                max-height: 100vh; /* Ensure the image doesn't overflow the viewport height */
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
    """

    if attributes:
        html_content += generate_attributes_html(attributes)

    if tables:
        html_content += generate_tables_html(tables)

    if plotGroups:
        html_content += generate_plotgroups_html(plotGroups)

    html_content += """
    </body>
    </html>
    """

    return html_content

# Save HTML to a file
def save_html(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# Main execution
if __name__ == "__main__":
    folder_path = 'c:\\Users\\Anja\\OneDrive - Cranfield University\\Documents\\Bioinformatics_MSc\\Thesis\\Results\\PB_custom_pipeline\\NEM_hifi_reports'  # change to folder path 
    for filename in os.listdir(folder_path):
        if filename.endswith('report.json'):
            json_filepath = os.path.join(folder_path, filename)
            json_data = load_json(json_filepath)
            html_report = generate_html_report(json_data)
            html_filename = os.path.splitext(filename)[0] + '.html'
            html_filepath = os.path.join(folder_path, html_filename)
            save_html(html_filepath, html_report)
            print(f"HTML report saved to {html_filepath}")
