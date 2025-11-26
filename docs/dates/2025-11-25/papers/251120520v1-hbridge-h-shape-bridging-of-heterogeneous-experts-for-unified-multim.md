---
layout: default
title: HBridge: H-Shape Bridging of Heterogeneous Experts for Unified Multimodal Understanding and Generation
---

# HBridge: H-Shape Bridging of Heterogeneous Experts for Unified Multimodal Understanding and Generation
**arXiv**：[2511.20520v1](https://arxiv.org/abs/2511.20520) · [PDF](https://arxiv.org/pdf/2511.20520.pdf)  
**作者**：Xiang Wang, Zhifei Zhang, He Zhang, Zhe Lin, Yuqian Zhou, Qing Liu, Shiwei Zhang, Yijun Li, Shaoteng Liu, Haitian Zheng, Jason Kuen, Yuehuan Wang, Changxin Gao, Nong Sang  

**一句话要点**：提出HBridge以解决异构专家融合中的模态差异问题

**关键词**：多模态理解, 异构专家融合, 非对称架构, 注意力共享优化, 语义对齐

## 3 点简述
- 核心问题：对称设计在统一多模态模型中导致模态差异，影响性能。
- 方法要点：采用非对称H形架构，选择性桥接中间层，减少注意力共享。
- 实验或效果：在多个基准测试中表现优越，提升生成质量和效率。

## 摘要（原文）

> Recent unified models integrate understanding experts (e.g., LLMs) with generative experts (e.g., diffusion models), achieving strong multimodal performance. However, recent advanced methods such as BAGEL and LMFusion follow the Mixture-of-Transformers (MoT) paradigm, adopting a symmetric design that mirrors one expert to another for convenient initialization and fusion, which remains suboptimal due to inherent modality discrepancies. In this work, we propose HBridge, an asymmetric H-shaped architecture that enables heterogeneous experts to optimally leverage pretrained priors from their respective modality domains. Unlike prior dense fusion strategies that straightforwardly connect all layers between experts via shared attention, HBridge selectively bridges intermediate layers, reducing over 40% attention sharing, which improves efficiency and enhances generation quality. Shallow and deep layers, which capture modality-specific representations, are decoupled, while mid-layer bridging promotes semantic alignment. To further strengthen cross-modal coherence, we introduce semantic reconstruction tokens that explicitly guide the generative expert to reconstruct visual semantic tokens of the target image. Extensive experiments across multiple benchmarks demonstrate the effectiveness and superior performance of HBridge, establishing a new paradigm for unified multimodal generation.

