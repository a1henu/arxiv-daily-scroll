---
layout: default
title: Generating High-quality Privacy-preserving Synthetic Data
---

# Generating High-quality Privacy-preserving Synthetic Data
**arXiv**：[2602.06390v1](https://arxiv.org/abs/2602.06390) · [PDF](https://arxiv.org/pdf/2602.06390.pdf)  
**作者**：David Yavo, Richard Khoury, Christophe Pere, Sadoune Ait Kaci Azzou  

**一句话要点**：提出后处理框架以提升合成表格数据的质量与隐私保护平衡

**关键词**：合成表格数据, 隐私保护, 后处理框架, 分布保真度, k近邻过滤

## 3 点简述
- 核心问题：合成表格数据需平衡分布保真度、下游效用和隐私保护
- 方法要点：采用模式修补和k近邻过滤两步后处理，模型无关
- 实验或效果：在三个公共数据集上验证，改善分布相似性，隐私指标提升，下游性能保持稳定

## 摘要（原文）

> Synthetic tabular data enables sharing and analysis of sensitive records, but its practical deployment requires balancing distributional fidelity, downstream utility, and privacy protection. We study a simple, model agnostic post processing framework that can be applied on top of any synthetic data generator to improve this trade off. First, a mode patching step repairs categories that are missing or severely underrepresented in the synthetic data, while largely preserving learned dependencies. Second, a k nearest neighbor filter replaces synthetic records that lie too close to real data points, enforcing a minimum distance between real and synthetic samples. We instantiate this framework for two neural generative models for tabular data, a feed forward generator and a variational autoencoder, and evaluate it on three public datasets covering credit card transactions, cardiovascular health, and census based income. We assess marginal and joint distributional similarity, the performance of models trained on synthetic data and evaluated on real data, and several empirical privacy indicators, including nearest neighbor distances and attribute inference attacks. With moderate thresholds between 0.2 and 0.35, the post processing reduces divergence between real and synthetic categorical distributions by up to 36 percent and improves a combined measure of pairwise dependence preservation by 10 to 14 percent, while keeping downstream predictive performance within about 1 percent of the unprocessed baseline. At the same time, distance based privacy indicators improve and the success rate of attribute inference attacks remains largely unchanged. These results provide practical guidance for selecting thresholds and applying post hoc repairs to improve the quality and empirical privacy of synthetic tabular data, while complementing approaches that provide formal differential privacy guarantees.

