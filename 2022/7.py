import pprint
pp = pprint.PrettyPrinter(indent=1)

cwd = ''
initial = {
    "edges": {},
    "nodes": {}
}
graph = initial
edges = []

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def cwd_to_graph_path(size, name):
    cwd_sections = ([] if cwd == '/' else '|edges|'.join(cwd.split('/')).split('|'))
    if '' in cwd_sections:
        cwd_sections.remove('')
    #print('inserting dir in ', cwd_sections)
    if size == 'dir':
        nested_set(graph, cwd_sections+ ['edges', name], {})
    else:
        nested_set(graph, cwd_sections+ ['nodes',name], int(size))

def sum_graph(graph):
    try:
        sum_nodes = sum(graph['nodes'].values())
    except:
        sum_nodes = 0
    try:
        sum_edges = sum(map(lambda edge: sum_graph(edge), graph['edges'].values()))
    except:
        sum_edges = 0
    total = sum_nodes + sum_edges
    if total < 100000:
        edges.append(total)
    return total

with open('7.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        if line[:2] == '$ ':
            argv = line[2:].split(' ')
            if argv[0] == 'cd':
                if argv[1] == '/':
                    cwd = '/'
                elif argv[1] == '..':
                    cwd = cwd[:cwd.rfind('/')]
                elif cwd == '/':
                    cwd += argv[1]
                else:
                    cwd += ('/'+argv[1])
        else:
            cwd_to_graph_path(*line.split(' '))

pp.pprint(graph)
print(sum_graph(graph))
print(edges, sum(edges))
