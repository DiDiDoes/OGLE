import os
import logging
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from utils import prompt


logger = logging.getLogger("OGLE")
var_names = ["I", "V", "V_I", "P_1", "T0_1", "A_1"]


def load_data(filename):
    # load original data (dirty)
    logger.info(prompt("BEGIN: load data"))
    data_path = os.path.join("data", filename)
    logger.info(f"Loading data from {data_path}...")
    data = pd.read_table(data_path, skiprows=6, usecols=range(11))
    n_data = data.shape[0]
    logger.info(f"{n_data} datapoint loaded.")
    logger.info("Type summary:\n" + str(pd.value_counts(data["Type"])))

    # clean data
    logger.info(prompt("BEGIN: clean data"))
    data_clean = data
    for var in var_names:
        row_dirty = data_clean[var] == -99.99
        n_dirty = row_dirty.sum()
        logger.info(f"{n_dirty} data cleaned for {var}.")
        data_clean = data_clean[~row_dirty]

    # clean large values in P_1
    row_dirty = data_clean["P_1"] > 999
    n_dirty = row_dirty.sum()
    logger.info(f"{n_dirty} datapoint cleaned for P_1.")
    data_clean = data_clean[~row_dirty]

    # clean large values in T0_1
    row_dirty = data_clean["T0_1"] > 99999
    n_dirty = row_dirty.sum()
    logger.info(f"{n_dirty} datapoint cleaned for T0_1.")
    data_clean = data_clean[~row_dirty]

    logger.info("Type summary:\n" + str(pd.value_counts(data_clean["Type"])))
    logger.info(prompt("END: clean data"))

    n_data = data_clean.shape[0]
    logger.info(f"{n_data} datapoint remain.")
    logger.info("Summary of variables:\n" + str(data_clean.describe()))
    logger.info(prompt("END: load data"))
    return data_clean


def violin(data):
    ymins = [None, None, None, -1, None, None]
    ymaxs = [None, None, None, 20, None, None]

    logger.info(prompt("BEGIN: violin plot"))
    for var, ymin, ymax in zip(var_names, ymins, ymaxs):
        logger.info(f"Making violin plot of {var} variable...")
        plt.figure(figsize=(12, 9))
        sns.violinplot(data=data, x="Type", y=var)
        if ymin is not None:
            plt.ylim(ymin, ymax)
        save_path = os.path.join("figures", f"violin_{var}.jpg")
        plt.savefig(save_path)
        logger.info(f"Saved to {save_path}.")
    logger.info(prompt("END: violin plot"))
