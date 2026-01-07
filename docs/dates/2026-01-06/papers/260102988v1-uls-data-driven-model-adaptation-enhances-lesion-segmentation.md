---
layout: default
title: ULS+: Data-driven Model Adaptation Enhances Lesion Segmentation
---

# ULS+: Data-driven Model Adaptation Enhances Lesion Segmentation
**arXiv**：[2601.02988v1](https://arxiv.org/abs/2601.02988) · [PDF](https://arxiv.org/pdf/2601.02988.pdf)  
**作者**：Rianne Weber, Niels Rocholl, Max de Grauw, Mathias Prokop, Ewoud Smit, Alessa Hering  

**一句话要点**：提出ULS+模型，通过数据驱动适应增强CT扫描中全身病灶分割的准确性和速度

**关键词**：病灶分割, CT扫描, 数据驱动适应, 模型更新, 医学图像分析, ULS挑战

## 3 点简述
- 核心问题：原始ULS模型在CT扫描中分割全身病灶时，性能受限于可用数据集和输入图像大小，需提升准确性和推理效率。
- 方法要点：ULS+整合新公开数据集，采用更小输入图像尺寸，实现数据驱动的模型更新，以优化分割性能。
- 实验或效果：在ULS23挑战测试数据和Longitudinal-CT子集上，ULS+在Dice分数和点击点位置鲁棒性上显著优于ULS，并在ULS23挑战中排名第一。

## 摘要（原文）

> In this study, we present ULS+, an enhanced version of the Universal Lesion Segmentation (ULS) model. The original ULS model segments lesions across the whole body in CT scans given volumes of interest (VOIs) centered around a click-point. Since its release, several new public datasets have become available that can further improve model performance. ULS+ incorporates these additional datasets and uses smaller input image sizes, resulting in higher accuracy and faster inference.
>   We compared ULS and ULS+ using the Dice score and robustness to click-point location on the ULS23 Challenge test data and a subset of the Longitudinal-CT dataset. In all comparisons, ULS+ significantly outperformed ULS. Additionally, ULS+ ranks first on the ULS23 Challenge test-phase leaderboard. By maintaining a cycle of data-driven updates and clinical validation, ULS+ establishes a foundation for robust and clinically relevant lesion segmentation models.

