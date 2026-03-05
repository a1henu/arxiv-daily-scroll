---
layout: default
title: Beyond Edge Deletion: A Comprehensive Approach to Counterfactual Explanation in Graph Neural Networks
---

# Beyond Edge Deletion: A Comprehensive Approach to Counterfactual Explanation in Graph Neural Networks
**arXiv**：[2603.04209v1](https://arxiv.org/abs/2603.04209) · [PDF](https://arxiv.org/pdf/2603.04209.pdf)  
**作者**：Matteo De Sanctis, Riccardo De Sanctis, Stefano Faralli, Paola Velardi, Bardh Prenkaj  

**一句话要点**：提出XPlore技术以扩展图神经网络反事实解释的搜索空间

**关键词**：图神经网络, 反事实解释, 梯度引导扰动, 邻接矩阵扰动, 节点特征扰动, 可解释性评估

## 3 点简述
- 核心问题：图神经网络的黑盒性质在高风险应用中阻碍可解释性和信任。
- 方法要点：基于梯度联合扰动邻接矩阵和节点特征矩阵，支持边插入和特征扰动。
- 实验或效果：在13个真实和5个合成基准上，有效性和保真度提升超50%。

## 摘要（原文）

> Graph Neural Networks (GNNs) are increasingly adopted across domains such as molecular biology and social network analysis, yet their black-box nature hinders interpretability and trust. This is especially problematic in high-stakes applications, such as predicting molecule toxicity, drug discovery, or guiding financial fraud detections, where transparent explanations are essential. Counterfactual explanations - minimal changes that flip a model's prediction - offer a transparent lens into GNNs' behavior. In this work, we introduce XPlore, a novel technique that significantly broadens the counterfactual search space. It consists of gradient-guided perturbations to adjacency and node feature matrices. Unlike most prior methods, which focus solely on edge deletions, our approach belongs to the growing class of techniques that optimize edge insertions and node-feature perturbations, here jointly performed under a unified gradient-based framework, enabling a richer and more nuanced exploration of counterfactuals. To quantify both structural and semantic fidelity, we introduce a cosine similarity metric for learned graph embeddings that addresses a key limitation of traditional distance-based metrics, and demonstrate that XPlore produces more coherent and minimal counterfactuals. Empirical results on 13 real-world and 5 synthetic benchmarks show up to +56.3% improvement in validity and +52.8% in fidelity over state-of-the-art baselines, while retaining competitive runtime.

