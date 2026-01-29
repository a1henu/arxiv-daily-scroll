---
layout: default
title: Graph-Structured Deep Learning Framework for Multi-task Contention Identification with High-dimensional Metrics
---

# Graph-Structured Deep Learning Framework for Multi-task Contention Identification with High-dimensional Metrics
**arXiv**：[2601.20389v1](https://arxiv.org/abs/2601.20389) · [PDF](https://arxiv.org/pdf/2601.20389.pdf)  
**作者**：Xiao Yang, Yinan Ni, Yuqi Tang, Zhimin Qiu, Chen Wang, Tingzhou Yuan  

**一句话要点**：提出基于图结构深度学习的多任务争用识别框架，以解决高维系统环境中的争用类型分类问题。

**关键词**：多任务争用识别, 图结构深度学习, 高维系统度量, 表示学习, 性能管理

## 3 点简述
- 核心问题：高维系统环境中多任务争用类型的准确识别挑战。
- 方法要点：集成表示变换、图结构建模和任务解耦机制的统一分类框架。
- 实验或效果：在公开数据集上验证了准确性、召回率等优势，并分析了模型稳定性。

## 摘要（原文）

> This study addresses the challenge of accurately identifying multi-task contention types in high-dimensional system environments and proposes a unified contention classification framework that integrates representation transformation, structural modeling, and a task decoupling mechanism. The method first constructs system state representations from high-dimensional metric sequences, applies nonlinear transformations to extract cross-dimensional dynamic features, and integrates multiple source information such as resource utilization, scheduling behavior, and task load variations within a shared representation space. It then introduces a graph-based modeling mechanism to capture latent dependencies among metrics, allowing the model to learn competitive propagation patterns and structural interference across resource links. On this basis, task-specific mapping structures are designed to model the differences among contention types and enhance the classifier's ability to distinguish multiple contention patterns. To achieve stable performance, the method employs an adaptive multi-task loss weighting strategy that balances shared feature learning with task-specific feature extraction and generates final contention predictions through a standardized inference process. Experiments conducted on a public system trace dataset demonstrate advantages in accuracy, recall, precision, and F1, and sensitivity analyses on batch size, training sample scale, and metric dimensionality further confirm the model's stability and applicability. The study shows that structured representations and multi-task classification based on high-dimensional metrics can significantly improve contention pattern recognition and offer a reliable technical approach for performance management in complex computing environments.

