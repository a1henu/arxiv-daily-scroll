---
layout: default
title: High-Dimensional Change Point Detection using Graph Spanning Ratio
---

# High-Dimensional Change Point Detection using Graph Spanning Ratio
**arXiv**：[2512.07541v1](https://arxiv.org/abs/2512.07541) · [PDF](https://arxiv.org/pdf/2512.07541.pdf)  
**作者**：Youngwen Sun, Katerina Papagiannouli, Vladimir Spokoiny  

**一句话要点**：提出基于图生成比的高维变点检测算法，适用于离线和在线数据场景。

**关键词**：高维变点检测, 图生成比算法, 在线检测, 未知分布数据, 错误概率控制, 检测力分析

## 3 点简述
- 核心问题：高维数据中未知分布的变点检测，需控制错误概率。
- 方法要点：利用图生成比算法，适应欧几里得和图结构数据，理论证明检测能力强。
- 实验或效果：在Gaussian和非Gaussian数据上准确度优于其他方法，小观测窗口下仍保持高检测力。

## 摘要（原文）

> Inspired by graph-based methodologies, we introduce a novel graph-spanning algorithm designed to identify changes in both offline and online data across low to high dimensions. This versatile approach is applicable to Euclidean and graph-structured data with unknown distributions, while maintaining control over error probabilities. Theoretically, we demonstrate that the algorithm achieves high detection power when the magnitude of the change surpasses the lower bound of the minimax separation rate, which scales on the order of $\sqrt{nd}$. Our method outperforms other techniques in terms of accuracy for both Gaussian and non-Gaussian data. Notably, it maintains strong detection power even with small observation windows, making it particularly effective for online environments where timely and precise change detection is critical.

