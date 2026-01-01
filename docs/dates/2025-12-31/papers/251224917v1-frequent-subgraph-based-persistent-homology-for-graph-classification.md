---
layout: default
title: Frequent subgraph-based persistent homology for graph classification
---

# Frequent subgraph-based persistent homology for graph classification
**arXiv**：[2512.24917v1](https://arxiv.org/abs/2512.24917) · [PDF](https://arxiv.org/pdf/2512.24917.pdf)  
**作者**：Xinyang Chen, Amaël Broustet, Guoting Chen  

**一句话要点**：提出频繁子图过滤以增强图分类中的拓扑特征提取

**关键词**：持久同调, 频繁子图挖掘, 图分类, 拓扑数据分析, 图神经网络, 特征提取

## 3 点简述
- 问题：现有图持久同调方法依赖有限过滤，忽略数据集中的重复信息，限制表达能力。
- 方法：引入频繁子图过滤，生成稳定且信息丰富的频率基持久同调特征，并集成到机器学习和图神经网络中。
- 效果：实验显示FPH-ML达到竞争性或更优准确率，FPH-GNN在基准测试中相对性能提升最高达21%。

## 摘要（原文）

> Persistent homology (PH) has recently emerged as a powerful tool for extracting topological features. Integrating PH into machine learning and deep learning models enhances topology awareness and interpretability. However, most PH methods on graphs rely on a limited set of filtrations, such as degree-based or weight-based filtrations, which overlook richer features like recurring information across the dataset and thus restrict expressive power. In this work, we propose a novel graph filtration called Frequent Subgraph Filtration (FSF), which is derived from frequent subgraphs and produces stable and information-rich frequency-based persistent homology (FPH) features. We study the theoretical properties of FSF and provide both proofs and experimental validation. Beyond persistent homology itself, we introduce two approaches for graph classification: an FPH-based machine learning model (FPH-ML) and a hybrid framework that integrates FPH with graph neural networks (FPH-GNNs) to enhance topology-aware graph representation learning. Our frameworks bridge frequent subgraph mining and topological data analysis, offering a new perspective on topology-aware feature extraction. Experimental results show that FPH-ML achieves competitive or superior accuracy compared with kernel-based and degree-based filtration methods. When integrated into graph neural networks, FPH yields relative performance gains ranging from 0.4 to 21 percent, with improvements of up to 8.2 percentage points over GCN and GIN backbones across benchmarks.

