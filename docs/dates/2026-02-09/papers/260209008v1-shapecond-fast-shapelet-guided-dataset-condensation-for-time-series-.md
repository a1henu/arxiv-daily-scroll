---
layout: default
title: ShapeCond: Fast Shapelet-Guided Dataset Condensation for Time Series Classification
---

# ShapeCond: Fast Shapelet-Guided Dataset Condensation for Time Series Classification
**arXiv**：[2602.09008v1](https://arxiv.org/abs/2602.09008) · [PDF](https://arxiv.org/pdf/2602.09008.pdf)  
**作者**：Sijia Peng, Yun Xiong, Xi Chen, Yi Xie, Guanzhi Li, Yanwei Yu, Yangyong Zhu, Zhiqiang Shen  

**一句话要点**：提出ShapeCond以快速压缩时间序列分类数据集，通过形状引导优化提升效率与准确性。

**关键词**：时间序列分类, 数据集压缩, 形状引导优化, 高效合成, 局部模式保留

## 3 点简述
- 核心问题：时间序列数据增长快，现有压缩方法多为图像设计，忽略时间结构如局部判别模式。
- 方法要点：利用形状引导优化策略，合成成本独立于序列长度，显著加速合成过程。
- 实验或效果：在广泛实验中超越先前方法，合成速度提升最高达10,000倍，下游分类准确性提高。

## 摘要（原文）

> Time series data supports many domains (e.g., finance and climate science), but its rapid growth strains storage and computation. Dataset condensation can alleviate this by synthesizing a compact training set that preserves key information. Yet most condensation methods are image-centric and often fail on time series because they miss time-series-specific temporal structure, especially local discriminative motifs such as shapelets. In this work, we propose ShapeCond, a novel and efficient condensation framework for time series classification that leverages shapelet-based dataset knowledge via a shapelet-guided optimization strategy. Our shapelet-assisted synthesis cost is independent of sequence length: longer series yield larger speedups in synthesis (e.g., 29$\times$ faster over prior state-of-the-art method CondTSC for time-series condensation, and up to 10,000$\times$ over naively using shapelets on the Sleep dataset with 3,000 timesteps). By explicitly preserving critical local patterns, ShapeCond improves downstream accuracy and consistently outperforms all prior state-of-the-art time series dataset condensation methods across extensive experiments. Code is available at https://github.com/lunaaa95/ShapeCond.

