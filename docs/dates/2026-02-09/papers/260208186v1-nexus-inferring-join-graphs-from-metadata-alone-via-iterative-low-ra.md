---
layout: default
title: Nexus: Inferring Join Graphs from Metadata Alone via Iterative Low-Rank Matrix Completion
---

# Nexus: Inferring Join Graphs from Metadata Alone via Iterative Low-Rank Matrix Completion
**arXiv**：[2602.08186v1](https://arxiv.org/abs/2602.08186) · [PDF](https://arxiv.org/pdf/2602.08186.pdf)  
**作者**：Tianji Cong, Yuanyuan Tian, Andreas Mueller, Rathijit Sen, Yeye He, Fotis Psallidas, Shaleen Deep, H. V. Jagadish  

**一句话要点**：提出Nexus通过低秩矩阵补全从元数据推断连接图，解决企业数据发现中的连接关系识别问题。

**关键词**：连接图推断, 低秩矩阵补全, 元数据分析, 数据发现, 企业数据管理

## 3 点简述
- 核心问题：在仅元数据可用时，自动推断大型复杂模式中的连接关系，以支持数据发现与集成。
- 方法要点：基于连接图的高稀疏性和低秩性，将问题建模为低秩矩阵补全，并引入EM算法结合LLM优化候选概率。
- 实验或效果：在四个数据集上显著优于现有方法，快速模式可提速6倍，提供实用高效的部署方案。

## 摘要（原文）

> Automatically inferring join relationships is a critical task for effective data discovery, integration, querying and reuse. However, accurately and efficiently identifying these relationships in large and complex schemas can be challenging, especially in enterprise settings where access to data values is constrained. In this paper, we introduce the problem of join graph inference when only metadata is available. We conduct an empirical study on a large number of real-world schemas and observe that join graphs when represented as adjacency matrices exhibit two key properties: high sparsity and low-rank structure. Based on these novel observations, we formulate join graph inference as a low-rank matrix completion problem and propose Nexus, an end-to-end solution using only metadata. To further enhance accuracy, we propose a novel Expectation-Maximization algorithm that alternates between low-rank matrix completion and refining join candidate probabilities by leveraging Large Language Models. Our extensive experiments demonstrate that Nexus outperforms existing methods by a significant margin on four datasets including a real-world production dataset. Additionally, Nexus can operate in a fast mode, providing comparable results with up to 6x speedup, offering a practical and efficient solution for real-world deployments.

