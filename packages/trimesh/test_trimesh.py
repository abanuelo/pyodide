from pytest_pyodide import run_in_pyodide


@run_in_pyodide(packages=["trimesh"])
def test_np_unique(selenium):
    """General import for trimesh"""
    import trimesh

    mesh = trimesh.Trimesh(
        vertices=[[0, 0, 0], [0, 0, 1], [0, 1, 0]], faces=[[0, 1, 2]], process=False
    )
    assert mesh is not None
