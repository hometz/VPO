def generate_html_table(rows):
    step = 255 // (rows - 1)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gradient Table</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #000;
                padding: 8px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <table>
    """

    for i in range(rows):
        color_value = 255 - (i * step)
        color = f"rgb({color_value}, {color_value}, {color_value})"
        html_content += f'<tr style="background-color: {color};"><td>Row {i + 1}</td></tr>\n'

    html_content += """
        </table>
    </body>
    </html>
    """

    with open("gradient_table.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    generate_html_table(rows)
