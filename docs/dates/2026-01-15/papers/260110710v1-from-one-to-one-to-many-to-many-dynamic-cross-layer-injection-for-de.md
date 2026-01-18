---
layout: default
title: From One-to-One to Many-to-Many: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion
---

# From One-to-One to Many-to-Many: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion
**arXiv**：[2601.10710v1](https://arxiv.org/abs/2601.10710) · [PDF](https://arxiv.org/pdf/2601.10710.pdf)  
**作者**：Cheng Chen, Yuyu Guo, Pengpeng Zeng, Jingkuan Song, Peng Di, Hang Yu, Lianli Gao  

**一句话要点**：提出动态跨层注入框架以解决视觉语言模型中视觉特征瓶颈问题

**关键词**：视觉语言模型, 跨层注入, 动态融合, 参数高效, 多模态理解, 自适应门控

## 3 点简述
- 核心问题：现有视觉语言模型采用静态单层连接，限制语言模型与分层视觉知识的全面对齐，影响细节与语义的整合推理。
- 方法要点：引入跨层注入框架，包含自适应多投影模块和自适应门控融合机制，实现视觉与语言间的动态多对多桥接。
- 实验或效果：在LLaVA-OneVision和LLaVA-1.5中集成，18个基准测试显示性能显著提升，验证了框架的有效性和可扩展性。

## 摘要（原文）

> Vision-Language Models (VLMs) create a severe visual feature bottleneck by using a crude, asymmetric connection that links only the output of the vision encoder to the input of the large language model (LLM). This static architecture fundamentally limits the ability of LLMs to achieve comprehensive alignment with hierarchical visual knowledge, compromising their capacity to accurately integrate local details with global semantics into coherent reasoning. To resolve this, we introduce Cross-Layer Injection (CLI), a novel and lightweight framework that forges a dynamic many-to-many bridge between the two modalities. CLI consists of two synergistic, parameter-efficient components: an Adaptive Multi-Projection (AMP) module that harmonizes features from diverse vision layers, and an Adaptive Gating Fusion (AGF) mechanism that empowers the LLM to selectively inject the most relevant visual information based on its real-time decoding context. We validate the effectiveness and versatility of CLI by integrating it into LLaVA-OneVision and LLaVA-1.5. Extensive experiments on 18 diverse benchmarks demonstrate significant performance improvements, establishing CLI as a scalable paradigm that unlocks deeper multimodal understanding by granting LLMs on-demand access to the full visual hierarchy.

