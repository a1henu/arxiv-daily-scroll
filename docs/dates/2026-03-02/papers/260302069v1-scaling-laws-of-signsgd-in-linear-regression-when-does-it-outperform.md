---
layout: default
title: Scaling Laws of SignSGD in Linear Regression: When Does It Outperform SGD?
---

# Scaling Laws of SignSGD in Linear Regression: When Does It Outperform SGD?
**arXiv**：[2603.02069v1](https://arxiv.org/abs/2603.02069) · [PDF](https://arxiv.org/pdf/2603.02069.pdf)  
**作者**：Jihwan Kim, Dogyoon Song, Chulhee Yun  

**一句话要点**：分析signSGD在线性回归中的缩放定律，揭示其在噪声主导时优于SGD的条件。

**关键词**：signSGD, 缩放定律, 线性回归, 噪声重塑, 计算最优, WSD调度

## 3 点简述
- 研究signSGD在幂律随机特征模型下的缩放定律，考虑特征和目标衰减。
- 识别signSGD特有的漂移归一化和噪声重塑效应，并推导计算最优缩放定律。
- 发现WSD调度在特定衰减条件下能进一步降低噪声，优化性能。

## 摘要（原文）

> We study scaling laws of signSGD under a power-law random features (PLRF) model that accounts for both feature and target decay. We analyze the population risk of a linear model trained with one-pass signSGD on Gaussian-sketched features. We express the risk as a function of model size, training steps, learning rate, and the feature and target decay parameters. Comparing against the SGD risk analyzed by Paquette et al. (2024), we identify a drift-normalization effect and a noise-reshaping effect unique to signSGD. We then obtain compute-optimal scaling laws under the optimal choice of learning rate. Our analysis shows that the noise-reshaping effect can make the compute-optimal slope of signSGD steeper than that of SGD in regimes where noise is dominant. Finally, we observe that the widely used warmup-stable-decay (WSD) schedule further reduces the noise term and sharpens the compute-optimal slope, when feature decay is fast but target decay is slow.

