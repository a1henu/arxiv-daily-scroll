---
layout: default
title: Synthetic Data for Robust Runway Detection
---

# Synthetic Data for Robust Runway Detection
**arXiv**：[2510.20349v1](https://arxiv.org/abs/2510.20349) · [PDF](https://arxiv.org/pdf/2510.20349.pdf)  
**作者**：Estelle Chigot, Dennis G. Wilson, Meriem Ghrib, Fabrice Jimenez, Thomas Oberlin  

**一句话要点**：提出基于飞行模拟器的合成数据方法以增强跑道检测在自主着陆中的鲁棒性

**关键词**：合成数据生成, 跑道检测, 自主着陆系统, 域适应, 鲁棒性评估, 飞行模拟器

## 3 点简述
- 核心问题：关键应用中真实数据收集成本高且难以覆盖所有条件，如夜间场景。
- 方法要点：使用商业飞行模拟器生成合成图像，结合少量真实图像进行训练。
- 实验或效果：标准检测模型实现准确预测，并通过定制域适应策略提升对未知条件的鲁棒性。

## 摘要（原文）

> Deep vision models are now mature enough to be integrated in industrial and
> possibly critical applications such as autonomous navigation. Yet, data
> collection and labeling to train such models requires too much efforts and
> costs for a single company or product. This drawback is more significant in
> critical applications, where training data must include all possible conditions
> including rare scenarios. In this perspective, generating synthetic images is
> an appealing solution, since it allows a cheap yet reliable covering of all the
> conditions and environments, if the impact of the synthetic-to-real
> distribution shift is mitigated. In this article, we consider the case of
> runway detection that is a critical part in autonomous landing systems
> developed by aircraft manufacturers. We propose an image generation approach
> based on a commercial flight simulator that complements a few annotated real
> images. By controlling the image generation and the integration of real and
> synthetic data, we show that standard object detection models can achieve
> accurate prediction. We also evaluate their robustness with respect to adverse
> conditions, in our case nighttime images, that were not represented in the real
> data, and show the interest of using a customized domain adaptation strategy.

