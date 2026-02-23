---
layout: default
title: Temporal Consistency-Aware Text-to-Motion Generation
---

# Temporal Consistency-Aware Text-to-Motion Generation
**arXiv**：[2602.18057v1](https://arxiv.org/abs/2602.18057) · [PDF](https://arxiv.org/pdf/2602.18057.pdf)  
**作者**：Hongsong Wang, Wenjing Yan, Qiuxia Lai, Xin Geng  

**一句话要点**：提出TCA-T2M框架，通过跨序列时序对齐解决文本到动作生成中的时序一致性问题

**关键词**：文本到动作生成, 时序一致性, VQ-VAE, 运动学约束, 动作合成

## 3 点简述
- 核心问题：现有两阶段文本到动作生成方法忽视跨序列时序一致性，导致语义错位和物理不合理动作
- 方法要点：引入时序一致性感知空间VQ-VAE进行跨序列对齐，结合掩码动作Transformer和运动学约束模块
- 实验效果：在HumanML3D和KIT-ML基准测试中达到最先进性能，验证时序一致性的重要性

## 摘要（原文）

> Text-to-Motion (T2M) generation aims to synthesize realistic human motion sequences from natural language descriptions. While two-stage frameworks leveraging discrete motion representations have advanced T2M research, they often neglect cross-sequence temporal consistency, i.e., the shared temporal structures present across different instances of the same action. This leads to semantic misalignments and physically implausible motions. To address this limitation, we propose TCA-T2M, a framework for temporal consistency-aware T2M generation. Our approach introduces a temporal consistency-aware spatial VQ-VAE (TCaS-VQ-VAE) for cross-sequence temporal alignment, coupled with a masked motion transformer for text-conditioned motion generation. Additionally, a kinematic constraint block mitigates discretization artifacts to ensure physical plausibility. Experiments on HumanML3D and KIT-ML benchmarks demonstrate that TCA-T2M achieves state-of-the-art performance, highlighting the importance of temporal consistency in robust and coherent T2M generation.

