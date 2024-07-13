# Player Data ETL Application

## Overview

This ETL (Extract, Transform, Load) application processes player data and stores it in an AWS S3 bucket in Parquet format. The data is organized by continent, and the application supports incremental updates and parallel processing.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.8 or higher
- Apache Spark
- `boto3` library
- `pandas` library
- `pyspark` library

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/player-data-etl.git
   cd player-data-etl


## Execution
Run the ETL Process
python src/etl.py
