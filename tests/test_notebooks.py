import sys
import papermill as pm
import pytest


@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
        "kernel_name": f"python{sys.version_info.major}",
    }


def test_likelihood_function(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/Likelihood-Function.ipynb", **common_kwargs
    )


def test_error_on_means(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/Error-on-means.ipynb", **common_kwargs
    )


def test_gaussian_sampling(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/Gaussian-Sampling.ipynb", **common_kwargs
    )


def test_normal_dist(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/Gaussian-Distribution.ipynb", **common_kwargs
    )


def test_chi_square_dist(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/Chi-Squared-Distribution.ipynb", **common_kwargs
    )


def test_probability_integral_transform(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/Introductory/probability-integral-transform.ipynb",
        **common_kwargs,
    )


def test_rejection_sampling(common_kwargs):
    pm.execute_notebook(
        "book/notebooks/simulation/Rejection-Sampling-MC.ipynb", **common_kwargs
    )


def test_extended_likelihood(common_kwargs):
    pm.execute_notebook("book/notebooks/HEP/Extended-Likelihood.ipynb", **common_kwargs)
