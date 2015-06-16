import networkx as nx
from networkx.algorithms.bipartite import biadjacency_matrix
import matplotlib.pyplot as plt

# edge_prob is in format of :  e ||| f =  p(f|e)
def alignment_view(source_list, target_list, edge_prob):
    #print source_list, target_list
    B = nx.complete_bipartite_graph(len(source_list),len(target_list))
    for u,v in B.edges():
        key = source_list[u]+" ||| "+target_list[v-len(source_list)]
        if key in edge_prob:
            B[u][v]['weight']= int(edge_prob[key] /(0.25))
        else:
            B.remove_edge(u,v)
    plt.figure(1)
    #pos = nx.spring_layout(B)
    colors = [d['weight'] for (u,v,d) in B.edges(data=True)]
    #nx.draw(B,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
    #plt.savefig('full_graph.png')

    # simple bipartite layout
    #plt.figure(2)
    pos = {}
    label_pos = []
    label_pos2 = []
    glabels = {}
    offset=0.07
    for n in range(len(source_list)):
        pos[n]=(n*2,1)
        label_pos.append((n*2,1+offset))
        label_pos2.append((n*2,-1))
        glabels[n]=source_list[n]
    for n in range(len(source_list),len(target_list)+len(source_list)):
        pos[n]=((n-len(source_list))*2,0)
        label_pos.append(((n-len(source_list))*2,0-offset))
        label_pos2.append(((n-len(source_list))*2,-2-offset))
        glabels[n]=target_list[n-len(source_list)]
    nx.draw(B,pos,labels=glabels,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
    nx.draw_networkx_labels(B,label_pos,labels=glabels)
    #plt.savefig('graph_view.png')

    # biadjacency matrix colormap
    #plt.xticks([-10] +  [item*10 for item in xrange(len(source_list))],['']+source_list)
    #plt.yticks([-10] +  [item*10 for item in xrange(len(target_list))],['']+target_list)

    M = biadjacency_matrix(B,row_order=xrange(len(source_list)),column_order=xrange(len(target_list),len(target_list)+len(source_list)))
    plt.matshow(M,cmap=plt.cm.Blues)
    plt.xticks( [item for item in xrange(len(source_list))],source_list)
    plt.yticks( [item for item in xrange(len(target_list))],target_list)
    #plt.savefig('matrix_view.png')
    plt.show()

def unit_test():
    test_source_list = ["Bob","went","to","school","."]
    test_target_list = ["Bob","went","to","school","."]
    edge_prob={}
    edge_prob["Bob ||| Bob"]=1
    edge_prob["went ||| went"]=0.8
    edge_prob["went ||| to"]=0.2
    edge_prob["to ||| to"]= 0.55
    edge_prob["to ||| went"]=0.45
    edge_prob["school ||| to"]=0.33
    edge_prob["school ||| school"]=0.33
    edge_prob["school ||| ."]=0.33
    edge_prob[". ||| ."]=1

    alignment_view(test_source_list, test_target_list, edge_prob)

if __name__ == '__main__':
    unit_test()
