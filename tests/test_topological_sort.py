import pytest

from algorithms.topological_sort import Pipeline, resolve_dependencies

def test_topological_sort():
    pipe01 = Pipeline("pipe01")
    pipe02 = Pipeline("pipe02")
    pipe03 = Pipeline("pipe03")
    pipe04 = Pipeline("pipe04")

    pipe03.dependencies.update([pipe01, pipe02])
    pipe04.dependencies.update([pipe02, pipe03])

    pipelines = [pipe01, pipe02, pipe03, pipe04]

    assert len(resolve_dependencies(pipelines=pipelines))

