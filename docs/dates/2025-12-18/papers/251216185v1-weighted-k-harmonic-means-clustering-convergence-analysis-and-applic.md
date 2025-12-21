---
layout: default
title: Weighted K-Harmonic Means Clustering: Convergence Analysis and Applications to Wireless Communications
---

# Weighted K-Harmonic Means Clustering: Convergence Analysis and Applications to Wireless Communications
**arXiv**：[2512.16185v1](https://arxiv.org/abs/2512.16185) · [PDF](https://arxiv.org/pdf/2512.16185.pdf)  
**作者**：Gourab Ghatak  

**一句话要点**：提出加权K调和均值聚类算法，确保数值稳定性并应用于无线网络用户关联。

**关键词**：加权K调和均值聚类, 无线网络用户关联, 收敛性分析, 软分配, 数值稳定性, 信号强度优化

## 3 点简述
- 核心问题：传统K调和均值聚类在数值稳定性和软分配方面存在不足，需改进以适应无线网络场景。
- 方法要点：引入加权K调和均值，通过逆距离加权实现软分配，权重对应无线信号强度，提供收敛性保证。
- 实验或效果：模拟显示算法在信号强度和负载公平性间取得更好权衡，优于现有基线方法。

## 摘要（原文）

> We propose the \emph{weighted K-harmonic means} (WKHM) clustering algorithm, a regularized variant of K-harmonic means designed to ensure numerical stability while enabling soft assignments through inverse-distance weighting. Unlike classical K-means and constrained K-means, WKHM admits a direct interpretation in wireless networks: its weights are exactly equivalent to fractional user association based on received signal strength. We establish rigorous convergence guarantees under both deterministic and stochastic settings, addressing key technical challenges arising from non-convexity and random initialization. Specifically, we prove monotone descent to a local minimum under fixed initialization, convergence in probability under Binomial Point Process (BPP) initialization, and almost sure convergence under mild decay conditions. These results provide the first stochastic convergence guarantees for harmonic-mean-based clustering. Finally, through extensive simulations with diverse user distributions, we show that WKHM achieves a superior tradeoff between minimum signal strength and load fairness compared to classical and modern clustering baselines, making it a principled tool for joint radio node placement and user association in wireless networks.

