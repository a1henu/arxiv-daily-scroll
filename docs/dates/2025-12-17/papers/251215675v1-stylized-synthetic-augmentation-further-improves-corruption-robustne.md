---
layout: default
title: Stylized Synthetic Augmentation further improves Corruption Robustness
---

# Stylized Synthetic Augmentation further improves Corruption Robustness
**arXiv**：[2512.15675v1](https://arxiv.org/abs/2512.15675) · [PDF](https://arxiv.org/pdf/2512.15675.pdf)  
**作者**：Georg Siedel, Rojan Regmi, Abhirami Anand, Weijia Shao, Silvia Vock, Andrey Morozov  

**一句话要点**：提出结合合成图像与神经风格迁移的数据增强方法，提升深度视觉模型对常见损坏的鲁棒性。

**关键词**：数据增强, 合成图像, 神经风格迁移, 鲁棒性, 图像分类, 模型训练

## 3 点简述
- 核心问题：深度视觉模型对图像常见损坏（如噪声、模糊）的鲁棒性不足。
- 方法要点：通过合成图像与神经风格迁移结合，生成风格化合成图像用于训练，并与规则增强技术互补。
- 实验或效果：在CIFAR-10-C等基准上实现最先进的鲁棒准确率，最高达93.54%。

## 摘要（原文）

> This paper proposes a training data augmentation pipeline that combines synthetic image data with neural style transfer in order to address the vulnerability of deep vision models to common corruptions. We show that although applying style transfer on synthetic images degrades their quality with respect to the common FID metric, these images are surprisingly beneficial for model training. We conduct a systematic empirical analysis of the effects of both augmentations and their key hyperparameters on the performance of image classifiers. Our results demonstrate that stylization and synthetic data complement each other well and can be combined with popular rule-based data augmentation techniques such as TrivialAugment, while not working with others. Our method achieves state-of-the-art corruption robustness on several small-scale image classification benchmarks, reaching 93.54%, 74.9% and 50.86% robust accuracy on CIFAR-10-C, CIFAR-100-C and TinyImageNet-C, respectively

