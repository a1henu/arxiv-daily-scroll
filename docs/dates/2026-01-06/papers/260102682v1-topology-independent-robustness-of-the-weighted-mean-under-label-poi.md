---
layout: default
title: Topology-Independent Robustness of the Weighted Mean under Label Poisoning Attacks in Heterogeneous Decentralized Learning
---

# Topology-Independent Robustness of the Weighted Mean under Label Poisoning Attacks in Heterogeneous Decentralized Learning
**arXiv**：[2601.02682v1](https://arxiv.org/abs/2601.02682) · [PDF](https://arxiv.org/pdf/2601.02682.pdf)  
**作者**：Jie Peng, Weiyu Li, Stefan Vlaski, Qing Ling  

**一句话要点**：分析加权平均聚合器在异构去中心化学习中标签投毒攻击下的拓扑无关鲁棒性

**关键词**：去中心化学习, 标签投毒攻击, 加权平均聚合器, 网络拓扑, 鲁棒性分析, 异构数据

## 3 点简述
- 核心问题：去中心化学习在标签投毒攻击下的鲁棒性，现有鲁棒聚合器性能受网络拓扑影响
- 方法要点：理论分析加权平均聚合器在异构条件下可超越鲁棒聚合器，性能与拓扑无关
- 实验或效果：实证支持理论，强调网络拓扑在标签投毒攻击鲁棒性中的关键作用

## 摘要（原文）

> Robustness to malicious attacks is crucial for practical decentralized signal processing and machine learning systems. A typical example of such attacks is label poisoning, meaning that some agents possess corrupted local labels and share models trained on these poisoned data. To defend against malicious attacks, existing works often focus on designing robust aggregators; meanwhile, the weighted mean aggregator is typically considered a simple, vulnerable baseline. This paper analyzes the robustness of decentralized gradient descent under label poisoning attacks, considering both robust and weighted mean aggregators. Theoretical results reveal that the learning errors of robust aggregators depend on the network topology, whereas the performance of weighted mean aggregator is topology-independent. Remarkably, the weighted mean aggregator, although often considered vulnerable, can outperform robust aggregators under sufficient heterogeneity, particularly when: (i) the global contamination rate (i.e., the fraction of poisoned agents for the entire network) is smaller than the local contamination rate (i.e., the maximal fraction of poisoned neighbors for the regular agents); (ii) the network of regular agents is disconnected; or (iii) the network of regular agents is sparse and the local contamination rate is high. Empirical results support our theoretical findings, highlighting the important role of network topology in the robustness to label poisoning attacks.

