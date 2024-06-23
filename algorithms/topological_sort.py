from collections import deque

# Pipeline object
class Pipeline:
    def __init__(self, name: str) -> None:
        self.name = name
        self.dependencies = set()
    
    def executor(self, params: dict = {}) -> None:
        print("Executing pipe: ", self.name)


def resolve_dependencies(pipelines: list[Pipeline]) -> list[Pipeline]:
    """
    Dependecy resolver

    :param pipelines: :class:`list[User]`
    """

    # Build a dictionary to store the indegree of each pipeline
    indegree = {pipeline: 0 for pipeline in pipelines}
    for pipeline in pipelines:
        for dependency in pipeline.dependencies:
            indegree[dependency] += 1

    # Perform topological sorting
    resolved_order = []
    queue = deque([pipeline for pipeline in pipelines if indegree[pipeline] == 0])

    while queue:
        current_pipeline = queue.popleft()
        resolved_order.append(current_pipeline)

        for dependency in current_pipeline.dependencies:
            indegree[dependency] -= 1
            if indegree[dependency] == 0:
                queue.append(dependency)

    # Check for cycles
    if len(resolved_order) != len(pipelines):
        raise ValueError("Dependency graph contains a cycle")

    return resolved_order
