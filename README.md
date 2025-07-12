# World GDP Choropleth Map Visualization

A professional Python application for visualizing the Gross Domestic Product (GDP) of countries worldwide using an interactive choropleth map powered by Plotly.

---

## Overview

This project enables users to explore global GDP data interactively. Each country is color-coded according to its GDP, making it easy to compare economic output across regions. The visualization is generated using Plotly and Pandas, and the data is sourced from the CIA World Factbook (2014).

---

## Features

- **Interactive Choropleth Map:** Visualizes GDP data for each country.
- **Hover Tooltips:** Displays country names and GDP values.
- **Customizable Visualization:** Easily change color scales, projections, and annotations.
- **Robust Error Handling:** Informs users of data loading issues.
- **Clean Code Structure:** Modular functions and clear documentation.

---

## Technologies Used

- [Python 3](https://www.python.org/)
- [Plotly](https://plotly.com/python/) (for visualization)
- [Pandas](https://pandas.pydata.org/) (for data manipulation)

---

## Installation

1. **Clone or Download the Repository**

2. **Install Required Packages**

    ```sh
    pip install plotly pandas
    ```

---

## Usage

1. **Run the Application**

    ```sh
    python app.py
    ```

2. The choropleth map will open in your default web browser or a window.

---

## Data Source

- **Dataset:** [2014 World GDP with Codes (Plotly)](https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv)
- **Original Source:** [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html)

---

## Customization

- **Update Data:** To use a newer dataset, change the `DATA_URL` in `app.py` and ensure the column names match your new data.
- **Change Visualization:** Modify the `create_choropleth` function to adjust color scales, map projection, or annotations.
- **Error Handling:** The script will notify you if the data fails to load or columns are missing.

---

## File Structure

- `app.py` — Main script for loading data and generating the choropleth map.

---

## Example Output

![Example Choropleth Map](https://raw.githubusercontent.com/plotly/datasets/master/images/gdp_choropleth_example.png)

---

## Author

Developed by **Ganesh**.

---

## License

This project is for educational and visualization purposes. Please check the data source for any restrictions on data usage.

---

## Contact

If you have any questions or need help with the visualization, feel free to reach out to me at [email](mailto:roy862452@gmail.com) and I'll be happy to help. You can also open an issue on GitHub or submit a pull request if you'd like to contribute to the project. Alternatively, you can message me on [WhatsApp](https://wa.me/8249873663).
