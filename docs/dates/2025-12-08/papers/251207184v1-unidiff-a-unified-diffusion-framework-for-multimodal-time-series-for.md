---
layout: default
title: UniDiff: A Unified Diffusion Framework for Multimodal Time Series Forecasting
---

# UniDiff: A Unified Diffusion Framework for Multimodal Time Series Forecasting
**arXiv**：[2512.07184v1](https://arxiv.org/abs/2512.07184) · [PDF](https://arxiv.org/pdf/2512.07184.pdf)  
**作者**：Da Zhang, Bingyu Li, Zhuyuan Zhao, Junyu Gao, Feiping Nie, Xuelong Li  

**一句话要点**：提出UniDiff统一扩散框架以解决多模态时间序列预测中异构信息融合的挑战

**关键词**：多模态时间序列预测, 扩散模型, 异构信息融合, 交叉注意力机制, 分类器自由引导

## 3 点简述
- 核心问题：现有扩散模型在时间序列预测中多局限于单模态数值序列，忽略文本和时间戳等异构跨模态信号。
- 方法要点：通过统一并行融合模块，使用单交叉注意力机制一步整合时间戳结构信息和文本语义上下文，并引入多源条件分类器自由引导机制。
- 实验或效果：在八个领域的真实世界基准数据集上广泛实验，UniDiff实现了最先进的性能。

## 摘要（原文）

> As multimodal data proliferates across diverse real-world applications, leveraging heterogeneous information such as texts and timestamps for accurate time series forecasting (TSF) has become a critical challenge. While diffusion models demonstrate exceptional performance in generation tasks, their application to TSF remains largely confined to modeling single-modality numerical sequences, overlooking the abundant cross-modal signals inherent in complex heterogeneous data. To address this gap, we propose UniDiff, a unified diffusion framework for multimodal time series forecasting. To process the numerical sequence, our framework first tokenizes the time series into patches, preserving local temporal dynamics by mapping each patch to an embedding space via a lightweight MLP. At its core lies a unified and parallel fusion module, where a single cross-attention mechanism adaptively weighs and integrates structural information from timestamps and semantic context from texts in one step, enabling a flexible and efficient interplay between modalities. Furthermore, we introduce a novel classifier-free guidance mechanism designed for multi-source conditioning, allowing for decoupled control over the guidance strength of textual and temporal information during inference, which significantly enhances model robustness. Extensive experiments on real-world benchmark datasets across eight domains demonstrate that the proposed UniDiff model achieves state-of-the-art performance.

