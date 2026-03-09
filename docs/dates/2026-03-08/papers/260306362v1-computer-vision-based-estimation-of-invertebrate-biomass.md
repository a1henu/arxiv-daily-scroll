---
layout: default
title: Computer vision-based estimation of invertebrate biomass
---

# Computer vision-based estimation of invertebrate biomass
**arXiv**：[2603.06362v1](https://arxiv.org/abs/2603.06362) · [PDF](https://arxiv.org/pdf/2603.06362.pdf)  
**作者**：Mikko Impiö, Philipp M. Rehsen, Jarrett Blair, Cecilie Mielec, Arne J. Beermann, Florian Leese, Toke T. Høye, Jenni Raitoharju  

**一句话要点**：提出基于计算机视觉的无脊椎动物干重估计方法，以提升生物多样性监测效率

**关键词**：计算机视觉, 生物量估计, 深度神经网络, 生物多样性监测, 图像序列分析, 干重预测

## 3 点简述
- 核心问题：传统干重测量依赖手动称重，耗时且破坏样本，阻碍大规模生物多样性监测。
- 方法要点：利用BIODISCOVER系统采集图像序列，结合面积和下沉速度等新预测因子，开发线性模型和端到端深度神经网络。
- 实验或效果：在复杂形态样本上实现个体干重估计，中位百分比误差为10-20%，结合自动分类可提升群体级估计准确性。

## 摘要（原文）

> The ability to estimate invertebrate biomass using only images could help scaling up quantitative biodiversity monitoring efforts. Computer vision-based methods have the potential to omit the manual, time-consuming, and destructive process of dry weighing specimens. We present two approaches for dry mass estimation that do not require additional manual effort apart from imaging the specimens: fitting a linear model with novel predictors, automatically calculated by an imaging device, and training a family of end-to-end deep neural networks for the task, using single-view, multi-view, and metadata-aware architectures. We propose using area and sinking speed as predictors. These can be calculated with BIODISCOVER, which is a dual-camera system that captures image sequences of specimens sinking in an ethanol column. For this study, we collected a large dataset of dry mass measurement and image sequence pairs to train and evaluate models. We show that our methods can estimate specimen dry mass even with complex and visually diverse specimen morphologies. Combined with automatic taxonomic classification, our approach is an accurate method for group-level dry mass estimation, with a median percentage error of 10-20% for individuals. We highlight the importance of choosing appropriate evaluation metrics, and encourage using both percentage errors and absolute errors as metrics, because they measure different properties. We also explore different optimization losses, data augmentation methods, and model architectures for training deep-learning models.

