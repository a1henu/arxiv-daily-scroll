---
layout: default
title: Towards Single-Source Domain Generalized Object Detection via Causal Visual Prompts
---

# Towards Single-Source Domain Generalized Object Detection via Causal Visual Prompts
**arXiv**：[2510.19487v1](https://arxiv.org/abs/2510.19487) · [PDF](https://arxiv.org/pdf/2510.19487.pdf)  
**作者**：Chen Li, Huiying Xu, Changxin Gao, Zeyu Wang, Yun Liu, Xinzhong Zhu  

**一句话要点**：提出Cauvis方法以解决单源域泛化目标检测中的伪相关性问题

**关键词**：单源域泛化目标检测, 因果视觉提示, 跨注意力机制, 特征解耦, 高频特征提取, 鲁棒性增强

## 3 点简述
- 核心问题：模型在单源域训练中易陷入伪相关，过度依赖颜色等浅层特征而非轮廓等不变表示。
- 方法要点：引入跨注意力提示模块和双分支适配器，解耦因果-伪特征并提取高频特征实现域适应。
- 实验或效果：在SDGOD数据集上性能提升15.9-31.4%，并在复杂干扰环境中展现强鲁棒性。

## 摘要（原文）

> Single-source Domain Generalized Object Detection (SDGOD), as a cutting-edge
> research topic in computer vision, aims to enhance model generalization
> capability in unseen target domains through single-source domain training.
> Current mainstream approaches attempt to mitigate domain discrepancies via data
> augmentation techniques. However, due to domain shift and limited
> domain-specific knowledge, models tend to fall into the pitfall of spurious
> correlations. This manifests as the model's over-reliance on simplistic
> classification features (e.g., color) rather than essential domain-invariant
> representations like object contours. To address this critical challenge, we
> propose the Cauvis (Causal Visual Prompts) method. First, we introduce a
> Cross-Attention Prompts module that mitigates bias from spurious features by
> integrating visual prompts with cross-attention. To address the inadequate
> domain knowledge coverage and spurious feature entanglement in visual prompts
> for single-domain generalization, we propose a dual-branch adapter that
> disentangles causal-spurious features while achieving domain adaptation via
> high-frequency feature extraction. Cauvis achieves state-of-the-art performance
> with 15.9-31.4% gains over existing domain generalization methods on SDGOD
> datasets, while exhibiting significant robustness advantages in complex
> interference environments.

