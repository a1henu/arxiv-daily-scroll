---
layout: default
title: BRAVA-GNN: Betweenness Ranking Approximation Via Degree MAss Inspired Graph Neural Network
---

# BRAVA-GNN: Betweenness Ranking Approximation Via Degree MAss Inspired Graph Neural Network
**arXiv**：[2602.09716v1](https://arxiv.org/abs/2602.09716) · [PDF](https://arxiv.org/pdf/2602.09716.pdf)  
**作者**：Justin Dachille, Aurora Rossi, Sunil Kumar Maurya, Frederik Mallmann-Trenn, Xin Liu, Frédéric Giroire, Tsuyoshi Murata, Emanuele Natale  

**一句话要点**：提出BRAVA-GNN以解决高直径图（如路网）上介数中心性预测的泛化问题。

**关键词**：介数中心性预测, 图神经网络, 度质量特征, 双曲随机图, 路网分析, 轻量架构

## 3 点简述
- 核心问题：大规模网络中计算介数中心性耗时，现有GNN方法在高直径图上泛化差。
- 方法要点：利用度质量相关性设计轻量GNN，采用双曲随机图模型生成训练数据。
- 实验或效果：在19个真实网络上，相比基线提升Kendall-Tau相关性达214%，推理加速70倍。

## 摘要（原文）

> Computing node importance in networks is a long-standing fundamental problem that has driven extensive study of various centrality measures. A particularly well-known centrality measure is betweenness centrality, which becomes computationally prohibitive on large-scale networks. Graph Neural Network (GNN) models have thus been proposed to predict node rankings according to their relative betweenness centrality. However, state-of-the-art methods fail to generalize to high-diameter graphs such as road networks. We propose BRAVA-GNN, a lightweight GNN architecture that leverages the empirically observed correlation linking betweenness centrality to degree-based quantities, in particular multi-hop degree mass. This correlation motivates the use of degree masses as size-invariant node features and synthetic training graphs that closely match the degree distributions of real networks. Furthermore, while previous work relies on scale-free synthetic graphs, we leverage the hyperbolic random graph model, which reproduces power-law exponents outside the scale-free regime, better capturing the structure of real-world graphs like road networks. This design enables BRAVA-GNN to generalize across diverse graph families while using 54x fewer parameters than the most lightweight existing GNN baseline. Extensive experiments on 19 real-world networks, spanning social, web, email, and road graphs, show that BRAVA-GNN achieves up to 214% improvement in Kendall-Tau correlation and up to 70x speedup in inference time over state-of-the-art GNN-based approaches, particularly on challenging road networks.

