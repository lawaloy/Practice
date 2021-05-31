{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'kruskal' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-1691da7c684d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     28\u001b[0m \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m7\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     29\u001b[0m \u001b[0medges\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 30\u001b[1;33m \u001b[0mkruskal\u001b[0m\u001b[1;33m(\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0medges\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'kruskal' is not defined"
     ]
    }
   ],
   "source": [
    "#Kruskal\n",
    "\n",
    "def kruskal_slow( n, edges ): #[ (1,2, 100), ... ]\n",
    "    edges = sorted( edges, key = lambda a : a[2] )\n",
    "    graph = [ [] for _ in range( n + 1 ) ]\n",
    "    visited = [ False ] * ( n + 1 )\n",
    "    def dfs( u ):\n",
    "        visited[ u ] = True\n",
    "        for v in graph[ u ]:\n",
    "            if visited[ v ]:\n",
    "                continue\n",
    "            dfs( v )\n",
    "    MST = []\n",
    "    mst_sum = 0\n",
    "    for u,v,w in edges:\n",
    "        for i in range( n + 1 ):\n",
    "            visited[ i ] = False\n",
    "        dfs( u )\n",
    "        if visited[ v ]:\n",
    "            continue\n",
    "        graph[ u ].append( v )\n",
    "        graph[ v ].append( u )\n",
    "        MST.append( ( u, v, w ) )\n",
    "        mst_sum += w\n",
    "    return MST, mst_sum\n",
    "\n",
    "#O(VE)\n",
    "n = 7\n",
    "edges = [(1,2,1), (2,3,2), (3,4,2), (1,4,3), (1,5,4), (5,6,7), (1,6,2)]\n",
    "kruskal( n, edges )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class DSU:\n",
    "    def __init__( self, n ):\n",
    "        self.parent = [ i for i in range( n ) ]\n",
    "        self.rank = [ 1 for _ in range( n ) ]\n",
    "        \n",
    "    def union( self, x, y ):\n",
    "        x = self.find( x )\n",
    "        y = self.find( y )\n",
    "        if x == y:\n",
    "            return\n",
    "        if self.rank[ x ] < self.rank[ y ]:\n",
    "            self.parent[ x ] = y\n",
    "        elif self.rank[ y ] < self.rank[ x ]:\n",
    "            self.parent[ y ] = x\n",
    "        else:\n",
    "            self.parent[ x ] = y\n",
    "            self.rank[ y ] += 1\n",
    "    \n",
    "    def find( self, x ):\n",
    "        if x == self.parent[ x ]:\n",
    "            return x\n",
    "        new_parent = self.find( self.parent[ x ] )\n",
    "        self.parent[ x ] = new_parent\n",
    "        return new_parent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([(1, 2, 1), (2, 3, 2), (3, 4, 2), (1, 6, 2), (1, 5, 4)], 11)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Kruskal - Fast\n",
    "def kruskal( n, edges ): #[ (1,2, 100), ... ]\n",
    "    my_sets = DSU( n + 1 )\n",
    "    edges = sorted( edges, key = lambda a : a[2] )\n",
    "    MST = []\n",
    "    mst_sum = 0\n",
    "    for u,v,w in edges:\n",
    "        if my_sets.find( u ) == my_sets.find( v ):\n",
    "            continue\n",
    "        my_sets.union( u, v )\n",
    "        MST.append( ( u, v, w ) )\n",
    "        mst_sum += w\n",
    "    return MST, mst_sum\n",
    "\n",
    "#O( ElogV )\n",
    "n = 7\n",
    "edges = [(1,2,1), (2,3,2), (3,4,2), (1,4,3), (1,5,4), (5,6,7), (1,6,2)]\n",
    "kruskal( n, edges )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Popping node 1 with weight 0\n",
      "Popping node 2 with weight 1\n",
      "Popping node 3 with weight 2\n",
      "Popping node 6 with weight 2\n",
      "Popping node 4 with weight 3\n",
      "Popping node 5 with weight 4\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([(1, 2, 1), (1, 4, 3), (1, 5, 4), (1, 6, 2), (2, 3, 2)], 12)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from heapq import heappop, heappush\n",
    "\n",
    "def prim( n, graph ):\n",
    "    visited = [ False ] * n\n",
    "    heap = [ [ 0, 1 ] ]\n",
    "    visited[ 1 ] = True\n",
    "    MST, mst_sum = [], 0\n",
    "    while len( heap ):\n",
    "        weight, u = heappop( heap )\n",
    "        for ( v, weight ) in graph[ u ]:\n",
    "            if visited[ v ]:\n",
    "                continue\n",
    "            visited[ v ] = True\n",
    "            mst_sum += weight\n",
    "            MST.append( ( u, v, weight ) )\n",
    "            heappush( heap, ( weight, v ) )\n",
    "    return MST, mst_sum\n",
    "\n",
    "def createAdjList( n, edges ):\n",
    "    graph = [ [] for _ in range( n ) ]\n",
    "    for x, y, w in edges:\n",
    "        graph[ x ].append( ( y, w ) )\n",
    "        graph[ y ].append( ( x, w ) )\n",
    "    return graph\n",
    "\n",
    "n = 7\n",
    "edges = [(1,2,1), (2,3,2), (3,4,2), (1,4,3), (1,5,4), (5,6,7), (1,6,2)]\n",
    "prim( n, createAdjList( n, edges ) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def levelOrder(self, root: TreeNode) -> List[List[int]]:\n",
    "        Q = []\n",
    "        Q.append((root,0))\n",
    "        ans = []\n",
    "        while Q:\n",
    "            node,level = Q.pop(0)\n",
    "            if node is None:\n",
    "                continue\n",
    "            if len(ans)<=level:\n",
    "                ans.append([node.val])\n",
    "            else:\n",
    "                ans[-1].append(node.val)\n",
    "            Q.append((node.left,level+1))\n",
    "            Q.append((node.right,level+1))\n",
    "        return ans \n",
    "#Binary Tree Level Order Traversal"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
