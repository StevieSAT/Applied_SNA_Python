import networkx as nx
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def answer_four():
    
    # YOUR CODE HERE
    df = pd.read_csv('assets/Employee_Movie_Choices.txt', header=None, delimiter='\t')
    df.columns = ['employee', 'movie']
    g = nx.from_pandas_edgelist(df, 'employee', 'movie')
    
    gtest = pd.DataFrame(answer_three().edges(data=True), columns=['E1', 'E2', 'MovieCommon'])
    gtest['MovieCommon'] = gtest['MovieCommon'].map(lambda x: x['weight'])
    
    g4_relation2 = pd.read_csv('assets/Employee_Relationships.txt', sep='\t', ## you may need to change the path 'Employee_Relationships.txt'
                   header=None, names=['E1', 'E2', 'Relationship'])
    
    g4_MovieRelation = []
    for e1, e2 in g4_relation2[['E1', 'E2']].itertuples(index=False):
        movies_in_common = set(g.neighbors(e1)) & set(g.neighbors(e2))
        g4_MovieRelation.append((e1, e2, len(movies_in_common) or 0))

    g4_MovieRelation_df = pd.DataFrame(g4_MovieRelation, columns=['E1', 'E2', 'movies'])

    pearson_corr, _ = pearsonr(g4_relation2.set_index(['E1', 'E2']).Relationship, g4_MovieRelation_df.set_index(['E1', 'E2']).movies)
    
    return pearson_corr
    raise NotImplementedError()
#answer_four()
