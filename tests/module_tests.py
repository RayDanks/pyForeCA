def basic_foreca_results_test(basic_multivariate_data):
    """
    In progress.
    Test on the resuts of the overall module.
    "Correct" answers gained from the existing R package.
    """
    foreca = ForeCA( # Defaulting spectrum and entropy control
        n_components = 1,
    )

    results = foreca.run(basic_multivariate_data)

    assert results.omega_forec == [26.81728]
    assert results.omega_original == {
        "variable_1": 12.50753,
        "variable_2": 10.94238 ,
        "variable_3":  16.47975,
        "variable_4": 11.73265,
    }
    assert results.loadings == [
        { # First ForeC coefficients
            "variable_1": 0.523,
            "variable_2": 0.228,
            "variable_3": -1.182,
            "variable_4": -0.187,
        }
    ]
