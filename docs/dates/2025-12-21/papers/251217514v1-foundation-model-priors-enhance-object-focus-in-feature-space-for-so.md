---
layout: default
title: Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection
---

# Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection
**arXiv**：[2512.17514v1](https://arxiv.org/abs/2512.17514) · [PDF](https://arxiv.org/pdf/2512.17514.pdf)  
**作者**：Sairam VCR, Rishabh Lalla, Aveen Dayal, Tejal Kulkarni, Anuj Lalla, Vineeth N Balasubramanian, Muhammad Haris Khan  

**一句话要点**：提出FALCON-SFOD框架，利用基础模型先验增强特征空间中的对象聚焦，以解决源自由目标检测中的域偏移问题。

**关键词**：源自由目标检测, 特征空间正则化, 基础模型先验, 伪标签噪声鲁棒性, 前景-背景不平衡

## 3 点简述
- 核心问题：域偏移导致检测器特征空间对象聚焦弱化，产生不可靠伪标签。
- 方法要点：结合SPAR利用视觉基础模型正则化特征空间，IRPL处理前景-背景不平衡和噪声。
- 实验或效果：在SFOD基准测试中实现竞争性性能，理论分析支持更紧的误差界。

## 摘要（原文）

> Current state-of-the-art approaches in Source-Free Object Detection (SFOD) typically rely on Mean-Teacher self-labeling. However, domain shift often reduces the detector's ability to maintain strong object-focused representations, causing high-confidence activations over background clutter. This weak object focus results in unreliable pseudo-labels from the detection head. While prior works mainly refine these pseudo-labels, they overlook the underlying need to strengthen the feature space itself. We propose FALCON-SFOD (Foundation-Aligned Learning with Clutter suppression and Noise robustness), a framework designed to enhance object-focused adaptation under domain shift. It consists of two complementary components. SPAR (Spatial Prior-Aware Regularization) leverages the generalization strength of vision foundation models to regularize the detector's feature space. Using class-agnostic binary masks derived from OV-SAM, SPAR promotes structured and foreground-focused activations by guiding the network toward object regions. IRPL (Imbalance-aware Noise Robust Pseudo-Labeling) complements SPAR by promoting balanced and noise-tolerant learning under severe foreground-background imbalance. Guided by a theoretical analysis that connects these designs to tighter localization and classification error bounds, FALCON-SFOD achieves competitive performance across SFOD benchmarks.

