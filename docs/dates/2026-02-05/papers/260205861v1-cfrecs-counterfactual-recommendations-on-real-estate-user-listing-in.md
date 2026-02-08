---
layout: default
title: CFRecs: Counterfactual Recommendations on Real Estate User Listing Interaction Graphs
---

# CFRecs: Counterfactual Recommendations on Real Estate User Listing Interaction Graphs
**arXiv**：[2602.05861v1](https://arxiv.org/abs/2602.05861) · [PDF](https://arxiv.org/pdf/2602.05861.pdf)  
**作者**：Seyedmasoud Mousavi, Ruomeng Xu, Xiaojing Zhu  

**一句话要点**：提出CFRecs框架，通过反事实图学习为房地产推荐系统提供可操作建议。

**关键词**：反事实图学习, 图神经网络, 推荐系统, 房地产数据, 图变分自编码器, 可解释性

## 3 点简述
- 核心问题：图神经网络在推荐系统中缺乏可解释性，难以提供用户可操作的改进建议。
- 方法要点：采用两阶段架构，结合图神经网络和图变分自编码器，优化图结构和节点属性的最小高影响变化。
- 实验或效果：在Zillow用户-房源交互数据上验证有效性，为买卖双方提供反事实推理的推荐新视角。

## 摘要（原文）

> Graph-structured data is ubiquitous and powerful in representing complex relationships in many online platforms. While graph neural networks (GNNs) are widely used to learn from such data, counterfactual graph learning has emerged as a promising approach to improve model interpretability. Counterfactual explanation research focuses on identifying a counterfactual graph that is similar to the original but leads to different predictions. These explanations optimize two objectives simultaneously: the sparsity of changes in the counterfactual graph and the validity of its predictions. Building on these qualitative optimization goals, this paper introduces CFRecs, a novel framework that transforms counterfactual explanations into actionable insights. CFRecs employs a two-stage architecture consisting of a graph neural network (GNN) and a graph variational auto-encoder (Graph-VAE) to strategically propose minimal yet high-impact changes in graph structure and node attributes to drive desirable outcomes in recommender systems. We apply CFRecs to Zillow's graph-structured data to deliver actionable recommendations for both home buyers and sellers with the goal of helping them navigate the competitive housing market and achieve their homeownership goals. Experimental results on Zillow's user-listing interaction data demonstrate the effectiveness of CFRecs, which also provides a fresh perspective on recommendations using counterfactual reasoning in graphs.

