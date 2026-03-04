---
layout: default
title: Neural quantum support vector data description for one-class classification
---

# Neural quantum support vector data description for one-class classification
**arXiv**：[2603.02700v1](https://arxiv.org/abs/2603.02700) · [PDF](https://arxiv.org/pdf/2603.02700.pdf)  
**作者**：Changjae Im, Hyeondo Oh, Daniel K. Park  

**一句话要点**：提出神经量子支持向量数据描述框架，用于一分类任务以提升表达性和效率。

**关键词**：一分类, 量子机器学习, 支持向量数据描述, 异常检测, 混合架构, 表示学习

## 3 点简述
- 一分类是机器学习基础问题，适用于异常检测和质量控制等场景。
- 结合经典神经网络与可训练量子编码及变分量子电路，实现端到端优化层次表示学习。
- 在基准数据集上，相比经典和量子基线，达到竞争或更优的AUC性能，参数高效且噪声鲁棒。

## 摘要（原文）

> One-class classification (OCC) is a fundamental problem in machine learning with numerous applications, such as anomaly detection and quality control. With the increasing complexity and dimensionality of modern datasets, there is a growing demand for advanced OCC techniques with better expressivity and efficiency. We introduce Neural Quantum Support Vector Data Description (NQSVDD), a classical-quantum hybrid framework for OCC that performs end-to-end optimized hierarchical representation learning. NQSVDD integrates a classical neural network with trainable quantum data encoding and a variational quantum circuit, enabling the model to learn nonlinear feature transformations tailored to the OCC objective. The hybrid architecture maps input data into an intermediate high-dimensional feature space and subsequently projects it into a compact latent space defined through quantum measurements. Importantly, both the feature embedding and the latent representation are jointly optimized such that normal data form a compact cluster, for which a minimum-volume enclosing hypersphere provides an effective decision boundary. Experimental evaluations on benchmark datasets demonstrate that NQSVDD achieves competitive or superior AUC performance compared to classical Deep SVDD and quantum baselines, while maintaining parameter efficiency and robustness under realistic noise conditions.

