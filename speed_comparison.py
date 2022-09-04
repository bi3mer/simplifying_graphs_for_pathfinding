from timeit import timeit
from pickle import load
from networkx import astar_path
from tqdm import tqdm
import os

SIZES = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

for S in tqdm(SIZES, leave=False):
    save_name = os.path.join('mazes', f'run_times_{S}.csv')
    if os.path.exists(save_name):
        continue

    START = (0,S-1)
    END = (S-1,0)

    run_times_G = []
    run_times_HG = []
    match_comparison = f'_{S}'
    for dir_name in tqdm(os.listdir('mazes'), leave=False):
        if match_comparison not in dir_name or 'run_times' in dir_name:
            continue
        
        base_path = os.path.join('mazes', dir_name)
        with open(os.path.join(base_path, 'maze_graph.pkl'), 'rb') as f:
            G = load(f)

        with open(os.path.join(base_path, 'maze_hyper_graph.pkl'), 'rb') as f:
            HG = load(f)

        with open(os.path.join(base_path, 'node_lookup.pkl'), 'rb') as f:
            NL = load(f)

        def test_g():
            p = astar_path(G, START, END)
        run_times_G.append(timeit('test_g()', "from __main__ import test_g", number=100))

        def test_hg():
            p = astar_path(HG, NL[START], NL[END])
        run_times_HG.append(timeit('test_hg()', "from __main__ import test_hg", number=100))

    with open(save_name, 'w') as f:
        f.write('G,HG\n')
        for a1, a2 in zip(run_times_G, run_times_HG):
            f.write(f'{a1},{a2}\n')
