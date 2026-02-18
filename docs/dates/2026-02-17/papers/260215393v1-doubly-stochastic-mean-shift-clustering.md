---
layout: default
title: Doubly Stochastic Mean-Shift Clustering
---

# Doubly Stochastic Mean-Shift Clustering
**arXiv**：[2602.15393v1](https://arxiv.org/abs/2602.15393) · [PDF](https://arxiv.org/pdf/2602.15393.pdf)  
**作者**：Tom Trigano, Yann Sepulcre, Itshak Lapidot  

**一句话要点**：提出双随机均值漂移聚类以解决带宽超参数敏感性问题

**关键词**：均值漂移聚类, 随机带宽, 密度估计, 聚类稳定性, 超参数敏感

## 3 点简述
- 标准均值漂移算法对带宽超参数敏感，在数据稀缺时易导致分割和虚假模式
- 引入随机性于轨迹更新和核带宽，通过均匀分布采样实现密度景观的更好探索
- 在合成高斯混合实验中显著优于基线，提高稳定性并防止过分割

## 摘要（原文）

> Standard Mean-Shift algorithms are notoriously sensitive to the bandwidth hyperparameter, particularly in data-scarce regimes where fixed-scale density estimation leads to fragmentation and spurious modes. In this paper, we propose Doubly Stochastic Mean-Shift (DSMS), a novel extension that introduces randomness not only in the trajectory updates but also in the kernel bandwidth itself. By drawing both the data samples and the radius from a continuous uniform distribution at each iteration, DSMS effectively performs a better exploration of the density landscape. We show that this randomized bandwidth policy acts as an implicit regularization mechanism, and provide convergence theoretical results. Comparative experiments on synthetic Gaussian mixtures reveal that DSMS significantly outperforms standard and stochastic Mean-Shift baselines, exhibiting remarkable stability and preventing over-segmentation in sparse clustering scenarios without other performance degradation.

