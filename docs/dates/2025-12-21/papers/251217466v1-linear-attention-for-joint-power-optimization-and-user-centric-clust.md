---
layout: default
title: Linear Attention for Joint Power Optimization and User-Centric Clustering in Cell-Free Networks
---

# Linear Attention for Joint Power Optimization and User-Centric Clustering in Cell-Free Networks
**arXiv**：[2512.17466v1](https://arxiv.org/abs/2512.17466) · [PDF](https://arxiv.org/pdf/2512.17466.pdf)  
**作者**：Irched Chafaa, Giacomo Bacci, Luca Sanguinetti  

**一句话要点**：提出轻量级Transformer模型，联合预测AP聚类和功率分配以优化用户中心无蜂窝网络性能。

**关键词**：无蜂窝大规模MIMO, 用户中心聚类, 功率分配, 线性注意力, Transformer模型, 导频污染避免

## 3 点简述
- 核心问题：现有深度学习模型在动态网络配置中灵活性不足，且常忽略导频污染和高计算复杂度。
- 方法要点：基于用户和AP空间坐标，使用线性注意力机制高效捕获交互，无需信道估计，避免导频污染。
- 实验或效果：数值结果证实模型最大化最小频谱效率，提供近最优性能，确保动态场景下的适应性和可扩展性。

## 摘要（原文）

> Optimal AP clustering and power allocation are critical in user-centric cell-free massive MIMO systems. Existing deep learning models lack flexibility to handle dynamic network configurations. Furthermore, many approaches overlook pilot contamination and suffer from high computational complexity. In this paper, we propose a lightweight transformer model that overcomes these limitations by jointly predicting AP clusters and powers solely from spatial coordinates of user devices and AP. Our model is architecture-agnostic to users load, handles both clustering and power allocation without channel estimation overhead, and eliminates pilot contamination by assigning users to AP within a pilot reuse constraint. We also incorporate a customized linear attention mechanism to capture user-AP interactions efficiently and enable linear scalability with respect to the number of users. Numerical results confirm the model's effectiveness in maximizing the minimum spectral efficiency and providing near-optimal performance while ensuring adaptability and scalability in dynamic scenarios.

