---
layout: default
title: Mitigating Bias in Graph Hyperdimensional Computing
---

# Mitigating Bias in Graph Hyperdimensional Computing
**arXiv**：[2512.07433v1](https://arxiv.org/abs/2512.07433) · [PDF](https://arxiv.org/pdf/2512.07433.pdf)  
**作者**：Yezi Liu, William Youngwoo Chung, Yang Ni, Hanning Chen, Mohsen Imani  

**一句话要点**：提出FairGHDC框架以缓解图超维计算中的偏见问题

**关键词**：图超维计算, 公平性学习, 偏见缓解, 超向量编码, 人口统计均等, 计算效率

## 3 点简述
- 研究图超维计算中数据表示和决策规则偏见导致的不公平处理
- 提出基于人口统计均等正则器的偏置校正项，转换为公平因子直接更新类超向量
- 实验显示FairGHDC显著减少公平性差距，保持准确性，训练速度提升约10倍

## 摘要（原文）

> Graph hyperdimensional computing (HDC) has emerged as a promising paradigm for cognitive tasks, emulating brain-like computation with high-dimensional vectors known as hypervectors. While HDC offers robustness and efficiency on graph-structured data, its fairness implications remain largely unexplored. In this paper, we study fairness in graph HDC, where biases in data representation and decision rules can lead to unequal treatment of different groups. We show how hypervector encoding and similarity-based classification can propagate or even amplify such biases, and we propose a fairness-aware training framework, FairGHDC, to mitigate them. FairGHDC introduces a bias correction term, derived from a gap-based demographic-parity regularizer, and converts it into a scalar fairness factor that scales the update of the class hypervector for the ground-truth label. This enables debiasing directly in the hypervector space without modifying the graph encoder or requiring backpropagation. Experimental results on six benchmark datasets demonstrate that FairGHDC substantially reduces demographic-parity and equal-opportunity gaps while maintaining accuracy comparable to standard GNNs and fairness-aware GNNs. At the same time, FairGHDC preserves the computational advantages of HDC, achieving up to about one order of magnitude ($\approx 10\times$) speedup in training time on GPU compared to GNN and fairness-aware GNN baselines.

