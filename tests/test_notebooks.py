import sys
import papermill as pm


def test_notebooks_all_execute(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    common_kwargs = {
        "output_path": str(outputnb),
        "kernel_name": "python{}".format(sys.version_info.major),
    }

    pm.execute_notebook(
        "book/notebooks/Introductory/Chi-Squared-Distribution.ipynb", **common_kwargs
    )
    pm.execute_notebook(
        "book/notebooks/Introductory/Error-on-means.ipynb", **common_kwargs
    )
    pm.execute_notebook(
        "book/notebooks/Introductory/Gaussian-Distribution.ipynb", **common_kwargs
    )
    pm.execute_notebook(
        "book/notebooks/Introductory/Gaussian-Sampling.ipynb", **common_kwargs
    )
    pm.execute_notebook(
        "book/notebooks/Introductory/Likelihood-Function.ipynb", **common_kwargs
    )
    pm.execute_notebook(
        "book/notebooks/Introductory/probability-integral-transform.ipynb",
        **common_kwargs
    )

    pm.execute_notebook(
        "Notebooks/Likelihood_Methods/Extended-Likelihood.ipynb", **common_kwargs
    )

    pm.execute_notebook(
        "Notebooks/Sampling/Rejection-Sampling-MC.ipynb", **common_kwargs
    )
