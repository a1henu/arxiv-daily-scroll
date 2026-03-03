---
layout: default
title: What Helps -- and What Hurts: Bidirectional Explanations for Vision Transformers
---

# What Helps -- and What Hurts: Bidirectional Explanations for Vision Transformers
**arXiv**：[2603.01605v1](https://arxiv.org/abs/2603.01605) · [PDF](https://arxiv.org/pdf/2603.01605.pdf)  
**作者**：Qin Su, Tie Luo  

**一句话要点**：提出BiCAM方法以解释Vision Transformers的决策，通过双向类激活映射捕获正负贡献。

**关键词**：Vision Transformers解释, 双向类激活映射, 正负归因, 对抗样本检测, 模型可解释性

## 3 点简述
- 核心问题：Vision Transformers决策难以解释，现有方法忽略负信号。
- 方法要点：BiCAM保留有符号归因，引入正负比总结归因平衡，支持对抗样本检测。
- 实验或效果：在ImageNet等数据集上提升定位和忠实度，适用于DeiT和Swin等变体。

## 摘要（原文）

> Vision Transformers (ViTs) achieve strong performance in visual recognition, yet their decision-making remains difficult to interpret. We propose BiCAM, a bidirectional class activation mapping method that captures both supportive (positive) and suppressive (negative) contributions to model predictions. Unlike prior CAM-based approaches that discard negative signals, BiCAM preserves signed attributions to produce more complete and contrastive explanations. BiCAM further introduces a Positive-to-Negative Ratio (PNR) that summarizes attribution balance and enables lightweight detection of adversarial examples without retraining. Across ImageNet, VOC, and COCO, BiCAM improves localization and faithfulness while remaining computationally efficient. It generalizes to multiple ViT variants, including DeiT and Swin. These results suggest the importance of modeling both supportive and suppressive evidence for interpreting transformer-based vision models.

