---
layout: default
title: Plug, Play, and Fortify: A Low-Cost Module for Robust Multimodal Image Understanding Models
---

# Plug, Play, and Fortify: A Low-Cost Module for Robust Multimodal Image Understanding Models
**arXiv**：[2602.22644v1](https://arxiv.org/abs/2602.22644) · [PDF](https://arxiv.org/pdf/2602.22644.pdf)  
**作者**：Siqi Lu, Wanying Xu, Yongbin Zheng, Wenting Luan, Peng Sun, Jianhang Yao  

**一句话要点**：提出多模态权重分配模块以解决模态缺失导致的性能下降问题

**关键词**：多模态学习, 模态缺失, 频域分析, 权重分配, 鲁棒性增强

## 3 点简述
- 核心问题：模态缺失导致多模态模型性能崩溃，源于模态间学习不平衡
- 方法要点：在频域量化模态偏好，通过动态权重分配模块平衡各分支贡献
- 实验或效果：模块可集成于CNN和ViT等架构，在多种任务中提升性能

## 摘要（原文）

> Missing modalities present a fundamental challenge in multimodal models, often causing catastrophic performance degradation. Our observations suggest that this fragility stems from an imbalanced learning process, where the model develops an implicit preference for certain modalities, leading to the under-optimization of others. We propose a simple yet efficient method to address this challenge. The central insight of our work is that the dominance relationship between modalities can be effectively discerned and quantified in the frequency domain. To leverage this principle, we first introduce a Frequency Ratio Metric (FRM) to quantify modality preference by analyzing features in the frequency domain. Guided by FRM, we then propose a Multimodal Weight Allocation Module, a plug-and-play component that dynamically re-balances the contribution of each branch during training, promoting a more holistic learning paradigm. Extensive experiments demonstrate that MWAM can be seamlessly integrated into diverse architectural backbones, such as those based on CNNs and ViTs. Furthermore, MWAM delivers consistent performance gains across a wide range of tasks and modality combinations. This advancement extends beyond merely optimizing the performance of the base model; it also manifests as further performance improvements to state-of-the-art methods addressing the missing modality problem.

