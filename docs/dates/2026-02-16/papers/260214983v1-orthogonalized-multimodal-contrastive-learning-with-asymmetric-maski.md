---
layout: default
title: Orthogonalized Multimodal Contrastive Learning with Asymmetric Masking for Structured Representations
---

# Orthogonalized Multimodal Contrastive Learning with Asymmetric Masking for Structured Representations
**arXiv**：[2602.14983v1](https://arxiv.org/abs/2602.14983) · [PDF](https://arxiv.org/pdf/2602.14983.pdf)  
**作者**：Carolin Cissee, Raneen Younis, Zahra Ahmadi  

**一句话要点**：提出COrAL框架，通过正交约束和不对称掩码解决多模态学习中冗余、独特和协同信息建模不足的问题。

**关键词**：多模态学习, 对比学习, 正交约束, 不对称掩码, 信息分离, 协同建模

## 3 点简述
- 核心问题：现有多模态对比学习方法主要捕获冗余跨模态信号，忽视模态独特和协同信息，导致表示不完整。
- 方法要点：采用双路径架构和正交约束分离共享与模态特定特征，引入不对称掩码强制模型推断跨模态依赖。
- 实验或效果：在合成基准和MultiBench数据集上匹配或超越先进方法，表现稳定且方差低，验证了全面建模的有效性。

## 摘要（原文）

> Multimodal learning seeks to integrate information from heterogeneous sources, where signals may be shared across modalities, specific to individual modalities, or emerge only through their interaction. While self-supervised multimodal contrastive learning has achieved remarkable progress, most existing methods predominantly capture redundant cross-modal signals, often neglecting modality-specific (unique) and interaction-driven (synergistic) information. Recent extensions broaden this perspective, yet they either fail to explicitly model synergistic interactions or learn different information components in an entangled manner, leading to incomplete representations and potential information leakage. We introduce \textbf{COrAL}, a principled framework that explicitly and simultaneously preserves redundant, unique, and synergistic information within multimodal representations. COrAL employs a dual-path architecture with orthogonality constraints to disentangle shared and modality-specific features, ensuring a clean separation of information components. To promote synergy modeling, we introduce asymmetric masking with complementary view-specific patterns, compelling the model to infer cross-modal dependencies rather than rely solely on redundant cues. Extensive experiments on synthetic benchmarks and diverse MultiBench datasets demonstrate that COrAL consistently matches or outperforms state-of-the-art methods while exhibiting low performance variance across runs. These results indicate that explicitly modeling the full spectrum of multimodal information yields more stable, reliable, and comprehensive embeddings.

