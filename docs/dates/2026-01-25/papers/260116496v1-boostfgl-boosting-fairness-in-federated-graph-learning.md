---
layout: default
title: BoostFGL: Boosting Fairness in Federated Graph Learning
---

# BoostFGL: Boosting Fairness in Federated Graph Learning
**arXiv**：[2601.16496v1](https://arxiv.org/abs/2601.16496) · [PDF](https://arxiv.org/pdf/2601.16496.pdf)  
**作者**：Zekai Chen, Kairui Yang, Xunkai Li, Henan Sun, Zhihan Zhang, Jia Li, Qiangqiang Dai, Rong-Hua Li, Guoren Wang  

**一句话要点**：提出BoostFGL框架以解决联邦图学习中节点组间公平性下降问题

**关键词**：联邦图学习, 公平性增强, 图神经网络, 节点组公平, 客户端增强, 服务器端聚合

## 3 点简述
- 核心问题：联邦图学习平均性能高但掩盖了弱势节点组性能严重下降，源于标签偏斜、拓扑混淆和聚合稀释。
- 方法要点：通过客户端节点和拓扑增强及服务器端模型增强，协调提升公平性。
- 实验或效果：在9个数据集上显著提升公平性，Overall-F1提高8.43%，同时保持整体性能竞争力。

## 摘要（原文）

> Federated graph learning (FGL) enables collaborative training of graph neural networks (GNNs) across decentralized subgraphs without exposing raw data. While existing FGL methods often achieve high overall accuracy, we show that this average performance can conceal severe degradation on disadvantaged node groups. From a fairness perspective, these disparities arise systematically from three coupled sources: label skew toward majority patterns, topology confounding in message propagation, and aggregation dilution of updates from hard clients. To address this, we propose \textbf{BoostFGL}, a boosting-style framework for fairness-aware FGL. BoostFGL introduces three coordinated mechanisms: \ding{182} \emph{Client-side node boosting}, which reshapes local training signals to emphasize systematically under-served nodes; \ding{183} \emph{Client-side topology boosting}, which reallocates propagation emphasis toward reliable yet underused structures and attenuates misleading neighborhoods; and \ding{184} \emph{Server-side model boosting}, which performs difficulty- and reliability-aware aggregation to preserve informative updates from hard clients while stabilizing the global model. Extensive experiments on 9 datasets show that BoostFGL delivers substantial fairness gains, improving Overall-F1 by 8.43\%, while preserving competitive overall performance against strong FGL baselines.

