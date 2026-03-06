---
layout: default
title: Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model
---

# Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model
**arXiv**：[2603.05012v1](https://arxiv.org/abs/2603.05012) · [PDF](https://arxiv.org/pdf/2603.05012.pdf)  
**作者**：Yulong Shi, Shijie Li, Ziyi Li, Lin Qi  

**一句话要点**：提出Tell2Adapt框架，利用视觉基础模型解决源自由无监督域适应在医学图像分割中的统一多目标问题。

**关键词**：源自由无监督域适应, 视觉基础模型, 医学图像分割, 多目标域适应, 伪标签生成, 上下文感知提示

## 3 点简述
- 核心问题：现有源自由无监督域适应方法难以处理多模态、多目标的统一框架，限制临床部署。
- 方法要点：通过上下文感知提示正则化和视觉合理性细化，利用视觉基础模型生成高质量伪标签并优化预测。
- 实验或效果：在10个域适应方向和22个解剖目标上验证，性能优于现有方法，达到医学图像分割的SOTA水平。

## 摘要（原文）

> Source Free Unsupervised Domain Adaptation (SFUDA) is critical for deploying deep learning models across diverse clinical settings. However, existing methods are typically designed for low-gap, specific domain shifts and cannot generalize into a unified, multi-modalities, and multi-target framework, which presents a major barrier to real-world application. To overcome this issue, we introduce Tell2Adapt, a novel SFUDA framework that harnesses the vast, generalizable knowledge of the Vision Foundation Model (VFM). Our approach ensures high-fidelity VFM prompts through Context-Aware Prompts Regularization (CAPR), which robustly translates varied text prompts into canonical instructions. This enables the generation of high-quality pseudo-labels for efficiently adapting the lightweight student model to target domain. To guarantee clinical reliability, the framework incorporates Visual Plausibility Refinement (VPR), which leverages the VFM's anatomical knowledge to re-ground the adapted model's predictions in target image's low-level visual features, effectively removing noise and false positives. We conduct one of the most extensive SFUDA evaluations to date, validating our framework across 10 domain adaptation directions and 22 anatomical targets, including brain, cardiac, polyp, and abdominal targets. Our results demonstrate that Tell2Adapt consistently outperforms existing approaches, achieving SOTA for a unified SFUDA framework in medical image segmentation. Code are avaliable at https://github.com/derekshiii/Tell2Adapt.

