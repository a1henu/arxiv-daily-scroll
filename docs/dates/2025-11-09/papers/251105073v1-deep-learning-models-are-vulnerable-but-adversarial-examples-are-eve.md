---
layout: default
title: Deep learning models are vulnerable, but adversarial examples are even more vulnerable
---

# Deep learning models are vulnerable, but adversarial examples are even more vulnerable
**arXiv**：[2511.05073v1](https://arxiv.org/abs/2511.05073) · [PDF](https://arxiv.org/pdf/2511.05073.pdf)  
**作者**：Jun Li, Yanwei Xu, Keran Li, Xiaoli Zhang  

**一句话要点**：提出滑动窗口掩码检测方法以增强对抗样本检测与模型鲁棒性

**关键词**：对抗样本检测, 模型鲁棒性, 遮挡敏感性, 深度学习安全, CIFAR-10数据集

## 3 点简述
- 核心问题：对抗样本在遮挡下比干净样本更敏感，影响DNN鲁棒性。
- 方法要点：引入SMCE量化遮挡下置信度波动，开发SWM-AED检测方法。
- 实验或效果：在CIFAR-10上评估，检测准确率最高达96.5%。

## 摘要（原文）

> Understanding intrinsic differences between adversarial examples and clean
> samples is key to enhancing DNN robustness and detection against adversarial
> attacks. This study first empirically finds that image-based adversarial
> examples are notably sensitive to occlusion. Controlled experiments on CIFAR-10
> used nine canonical attacks (e.g., FGSM, PGD) to generate adversarial examples,
> paired with original samples for evaluation. We introduce Sliding Mask
> Confidence Entropy (SMCE) to quantify model confidence fluctuation under
> occlusion. Using 1800+ test images, SMCE calculations supported by Mask Entropy
> Field Maps and statistical distributions show adversarial examples have
> significantly higher confidence volatility under occlusion than originals.
> Based on this, we propose Sliding Window Mask-based Adversarial Example
> Detection (SWM-AED), which avoids catastrophic overfitting of conventional
> adversarial training. Evaluations across classifiers and attacks on CIFAR-10
> demonstrate robust performance, with accuracy over 62% in most cases and up to
> 96.5%.

