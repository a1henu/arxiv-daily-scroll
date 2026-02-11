---
layout: default
title: Diffusion-Guided Pretraining for Brain Graph Foundation Models
---

# Diffusion-Guided Pretraining for Brain Graph Foundation Models
**arXiv**：[2602.09437v1](https://arxiv.org/abs/2602.09437) · [PDF](https://arxiv.org/pdf/2602.09437.pdf)  
**作者**：Xinxu Wei, Rong Zhou, Lifang He, Yu Zhang  

**一句话要点**：提出扩散引导的预训练框架以解决脑图基础模型中的语义破坏和全局信息缺失问题。

**关键词**：脑图基础模型, 扩散引导预训练, 结构感知增强, 拓扑感知重建, 神经影像分析

## 3 点简述
- 核心问题：现有脑图预训练方法依赖随机丢弃或掩码，破坏语义连接模式，且图级读出和重建方案无法捕获全局结构信息。
- 方法要点：设计扩散引导的结构感知丢弃和掩码策略，并利用扩散实现拓扑感知的图级读出和节点级全局重建。
- 实验或效果：在超过25,000名受试者和60,000次扫描的神经影像数据集上验证，性能持续提升。

## 摘要（原文）

> With the growing interest in foundation models for brain signals, graph-based pretraining has emerged as a promising paradigm for learning transferable representations from connectome data. However, existing contrastive and masked autoencoder methods typically rely on naive random dropping or masking for augmentation, which is ill-suited for brain graphs and hypergraphs as it disrupts semantically meaningful connectivity patterns. Moreover, commonly used graph-level readout and reconstruction schemes fail to capture global structural information, limiting the robustness of learned representations. In this work, we propose a unified diffusion-based pretraining framework that addresses both limitations. First, diffusion is designed to guide structure-aware dropping and masking strategies, preserving brain graph semantics while maintaining effective pretraining diversity. Second, diffusion enables topology-aware graph-level readout and node-level global reconstruction by allowing graph embeddings and masked nodes to aggregate information from globally related regions. Extensive experiments across multiple neuroimaging datasets with over 25,000 subjects and 60,000 scans involving various mental disorders and brain atlases demonstrate consistent performance improvements.

