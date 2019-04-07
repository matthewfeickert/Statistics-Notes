import sys
import papermill as pm


def test_notebooks_all_execute(tmpdir):
    outputnb = tmpdir.join('output.ipynb')
    common_kwargs = {
        'output_path': str(outputnb),
        'kernel_name': 'python{}'.format(sys.version_info.major)
    }

    pm.execute_notebook(
        'Notebooks/Introductory/Chi-Squared-Distribution.ipynb', **common_kwargs)
    pm.execute_notebook(
        'Notebooks/Introductory/Error-on-means.ipynb', **common_kwargs)
    pm.execute_notebook(
        'Notebooks/Introductory/Gaussian-Distribution.ipynb', **common_kwargs)
    pm.execute_notebook(
        'Notebooks/Introductory/Gaussian-Sampling.ipynb', **common_kwargs)
    pm.execute_notebook(
        'Notebooks/Introductory/Likelihood-Function.ipynb', **common_kwargs)
    pm.execute_notebook(
        'Notebooks/Introductory/probability-integral-transform.ipynb', **common_kwargs)

    pm.execute_notebook(
        'Notebooks/Likelihood_Methods/Extended-Likelihood.ipynb', **common_kwargs)

    pm.execute_notebook(
        'Notebooks/Sampling/Rejection-Sampling-MC.ipynb', **common_kwargs)

    pm.execute_notebook('Notebooks/Bayesian/Bayesian-Inference.ipynb', **common_kwargs)
