---
layout: default
title: Condensation-Concatenation Framework for Dynamic Graph Continual Learning
---

# Condensation-Concatenation Framework for Dynamic Graph Continual Learning
**arXiv**：[2512.11317v1](https://arxiv.org/abs/2512.11317) · [PDF](https://arxiv.org/pdf/2512.11317.pdf)  
**作者**：Tingxu Yan, Ye Yuan  

**一句话要点**：提出Condensation-Concatenation框架以解决动态图持续学习中的灾难性遗忘问题

**关键词**：动态图持续学习, 灾难性遗忘, 图神经网络, 拓扑变化, 语义压缩, 遗忘度量

## 3 点简述
- 核心问题：动态图结构变化导致图神经网络对现有节点的灾难性遗忘
- 方法要点：通过压缩历史图快照为语义表示，并选择性拼接当前图表示
- 实验或效果：在四个真实数据集上优于现有基线，并改进了遗忘度量

## 摘要（原文）

> Dynamic graphs are prevalent in real-world scenarios, where continuous structural changes induce catastrophic forgetting in graph neural networks (GNNs). While continual learning has been extended to dynamic graphs, existing methods overlook the effects of topological changes on existing nodes. To address it, we propose a novel framework for continual learning on dynamic graphs, named Condensation-Concatenation-based Continual Learning (CCC). Specifically, CCC first condenses historical graph snapshots into compact semantic representations while aiming to preserve the original label distribution and topological properties. Then it concatenates these historical embeddings with current graph representations selectively. Moreover, we refine the forgetting measure (FM) to better adapt to dynamic graph scenarios by quantifying the predictive performance degradation of existing nodes caused by structural updates. CCC demonstrates superior performance over state-of-the-art baselines across four real-world datasets in extensive experiments.

