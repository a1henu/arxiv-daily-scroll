---
layout: default
title: DeMa: Dual-Path Delay-Aware Mamba for Efficient Multivariate Time Series Analysis
---

# DeMa: Dual-Path Delay-Aware Mamba for Efficient Multivariate Time Series Analysis
**arXiv**：[2601.05527v1](https://arxiv.org/abs/2601.05527) · [PDF](https://arxiv.org/pdf/2601.05527.pdf)  
**作者**：Rui An, Haohao Qu, Wenqi Fan, Xuequn Shang, Qing Li  

**一句话要点**：提出DeMa以解决多变量时间序列分析中Mamba模型的局限性，提升效率与性能。

**关键词**：多变量时间序列分析, Mamba模型, 线性复杂度, 双路径架构, 延迟感知注意力, 状态空间模型

## 3 点简述
- 核心问题：Mamba在多变量时间序列中缺乏显式跨变量建模、难以解耦时间动态与交互、建模时间滞后效应不足。
- 方法要点：DeMa采用双路径设计，分解为时间路径和变量路径，分别用Mamba-SSD和Mamba-DALA模块捕获长程动态和跨变量依赖。
- 实验或效果：在五个任务上实现最优性能，保持线性复杂度，显著提升计算效率。

## 摘要（原文）

> Accurate and efficient multivariate time series (MTS) analysis is increasingly critical for a wide range of intelligent applications. Within this realm, Transformers have emerged as the predominant architecture due to their strong ability to capture pairwise dependencies. However, Transformer-based models suffer from quadratic computational complexity and high memory overhead, limiting their scalability and practical deployment in long-term and large-scale MTS modeling. Recently, Mamba has emerged as a promising linear-time alternative with high expressiveness. Nevertheless, directly applying vanilla Mamba to MTS remains suboptimal due to three key limitations: (i) the lack of explicit cross-variate modeling, (ii) difficulty in disentangling the entangled intra-series temporal dynamics and inter-series interactions, and (iii) insufficient modeling of latent time-lag interaction effects. These issues constrain its effectiveness across diverse MTS tasks. To address these challenges, we propose DeMa, a dual-path delay-aware Mamba backbone. DeMa preserves Mamba's linear-complexity advantage while substantially improving its suitability for MTS settings. Specifically, DeMa introduces three key innovations: (i) it decomposes the MTS into intra-series temporal dynamics and inter-series interactions; (ii) it develops a temporal path with a Mamba-SSD module to capture long-range dynamics within each individual series, enabling series-independent, parallel computation; and (iii) it designs a variate path with a Mamba-DALA module that integrates delay-aware linear attention to model cross-variate dependencies. Extensive experiments on five representative tasks, long- and short-term forecasting, data imputation, anomaly detection, and series classification, demonstrate that DeMa achieves state-of-the-art performance while delivering remarkable computational efficiency.

