# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Find a build order (dependency order) that allows projects to be built
# Construct an ordered graph d1 -> d2 for each dependency, detect a cycle.
# If cycle, cannot be built. If no cycle, can be built.

from graph import Graph

def get_build_order(dependencies, projects):
    g = Graph(projects, directed=True)
    for d1, d2 in dependencies:
        g.add_edge(d1, d2)

    return g.topological_order()


if __name__ == '__main__':
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    projects = ['a', 'b', 'c', 'd', 'e', 'f']

    print([n.name for n in get_build_order(dependencies, projects)])

    dependencies = [('f', 'c'), ('f', 'b'), ('f', 'a'), ('a', 'e'), ('d', 'g'), ('b', 'h')]
    projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    print([n.name for n in get_build_order(dependencies, projects)])



