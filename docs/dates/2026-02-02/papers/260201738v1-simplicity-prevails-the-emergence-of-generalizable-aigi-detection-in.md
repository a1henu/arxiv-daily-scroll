---
layout: default
title: Simplicity Prevails: The Emergence of Generalizable AIGI Detection in Visual Foundation Models
---

# Simplicity Prevails: The Emergence of Generalizable AIGI Detection in Visual Foundation Models
**arXiv**：[2602.01738v1](https://arxiv.org/abs/2602.01738) · [PDF](https://arxiv.org/pdf/2602.01738.pdf)  
**作者**：Yue Zhou, Xinan He, Kaiqing Lin, Bing Fan, Feng Ding, Bin Li  

**一句话要点**：提出基于视觉基础模型冻结特征的线性分类器，实现AIGI检测在真实场景中的泛化性能提升

**关键词**：AI生成图像检测, 视觉基础模型, 线性分类器, 泛化性能, 真实场景评估, 数据暴露

## 3 点简述
- 核心问题：专用AIGI检测器在真实场景中性能崩溃，泛化能力不足
- 方法要点：使用现代视觉基础模型的冻结特征训练简单线性分类器，避免复杂架构
- 实验或效果：在真实数据集上准确率提升超30%，超越专用检测器，但存在重捕获和传输等局限性

## 摘要（原文）

> While specialized detectors for AI-Generated Images (AIGI) achieve near-perfect accuracy on curated benchmarks, they suffer from a dramatic performance collapse in realistic, in-the-wild scenarios. In this work, we demonstrate that simplicity prevails over complex architectural designs. A simple linear classifier trained on the frozen features of modern Vision Foundation Models , including Perception Encoder, MetaCLIP 2, and DINOv3, establishes a new state-of-the-art. Through a comprehensive evaluation spanning traditional benchmarks, unseen generators, and challenging in-the-wild distributions, we show that this baseline not only matches specialized detectors on standard benchmarks but also decisively outperforms them on in-the-wild datasets, boosting accuracy by striking margins of over 30\%. We posit that this superior capability is an emergent property driven by the massive scale of pre-training data containing synthetic content. We trace the source of this capability to two distinct manifestations of data exposure: Vision-Language Models internalize an explicit semantic concept of forgery, while Self-Supervised Learning models implicitly acquire discriminative forensic features from the pretraining data. However, we also reveal persistent limitations: these models suffer from performance degradation under recapture and transmission, remain blind to VAE reconstruction and localized editing. We conclude by advocating for a paradigm shift in AI forensics, moving from overfitting on static benchmarks to harnessing the evolving world knowledge of foundation models for real-world reliability.

