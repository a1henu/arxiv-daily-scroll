---
layout: default
title: DIS2: Disentanglement Meets Distillation with Classwise Attention for Robust Remote Sensing Segmentation under Missing Modalities
---

# DIS2: Disentanglement Meets Distillation with Classwise Attention for Robust Remote Sensing Segmentation under Missing Modalities
**arXiv**：[2601.13502v1](https://arxiv.org/abs/2601.13502) · [PDF](https://arxiv.org/pdf/2601.13502.pdf)  
**作者**：Nhi Kieu, Kien Nguyen, Arnold Wiliem, Clinton Fookes, Sridha Sridharan  

**一句话要点**：提出DIS2方法，通过解耦与蒸馏结合及类特定注意力，解决遥感分割中模态缺失的鲁棒性问题。

**关键词**：遥感图像分割, 模态缺失处理, 解耦学习, 知识蒸馏, 类特定注意力, 多分辨率融合

## 3 点简述
- 核心问题：遥感数据异构且尺度多变，传统解耦学习和知识蒸馏在模态缺失时效果不佳。
- 方法要点：设计DLKD协同解耦与蒸馏，主动补偿缺失特征；CFLM模块学习类特定模态贡献；采用多分辨率融合增强预测。
- 实验或效果：在多个基准测试中显著优于现有方法，验证了方法的有效性。

## 摘要（原文）

> The efficacy of multimodal learning in remote sensing (RS) is severely undermined by missing modalities. The challenge is exacerbated by the RS highly heterogeneous data and huge scale variation. Consequently, paradigms proven effective in other domains often fail when confronted with these unique data characteristics. Conventional disentanglement learning, which relies on significant feature overlap between modalities (modality-invariant), is insufficient for this heterogeneity. Similarly, knowledge distillation becomes an ill-posed mimicry task where a student fails to focus on the necessary compensatory knowledge, leaving the semantic gap unaddressed. Our work is therefore built upon three pillars uniquely designed for RS: (1) principled missing information compensation, (2) class-specific modality contribution, and (3) multi-resolution feature importance. We propose a novel method DIS2, a new paradigm shifting from modality-shared feature dependence and untargeted imitation to active, guided missing features compensation. Its core novelty lies in a reformulated synergy between disentanglement learning and knowledge distillation, termed DLKD. Compensatory features are explicitly captured which, when fused with the features of the available modality, approximate the ideal fused representation of the full-modality case. To address the class-specific challenge, our Classwise Feature Learning Module (CFLM) adaptively learn discriminative evidence for each target depending on signal availability. Both DLKD and CFLM are supported by a hierarchical hybrid fusion (HF) structure using features across resolutions to strengthen prediction. Extensive experiments validate that our proposed approach significantly outperforms state-of-the-art methods across benchmarks.

