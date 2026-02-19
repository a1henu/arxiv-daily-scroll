---
layout: default
title: Parameter-free representations outperform single-cell foundation models on downstream benchmarks
---

# Parameter-free representations outperform single-cell foundation models on downstream benchmarks
**arXiv**：[2602.16696v1](https://arxiv.org/abs/2602.16696) · [PDF](https://arxiv.org/pdf/2602.16696.pdf)  
**作者**：Huan Souza, Pankaj Mehta  

**一句话要点**：提出参数无关表示方法，在单细胞下游基准上超越基础模型性能

**关键词**：单细胞RNA测序, 参数无关表示, 线性方法, 下游基准测试, 分布外泛化

## 3 点简述
- 核心问题：单细胞基础模型是否依赖复杂深度学习表示才能达到最优性能
- 方法要点：使用简单归一化和线性方法构建可解释表示，避免计算密集型深度学习
- 实验或效果：在多个基准测试中达到或接近SOTA，尤其在分布外任务上超越基础模型

## 摘要（原文）

> Single-cell RNA sequencing (scRNA-seq) data exhibit strong and reproducible statistical structure. This has motivated the development of large-scale foundation models, such as TranscriptFormer, that use transformer-based architectures to learn a generative model for gene expression by embedding genes into a latent vector space. These embeddings have been used to obtain state-of-the-art (SOTA) performance on downstream tasks such as cell-type classification, disease-state prediction, and cross-species learning. Here, we ask whether similar performance can be achieved without utilizing computationally intensive deep learning-based representations. Using simple, interpretable pipelines that rely on careful normalization and linear methods, we obtain SOTA or near SOTA performance across multiple benchmarks commonly used to evaluate single-cell foundation models, including outperforming foundation models on out-of-distribution tasks involving novel cell types and organisms absent from the training data. Our findings highlight the need for rigorous benchmarking and suggest that the biology of cell identity can be captured by simple linear representations of single cell gene expression data.

