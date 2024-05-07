from pathlib import Path
import numpy as np
import pandas as pd
import rasterio

country = "chn"


def pop(pop, cov: str, mastergrid: str, watermask: str, output_dir: str, log=True):
    covariates_output = Path(output_dir) / 'covariates'
    covariates_output.mkdir(parents=True, exist_ok=True)
    zonal_output = Path(output_dir) / 'zonal'
    zonal_output.mkdir(parents=True, exist_ok=True)
    tmp_output = Path(output_dir) / 'tmp'
    tmp_output.mkdir(parents=True, exist_ok=True)

    # calculate zonal stats
    census_data = pd.DataFrame(columns=['ADMINID', 'ADMINPOP'])
    pop_table = pd.DataFrame(columns=['ADMINID', 'ADMINPOP'])

    zonal_path = mastergrid
    zonal_raster = rasterio.open(zonal_path)
    for cvr in cov:
        if cvr in ['watermask', 'mastergrid']:
            continue

    # popfit
    popfit_output = tmp_output / ('init_popfit' + country + ".data")
