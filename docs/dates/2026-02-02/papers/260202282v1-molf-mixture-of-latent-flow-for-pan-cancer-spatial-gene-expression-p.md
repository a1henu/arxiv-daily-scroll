---
layout: default
title: MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology
---

# MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology
**arXiv**：[2602.02282v1](https://arxiv.org/abs/2602.02282) · [PDF](https://arxiv.org/pdf/2602.02282.pdf)  
**作者**：Susu Hu, Stefanie Speidel  

**一句话要点**：提出MoLF模型以解决跨癌症类型空间基因表达预测中的异质性问题

**关键词**：空间转录组学, 跨癌症预测, 生成模型, 条件流匹配, 混合专家, 零样本泛化

## 3 点简述
- 核心问题：现有方法局限于单组织模型，无法利用跨癌症类型的共享生物学原理，且数据稀缺场景应用受限。
- 方法要点：采用条件流匹配目标，通过混合专家速度场参数化，动态路由输入到专门子网络，解耦优化多样组织模式。
- 实验或效果：在跨癌症基准测试中优于专业和基础模型基线，并展示零样本跨物种泛化能力。

## 摘要（原文）

> Inferring spatial transcriptomics (ST) from histology enables scalable histogenomic profiling, yet current methods are largely restricted to single-tissue models. This fragmentation fails to leverage biological principles shared across cancer types and hinders application to data-scarce scenarios. While pan-cancer training offers a solution, the resulting heterogeneity challenges monolithic architectures. To bridge this gap, we introduce MoLF (Mixture-of-Latent-Flow), a generative model for pan-cancer histogenomic prediction. MoLF leverages a conditional Flow Matching objective to map noise to the gene latent manifold, parameterized by a Mixture-of-Experts (MoE) velocity field. By dynamically routing inputs to specialized sub-networks, this architecture effectively decouples the optimization of diverse tissue patterns. Our experiments demonstrate that MoLF establishes a new state-of-the-art, consistently outperforming both specialized and foundation model baselines on pan-cancer benchmarks. Furthermore, MoLF exhibits zero-shot generalization to cross-species data, suggesting it captures fundamental, conserved histo-molecular mechanisms.

