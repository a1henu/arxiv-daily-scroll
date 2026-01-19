---
layout: default
title: TimeMar: Multi-Scale Autoregressive Modeling for Unconditional Time Series Generation
---

# TimeMar: Multi-Scale Autoregressive Modeling for Unconditional Time Series Generation
**arXiv**：[2601.11184v1](https://arxiv.org/abs/2601.11184) · [PDF](https://arxiv.org/pdf/2601.11184.pdf)  
**作者**：Xiangyu Xu, Qingsong Zhong, Jilin Hu  

**一句话要点**：提出多尺度自回归框架TimeMar，以解决时间序列生成中的结构复杂性问题。

**关键词**：时间序列生成, 多尺度建模, 自回归模型, 结构解耦, VQ-VAE

## 3 点简述
- 核心问题：时间序列的多尺度模式和异质组件导致生成质量不足。
- 方法要点：使用双路径VQ-VAE解耦趋势与季节性，并采用粗到细的自回归生成。
- 实验或效果：在六个数据集上优于现有方法，参数少且能生成高质量长序列。

## 摘要（原文）

> Generative modeling offers a promising solution to data scarcity and privacy challenges in time series analysis. However, the structural complexity of time series, characterized by multi-scale temporal patterns and heterogeneous components, remains insufficiently addressed. In this work, we propose a structure-disentangled multiscale generation framework for time series. Our approach encodes sequences into discrete tokens at multiple temporal resolutions and performs autoregressive generation in a coarse-to-fine manner, thereby preserving hierarchical dependencies. To tackle structural heterogeneity, we introduce a dual-path VQ-VAE that disentangles trend and seasonal components, enabling the learning of semantically consistent latent representations. Additionally, we present a guidance-based reconstruction strategy, where coarse seasonal signals are utilized as priors to guide the reconstruction of fine-grained seasonal patterns. Experiments on six datasets show that our approach produces higher-quality time series than existing methods. Notably, our model achieves strong performance with a significantly reduced parameter count and exhibits superior capability in generating high-quality long-term sequences. Our implementation is available at https://anonymous.4open.science/r/TimeMAR-BC5B.

