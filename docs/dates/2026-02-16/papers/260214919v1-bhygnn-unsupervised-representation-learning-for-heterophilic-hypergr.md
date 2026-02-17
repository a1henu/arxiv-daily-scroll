---
layout: default
title: BHyGNN+: Unsupervised Representation Learning for Heterophilic Hypergraphs
---

# BHyGNN+: Unsupervised Representation Learning for Heterophilic Hypergraphs
**arXiv**：[2602.14919v1](https://arxiv.org/abs/2602.14919) · [PDF](https://arxiv.org/pdf/2602.14919.pdf)  
**作者**：Tianyi Ma, Yiyue Qian, Zehong Wang, Zheyuan Zhang, Chuxu Zhang, Yanfang Ye  

**一句话要点**：提出BHyGNN+，基于超图对偶的自监督框架，用于无标签异配超图表示学习。

**关键词**：超图神经网络, 异配超图, 自监督学习, 超图对偶, 表示学习, 无标签学习

## 3 点简述
- 核心问题：现有超图神经网络依赖标注数据，在异配超图上性能受限，难以处理无标签场景。
- 方法要点：利用超图对偶结构，通过对比原始超图与其对偶的增强视图，无需负样本，实现无监督表示学习。
- 实验或效果：在11个基准数据集上，BHyGNN+优于监督和自监督基线，验证了对偶方法的有效性。

## 摘要（原文）

> Hypergraph Neural Networks (HyGNNs) have demonstrated remarkable success in modeling higher-order relationships among entities. However, their performance often degrades on heterophilic hypergraphs, where nodes connected by the same hyperedge tend to have dissimilar semantic representations or belong to different classes. While several HyGNNs, including our prior work BHyGNN, have been proposed to address heterophily, their reliance on labeled data significantly limits their applicability in real-world scenarios where annotations are scarce or costly. To overcome this limitation, we introduce BHyGNN+, a self-supervised learning framework that extends BHyGNN for representation learning on heterophilic hypergraphs without requiring ground-truth labels. The core idea of BHyGNN+ is hypergraph duality, a structural transformation where the roles of nodes and hyperedges are interchanged. By contrasting augmented views of a hypergraph against its dual using cosine similarity, our framework captures essential structural patterns in a fully unsupervised manner. Notably, this duality-based formulation eliminates the need for negative samples, a common requirement in existing hypergraph contrastive learning methods that is often difficult to satisfy in practice. Extensive experiments on eleven benchmark datasets demonstrate that BHyGNN+ consistently outperforms state-of-the-art supervised and self-supervised baselines on both heterophilic and homophilic hypergraphs. Our results validate the effectiveness of leveraging hypergraph duality for self-supervised learning and establish a new paradigm for representation learning on challenging, unlabeled hypergraphs.

