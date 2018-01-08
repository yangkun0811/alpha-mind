# -*- coding: utf-8 -*-
"""
Created on 2017-8-16

@author: cheng.li
"""

from alphamind.data.engines.sqlengine import SqlEngine
from alphamind.analysis.factoranalysis import factor_analysis
from alphamind.analysis.factoranalysis import er_portfolio_analysis
from alphamind.analysis.quantileanalysis import quantile_analysis
from alphamind.analysis.quantileanalysis import er_quantile_analysis
from alphamind.data.engines.universe import Universe
from alphamind.data.processing import factor_processing

from alphamind.portfolio.constraints import Constraints
from alphamind.portfolio.evolver import evolve_positions

from alphamind.data.engines.sqlengine import risk_styles
from alphamind.data.engines.sqlengine import industry_styles
from alphamind.data.engines.sqlengine import macro_styles
from alphamind.data.winsorize import winsorize_normal
from alphamind.data.standardize import standardize
from alphamind.data.standardize import projection
from alphamind.data.neutralize import neutralize
from alphamind.data.engines.sqlengine import factor_tables

from alphamind.model import LinearRegression
from alphamind.model import LassoRegression
from alphamind.model import ConstLinearModel
from alphamind.model import LogisticRegression
from alphamind.model import RandomForestRegressor
from alphamind.model import XGBRegressor
from alphamind.model import XGBClassifier
from alphamind.model import load_model
from alphamind.model.data_preparing import fetch_data_package
from alphamind.model.data_preparing import fetch_train_phase

from alphamind.execution.naiveexecutor import NaiveExecutor
from alphamind.execution.thresholdexecutor import ThresholdExecutor
from alphamind.execution.targetvolexecutor import TargetVolExecutor
from alphamind.execution.pipeline import ExecutionPipeline

from alphamind.utilities import alpha_logger
from alphamind.utilities import map_freq


__all__ = [
    'SqlEngine',
    'factor_analysis',
    'er_portfolio_analysis',
    'quantile_analysis',
    'er_quantile_analysis',
    'Universe',
    'factor_processing',
    'Constraints',
    'evolve_positions',
    'risk_styles',
    'industry_styles',
    'macro_styles',
    'winsorize_normal',
    'standardize',
    'projection',
    'neutralize',
    'factor_tables',
    'fetch_data_package',
    'fetch_train_phase',
    'LinearRegression',
    'LassoRegression',
    'ConstLinearModel',
    'LogisticRegression',
    'RandomForestRegressor',
    'XGBRegressor',
    'XGBClassifier',
    'load_model',
    'NaiveExecutor',
    'ThresholdExecutor',
    'TargetVolExecutor',
    'ExecutionPipeline',
    'alpha_logger',
    'map_freq'
]