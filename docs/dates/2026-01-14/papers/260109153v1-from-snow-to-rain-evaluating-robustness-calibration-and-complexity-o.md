---
layout: default
title: From Snow to Rain: Evaluating Robustness, Calibration, and Complexity of Model-Based Robust Training
---

# From Snow to Rain: Evaluating Robustness, Calibration, and Complexity of Model-Based Robust Training
**arXiv**：[2601.09153v1](https://arxiv.org/abs/2601.09153) · [PDF](https://arxiv.org/pdf/2601.09153.pdf)  
**作者**：Josué Martínez-Martínez, Olivia Brown, Giselle Zeno, Pooya Khorrami, Rajmonda Caceres  

**一句话要点**：提出基于学习的干扰模型训练方法，结合对抗精炼，提升交通标志识别在雪雨干扰下的鲁棒性、校准和效率。

**关键词**：鲁棒训练, 干扰模型, 对抗训练, 数据增强, 交通标志识别, 模型校准

## 3 点简述
- 核心问题：深度学习在自然干扰（如雪雨）下的鲁棒性不足，影响安全敏感领域的可靠性。
- 方法要点：利用学习到的干扰变化模型生成真实干扰，结合随机覆盖和对抗精炼的混合策略。
- 实验或效果：在CURE-TSR数据集上评估，模型方法优于基线，对抗训练提供最强鲁棒性，数据增强实现类似效果且计算更高效。

## 摘要（原文）

> Robustness to natural corruptions remains a critical challenge for reliable deep learning, particularly in safety-sensitive domains. We study a family of model-based training approaches that leverage a learned nuisance variation model to generate realistic corruptions, as well as new hybrid strategies that combine random coverage with adversarial refinement in nuisance space. Using the Challenging Unreal and Real Environments for Traffic Sign Recognition dataset (CURE-TSR), with Snow and Rain corruptions, we evaluate accuracy, calibration, and training complexity across corruption severities. Our results show that model-based methods consistently outperform baselines Vanilla, Adversarial Training, and AugMix baselines, with model-based adversarial training providing the strongest robustness under across all corruptions but at the expense of higher computation and model-based data augmentation achieving comparable robustness with $T$ less computational complexity without incurring a statistically significant drop in performance. These findings highlight the importance of learned nuisance models for capturing natural variability, and suggest a promising path toward more resilient and calibrated models under challenging conditions.

