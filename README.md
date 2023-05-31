# Frida Fooddata CLI

A command-line interface to query records from DTU's publically available Frida Fooddata dataset (https://frida.fooddata.dk/).

## Technologies

- **simple-term-menu** for creating a simple, interactive menu in the terminal
- **pandas** for reading, preparing, transforming and writing data

## Installation

1. Clone the project into your directory and change director to the project directory:

```
git clone https://github.com/cph-mf287/Frida-Fooddata-CLI.git
```
```
cd Frida-Fooddata-CLI
```

2. Install dependencies

```
pip3 install simple-term-menu
```
```
pip3 install pandas
```

## User guide

1. Run the program

```
python3 cli.py
```

2. Navigation

- Either use the arrow keys followed by the enter key to select a menu item, or use the designated hotkey (if one is defined).
- The escape key can be used to go back in the menu tree, or to quit the program entirely.

3. The menu

- **Language** (Frida Fooddata supports Danish and English, and so does the CLI)
- **Food entries**
  - Search food by name
  - Search food by group
  - Search food by nutritional value
- **Data categories**
  - Search food groups by name
  - Search parameter groups by name
  - Search parameters by group name

## Status

### What has been done

- An interactive menu has been created
- Data has been imported (read) from multiple CSV files for different occasions
- Data has been categorised (prepared) and queried
- Data has been calculated (transformed)
- Data has been exported (written) to new CSV files

### What has not been done

- Recommendation algorithms

## Challenges

- Working solo on an ambitious project
- Time
- Covering more than a couple of fields in data science alone
