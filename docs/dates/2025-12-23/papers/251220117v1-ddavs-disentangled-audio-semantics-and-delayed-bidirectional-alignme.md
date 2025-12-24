---
layout: default
title: DDAVS: Disentangled Audio Semantics and Delayed Bidirectional Alignment for Audio-Visual Segmentation
---

# DDAVS: Disentangled Audio Semantics and Delayed Bidirectional Alignment for Audio-Visual Segmentation
**arXiv**：[2512.20117v1](https://arxiv.org/abs/2512.20117) · [PDF](https://arxiv.org/pdf/2512.20117.pdf)  
**作者**：Jingqi Tian, Yiheng Du, Haoji Zhang, Yuji Wang, Isaac Ning Lee, Xulong Bai, Tianrui Zhu, Jingxuan Niu, Yansong Tang  

**一句话要点**：提出DDAVS框架，通过解耦音频语义和延迟双向对齐解决音频-视觉分割中的多源纠缠和模态错位问题。

**关键词**：音频-视觉分割, 多模态对齐, 语义解耦, 对比学习, 延迟交互, 原型记忆

## 3 点简述
- 核心问题：现有方法存在多源纠缠和音频-视觉错位，导致偏向响亮或大物体，忽略弱、小或共现声源。
- 方法要点：使用可学习查询提取音频语义，结合音频原型记忆库和对比学习优化；引入延迟模态交互的双重交叉注意力改善对齐鲁棒性。
- 实验或效果：在AVS-Objects和VPO基准上优于现有方法，在单源、多源和多实例场景中表现强健，验证了框架的有效性和泛化能力。

## 摘要（原文）

> Audio-Visual Segmentation (AVS) aims to localize sound-producing objects at the pixel level by jointly leveraging auditory and visual information. However, existing methods often suffer from multi-source entanglement and audio-visual misalignment, which lead to biases toward louder or larger objects while overlooking weaker, smaller, or co-occurring sources. To address these challenges, we propose DDAVS, a Disentangled Audio Semantics and Delayed Bidirectional Alignment framework. To mitigate multi-source entanglement, DDAVS employs learnable queries to extract audio semantics and anchor them within a structured semantic space derived from an audio prototype memory bank. This is further optimized through contrastive learning to enhance discriminability and robustness. To alleviate audio-visual misalignment, DDAVS introduces dual cross-attention with delayed modality interaction, improving the robustness of multimodal alignment. Extensive experiments on the AVS-Objects and VPO benchmarks demonstrate that DDAVS consistently outperforms existing approaches, exhibiting strong performance across single-source, multi-source, and multi-instance scenarios. These results validate the effectiveness and generalization ability of our framework under challenging real-world audio-visual segmentation conditions. Project page: https://trilarflagz.github.io/DDAVS-page/

