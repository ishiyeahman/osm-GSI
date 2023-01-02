import pickle
import gsi 
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures as futures

FILE = "out/"
WHERE = "thread_test"
PATH = FILE + WHERE

#get position of nodes
with open(f'{PATH}_pos.pkl', 'rb') as f:
    pos = pickle.load(f)
    
node = list(pos)
dict_Depth = {}
max_workers = 1000 


def process(i):
    # for i in range(20):
    lon, lat = pos.get(node[i])
    d = depth.get(lat, lon)
    new = {node[i] : d}
    dict_Depth.update(new)
    
    # print("proceed...", i)
    return d
    

    
if __name__ == '__main__':
    with tqdm(total=len(node)) as pbar:
        fs = []
        with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="thread") as executor:
            for i in range(len(node)):
                f = executor.submit(process, i)
                fs += [f]
            for f in futures.as_completed(fs):
                pbar.update(1)
            
    # with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="thread") as executor:
    #     for i in tqdm.tqdm(range(len(node))):
    #         future = executor.submit(process, i)
    #         futureList.append(future)
                
    print("file save ... ")
    with open(f'{PATH}_depth.pkl', 'wb') as f:
        pickle.dump(dict_Depth, f)
    print("End")
      
    
        
    



