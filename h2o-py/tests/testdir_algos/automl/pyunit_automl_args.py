from __future__ import print_function
import sys, os
sys.path.insert(1, os.path.join("..","..",".."))
import h2o
from tests import pyunit_utils
from h2o.automl import H2OAutoML

"""
This test is used to check arguments passed into H2OAutoML along with different ways of using `.train()`
"""
def prostate_automl_args():

    df = h2o.import_file(path=pyunit_utils.locate("smalldata/logreg/prostate.csv"))

    #Split frames
    fr = df.split_frame(ratios=[.8,.1])

    #Set up train, validation, and test sets
    train = fr[0]
    valid = fr[1]
    test = fr[2]

    train["CAPSULE"] = train["CAPSULE"].asfactor()
    valid["CAPSULE"] = valid["CAPSULE"].asfactor()
    test["CAPSULE"] = test["CAPSULE"].asfactor()
    
    max_models = 2
    
    # Below fails bc there are no models in the leaderboard, but AutoML needs to check the models to get the
    # model type (binomial, multinomial, or regression)
    # print("Check that exclude_algos implementation is complete, and empty leaderboard works")
    # aml = H2OAutoML(max_runtime_secs=30, project_name="py_aml0", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234, exclude_algos=["GLM", "DRF", "GBM", "DeepLearning", "StackedEnsemble"])
    # aml.train(y="CAPSULE", training_frame=train)
    # print("Check leaderboard to ensure that it only has a header")
    # print(aml.leaderboard)
    # assert aml.leaderboard.nrows == 0, "with all algos excluded, leaderboard is not empty"

    print("Check arguments to H2OAutoML class")
    aml = H2OAutoML(project_name="py_aml0", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234, exclude_algos=["DeepLearning"])
    aml.train(y="CAPSULE", training_frame=train)
    assert aml.project_name == "py_aml0", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)    

    print("AutoML run with x not provided and train set only")
    aml = H2OAutoML(project_name="py_aml1", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y="CAPSULE", training_frame=train)
    assert aml.project_name == "py_aml1", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)    

    print("AutoML run with x not provided with train and valid")
    aml = H2OAutoML(project_name="py_aml2", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y="CAPSULE", training_frame=train, validation_frame=valid)
    assert aml.project_name == "py_aml2", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)    

    print("AutoML run with x not provided with train and test")
    aml = H2OAutoML(project_name="py_aml3", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y="CAPSULE", training_frame=train, leaderboard_frame=test)
    assert aml.project_name == "py_aml3", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)    

    print("AutoML run with x not provided with train, valid, and test")
    aml = H2OAutoML(project_name="py_aml4", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y="CAPSULE", training_frame=train, validation_frame=valid, leaderboard_frame=test)
    assert aml.project_name == "py_aml4", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)    

    print("AutoML run with x not provided and y as col idx with train, valid, and test")
    aml = H2OAutoML(project_name="py_aml5", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y=1, training_frame=train, validation_frame=valid, leaderboard_frame=test)
    assert aml.project_name == "py_aml5", "Project name is not set"
    assert aml.stopping_rounds == 3, "stopping_rounds is not set to 3"
    assert aml.stopping_tolerence == 0.001, "stopping_tolerance is not set to 0.001"
    assert aml.stopping_metric == "AUC", "stopping_metrics is not set to `AUC`"
    assert aml.max_models == 2, "max_models is not set to 2"
    assert aml.seed == 1234, "seed is not set to `1234`"
    print("Check leaderboard")
    print(aml.leaderboard)

    print("Check predict, leader, and leaderboard")
    print("AutoML run with x not provided and train set only")
    aml = H2OAutoML(project_name="py_aml6", stopping_rounds=3, stopping_tolerance=0.001, stopping_metric="AUC", max_models=max_models, seed=1234)
    aml.train(y="CAPSULE", training_frame=train)
    print("Check leaderboard")
    print(aml.leaderboard)
    print("Check predictions")
    print(aml.predict(train))

    # TO DO: Clean up amodel creation below, should grep to get the DRF like we do in the runit
    print("Check nfolds is passed through to base models")
    train = h2o.import_file(path=pyunit_utils.locate("smalldata/logreg/prostate.csv"))
    train["CAPSULE"] = train["CAPSULE"].asfactor()
    aml = H2OAutoML(project_name="py_aml_nfolds3", nfolds=3, max_models=3, seed=1)
    aml.train(y="CAPSULE", training_frame=train)
    # grab the last model in the leaderboard, hoping that it's not an SE model
    amodel = h2o.get_model(aml.leaderboard[aml.leaderboard.nrows-1,0])
    # if you get a stacked ensemble, take the second to last 
    # right now, if the last is SE, then second to last must be non-SE, but when we add multiple SEs, this will need to be updated
    if type(amodel) == h2o.estimators.stackedensemble.H2OStackedEnsembleEstimator:
      amodel = h2o.get_model(aml.leaderboard[aml.leaderboard.nrows-2,0])
    assert amodel.params['nfolds']['actual'] == 3

    print("Check nfolds = 0 works properly")
    train = h2o.import_file(path=pyunit_utils.locate("smalldata/logreg/prostate.csv"))
    train["CAPSULE"] = train["CAPSULE"].asfactor()
    aml = H2OAutoML(project_name="py_aml_nfolds0", nfolds=0, max_models=3, seed=1)
    aml.train(y="CAPSULE", training_frame=train)
    # grab the last model in the leaderboard (which should not be an SE model) and verify that nfolds = 0
    # we assume that if one model correctly used nfolds = 0, then they all do, but we could add an extra check for this
    amodel = h2o.get_model(aml.leaderboard[aml.leaderboard.nrows-1,0])
    assert type(amodel) is not h2o.estimators.stackedensemble.H2OStackedEnsembleEstimator
    assert amodel.params['nfolds']['actual'] == 0


    print("Check balance_classes & related args work properly")
    train = h2o.import_file(path=pyunit_utils.locate("smalldata/logreg/prostate.csv"))
    train["CAPSULE"] = train["CAPSULE"].asfactor()
    aml = H2OAutoML(project_name="py_aml_balance_classes_etc", max_models=3, 
        balance_classes=True, class_sampling_factors=[0.2, 1.4], max_after_balance_size=3.0, seed=1)
    aml.train(y="CAPSULE", training_frame=train)
    # grab the last model in the leaderboard, hoping that it's not an SE model
    amodel = h2o.get_model(aml.leaderboard[aml.leaderboard.nrows-1,0])
    # if you get a stacked ensemble, take the second to last 
    # right now, if the last is SE, then second to last must be non-SE, but when we add multiple SEs, this will need to be updated
    if type(amodel) == h2o.estimators.stackedensemble.H2OStackedEnsembleEstimator:
      amodel = h2o.get_model(aml.leaderboard[aml.leaderboard.nrows-2,0])   
    assert amodel.params['balance_classes']['actual'] == True
    assert amodel.params['max_after_balance_size']['actual'] == 3.0
    assert amodel.params['class_sampling_factors']['actual'] == [0.2, 1.4]


    # TO DO
    # Add a test that checks fold_column like in runit



if __name__ == "__main__":
    pyunit_utils.standalone_test(prostate_automl_args)
else:
    prostate_automl_args()
