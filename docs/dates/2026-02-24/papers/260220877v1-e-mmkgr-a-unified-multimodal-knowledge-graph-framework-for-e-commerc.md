---
layout: default
title: E-MMKGR: A Unified Multimodal Knowledge Graph Framework for E-commerce Applications
---

# E-MMKGR: A Unified Multimodal Knowledge Graph Framework for E-commerce Applications
**arXiv**：[2602.20877v1](https://arxiv.org/abs/2602.20877) · [PDF](https://arxiv.org/pdf/2602.20877.pdf)  
**作者**：Jiwoo Kang, Yeon-Chang Lee  

**一句话要点**：提出E-MMKGR框架，构建电商多模态知识图谱以提升推荐和搜索任务性能。

**关键词**：多模态知识图谱, 图神经网络, 电商推荐, 统一表示学习, 模态扩展性

## 3 点简述
- 核心问题：多模态推荐系统依赖固定模态和任务特定目标，限制模态扩展性和任务泛化性。
- 方法要点：通过构建电商多模态知识图谱，利用GNN传播和知识图谱优化学习统一物品表示。
- 实验或效果：在亚马逊数据集上，推荐任务Recall@10提升达10.18%，产品搜索优于向量检索达21.72%。

## 摘要（原文）

> Multimodal recommender systems (MMRSs) enhance collaborative filtering by leveraging item-side modalities, but their reliance on a fixed set of modalities and task-specific objectives limits both modality extensibility and task generalization. We propose E-MMKGR, a framework that constructs an e-commerce-specific Multimodal Knowledge Graph E-MMKG and learns unified item representations through GNN-based propagation and KG-oriented optimization. These representations provide a shared semantic foundation applicable to diverse tasks. Experiments on real-world Amazon datasets show improvements of up to 10.18% in Recall@10 for recommendation and up to 21.72% over vector-based retrieval for product search, demonstrating the effectiveness and extensibility of our approach.

