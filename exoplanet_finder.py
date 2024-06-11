# Basic Libraries: numpy, maytplotlib
import numpy as np
import matplotlib.pyplot as plt

# Lightkruve library aka the main thing that allows us to plot lightcurves
from lightkurve import search_targetpixelfile
from lightkurve import TessTargetPixelFile
import lightkurve as lk

# Something to automate downloading pixel files (optional)
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

# Some more graphing/data organization library(s)
import pandas as pd

# W.I.P trying fit a curve to a lightcurve to find out more information about the potential exoplanet
from astropy.modeling import models, fitting
from astroquery.vizier import Vizier
import scipy.optimize

# Now to define what star we want to look at:
# I use MAST's Tess Input v8.x: https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html

# Target's catalog name; let's look at Tabby's star
tess_target = 'TIC 185336364'
# Search lightkurve's database for our target's photometry data, long cadence b/c I want to see "long term changes"
lk.search_targetpixelfile(target=tess_target, cadence='long')


