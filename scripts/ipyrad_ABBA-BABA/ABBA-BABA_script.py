#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipyrad.analysis as ipa
import ipyparallel as ipp
import toytree
import toyplot


# In[2]:


## ipyrad and raxml output files
locifile = "./Pogos/10SNPs.loci"
newick = "./Pogos/RAxML_bipartitions_10SNPs.nwk"


# In[3]:


## parse the newick tree.
tre = toytree.tree(newick=newick)


# In[4]:


## create a baba object linked to a data file and newick tree
bb = ipa.baba(data=locifile, newick=newick)


# In[5]:


## connect to cluster
ipyclient = ipp.Client()
ipyclient.ids


# In[6]:


bb.tests = [
    {"p4": ["Out_Pocc"],
        "p3": ["F2_MF", "F2_ROS", "G2_HOB", "G2_ALA", "H2_SS", "H2_H", "H2_Hill"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["F1_MF", "G1_HOB", "G1_ALA", "F1_ROS", "H1_H", "H1_SS", "H1_Hill", "FGH1_GP"]},
    {"p4": ["Out_Pocc"],
        "p3": ["F2_MF", "F2_ROS"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["F1_MF", "F1_ROS"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G2_HOB", "G2_ALA"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["G1_HOB", "G1_ALA"]},
    {"p4": ["Out_Pocc"],
        "p3": ["H2_SS", "H2_H", "H2_Hill"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["H1_H", "H1_SS", "H1_Hill"]},
    {"p4": ["Out_Pocc"],
        "p3": ["F1_MF", "G1_HOB", "G1_ALA", "F1_ROS", "H1_H", "H1_SS", "H1_Hill", "FGH1_GP"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["F2_MF", "F2_ROS", "G2_HOB", "G2_ALA", "H2_SS", "H2_H", "H2_Hill"]},
    {"p4": ["Out_Pocc"],
        "p3": ["F1_MF", "F1_ROS"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["F2_MF", "F2_ROS"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G1_HOB", "G1_ALA"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["G2_HOB", "G2_ALA"]},
    {"p4": ["Out_Pocc"],
        "p3": ["H1_H", "H1_SS", "H1_Hill"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["H2_SS", "H2_H", "H2_Hill"]},
    { "p4": ["Out_Pocc"],
        "p3": ["J2_FB", "J2_SL"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["J1_SON", "J1_SL", "J1_FB"]},
    { "p4": ["Out_Pocc"],
        "p3": ["J1_SON", "J1_SL", "J1_FB"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["J2_FB", "J2_SL"]},
    {"p4": ["Out_Pocc"],
        "p3": ["F2_MF", "F2_ROS", "G2_HOB", "G2_ALA", "H2_SS", "H2_H", "H2_Hill"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["F1_MF", "G1_HOB", "G1_ALA", "F1_ROS", "H1_H", "H1_SS", "H1_Hill", "FGH1_GP"]},
    {"p4": ["Out_Pocc"],
        "p3": ["F2_MF", "F2_ROS"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["F1_MF", "F1_ROS"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G2_HOB", "G2_ALA"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["G1_HOB", "G1_ALA"]},
    {"p4": ["Out_Pocc"],
        "p3": ["H2_SS", "H2_H", "H2_Hill"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["H1_H", "H1_SS", "H1_Hill"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G2_HOB"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["G1_HOB"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G2_ALA"],
        "p2": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"],
        "p1": ["G1_ALA"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G1_HOB"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["G2_HOB"]},
    {"p4": ["Out_Pocc"],
        "p3": ["G1_ALA"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["G2_ALA"]},
    { "p4": ["Out_Pocc"],
        "p3": ["J1_FB"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["J2_FB"]},
    { "p4": ["Out_Pocc"],
        "p3": ["J1_SL"],
        "p2": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p1": ["J2_SL"]},
    {"p4": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p3": ["J1_SON", "J1_SL", "J1_FB"],
        "p2": ["F1_MF", "G1_HOB", "G1_ALA", "F1_ROS", "H1_H", "H1_SS", "H1_Hill", "FGH1_GP"],
        "p1": ["Pr_EPW", "Pr_K40"]},
    {"p4": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p3": ["F1_MF", "G1_HOB", "G1_ALA", "F1_ROS", "H1_H", "H1_SS", "H1_Hill", "FGH1_GP"],
        "p2": ["J1_SON", "J1_SL", "J1_FB"],
        "p1": ["Pr_B", "Pr_Q", "Pr_WS", "Pr_PHX"]},
    {"p4": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p3": ["J1_SON", "J1_SL", "J1_FB"],
        "p2": ["F1_MF", "F1_ROS"],
        "p1": ["Pr_EPW", "Pr_K40"]},
    {"p4": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p3": ["J1_SON", "J1_SL", "J1_FB"],
        "p2": ["G1_HOB", "G1_ALA"],
        "p1": ["Pr_EPW", "Pr_K40"]},
    {"p4": ["Pb_LW", "Pb_CT", "Pb_TOR5", "Pb_TOR23"],
        "p3": ["J1_SON", "J1_SL", "J1_FB"],
        "p2": ["H1_H", "H1_SS", "H1_Hill"],
        "p1": ["Pr_EPW", "Pr_K40"]},
]


# In[7]:


## run all tests linked to bb 
bb.run(ipyclient)


# In[8]:

#print out results table
bb.results_table


# In[9]:

#build tree plot of Z scores for each test showing comparisons on tree
bb.plot(height=600,width=1200,pct_tree_x=0.4);



