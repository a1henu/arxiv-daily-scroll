---
layout: default
title: PLGC: Pseudo-Labeled Graph Condensation
---

# PLGC: Pseudo-Labeled Graph Condensation
**arXiv**：[2601.10358v1](https://arxiv.org/abs/2601.10358) · [PDF](https://arxiv.org/pdf/2601.10358.pdf)  
**作者**：Jay Nandy, Arnab Kumar Mondal, Anuj Rathore, Mahesh Chandran  

**一句话要点**：提出伪标签图压缩以解决标签稀缺或噪声下的大图训练成本问题

**关键词**：图神经网络, 图压缩, 自监督学习, 伪标签, 节点分类, 链接预测

## 3 点简述
- 核心问题：现有图压缩方法依赖干净监督标签，在标签稀缺、噪声或不一致时可靠性受限
- 方法要点：通过自监督框架从节点嵌入构建潜在伪标签，优化压缩图以匹配原图的结构和特征统计
- 实验或效果：在节点分类和链接预测任务中，PLGC在干净数据集上性能与监督方法相当，在标签噪声下表现出显著鲁棒性

## 摘要（原文）

> Large graph datasets make training graph neural networks (GNNs) computationally costly. Graph condensation methods address this by generating small synthetic graphs that approximate the original data. However, existing approaches rely on clean, supervised labels, which limits their reliability when labels are scarce, noisy, or inconsistent. We propose Pseudo-Labeled Graph Condensation (PLGC), a self-supervised framework that constructs latent pseudo-labels from node embeddings and optimizes condensed graphs to match the original graph's structural and feature statistics -- without requiring ground-truth labels. PLGC offers three key contributions: (1) A diagnosis of why supervised condensation fails under label noise and distribution shift. (2) A label-free condensation method that jointly learns latent prototypes and node assignments. (3) Theoretical guarantees showing that pseudo-labels preserve latent structural statistics of the original graph and ensure accurate embedding alignment. Empirically, across node classification and link prediction tasks, PLGC achieves competitive performance with state-of-the-art supervised condensation methods on clean datasets and exhibits substantial robustness under label noise, often outperforming all baselines by a significant margin. Our findings highlight the practical and theoretical advantages of self-supervised graph condensation in noisy or weakly-labeled environments.

