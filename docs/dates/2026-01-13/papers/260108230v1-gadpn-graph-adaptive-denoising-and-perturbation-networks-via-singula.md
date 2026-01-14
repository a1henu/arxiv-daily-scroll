---
layout: default
title: GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular Value Decomposition
---

# GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular Value Decomposition
**arXiv**：[2601.08230v1](https://arxiv.org/abs/2601.08230) · [PDF](https://arxiv.org/pdf/2601.08230.pdf)  
**作者**：Hao Deng, Bo Liu  

**一句话要点**：提出GADPN框架，通过奇异值分解自适应优化图结构以提升图神经网络性能

**关键词**：图结构学习, 奇异值分解, 自适应去噪, 图神经网络, 结构扰动

## 3 点简述
- 核心问题：图神经网络性能受限于观测图中的噪声、缺失链接或结构不匹配，现有图结构学习方法计算成本高
- 方法要点：基于贝叶斯优化自适应确定去噪强度，并利用奇异值分解扩展结构扰动方法至任意图
- 实验或效果：在基准数据集上实现最先进性能，显著提升效率，尤其在非同配性图上表现突出

## 摘要（原文）

> While Graph Neural Networks (GNNs) excel on graph-structured data, their performance is fundamentally limited by the quality of the observed graph, which often contains noise, missing links, or structural properties misaligned with GNNs' underlying assumptions. To address this, graph structure learning aims to infer a more optimal topology. Existing methods, however, often incur high computational costs due to complex generative models and iterative joint optimization, limiting their practical utility. In this paper, we propose GADPN, a simple yet effective graph structure learning framework that adaptively refines graph topology via low-rank denoising and generalized structural perturbation. Our approach makes two key contributions: (1) we introduce Bayesian optimization to adaptively determine the optimal denoising strength, tailoring the process to each graph's homophily level; and (2) we extend the structural perturbation method to arbitrary graphs via Singular Value Decomposition (SVD), overcoming its original limitation to symmetric structures. Extensive experiments on benchmark datasets demonstrate that GADPN achieves state-of-the-art performance while significantly improving efficiency. It shows particularly strong gains on challenging disassortative graphs, validating its ability to robustly learn enhanced graph structures across diverse network types.

