---
layout: default
title: Bayesian Optimization for Design Parameters of 3D Image Data Analysis
---

# Bayesian Optimization for Design Parameters of 3D Image Data Analysis
**arXiv**：[2602.15660v1](https://arxiv.org/abs/2602.15660) · [PDF](https://arxiv.org/pdf/2602.15660.pdf)  
**作者**：David Exler, Joaquin Eduardo Urrutia Gómez, Martin Krüger, Maike Schliephake, John Jbeily, Mario Vitacolonna, Rüdiger Rudolf, Markus Reischl  

**一句话要点**：提出3D数据优化管道，通过贝叶斯优化解决生物医学图像分割与分类的参数选择瓶颈。

**关键词**：3D图像分析, 贝叶斯优化, 生物医学图像分割, 参数调优, 分类器设计

## 3 点简述
- 核心问题：3D生物医学图像分析中，模型选择和参数调优是实践中的主要瓶颈。
- 方法要点：采用两阶段贝叶斯优化，先优化分割模型与后处理参数，再优化分类器设计选择。
- 实验或效果：在四个案例研究中，该管道能高效识别针对个体数据集的有效配置。

## 摘要（原文）

> Deep learning-based segmentation and classification are crucial to large-scale biomedical imaging, particularly for 3D data, where manual analysis is impractical. Although many methods exist, selecting suitable models and tuning parameters remains a major bottleneck in practice. Hence, we introduce the 3D data Analysis Optimization Pipeline, a method designed to facilitate the design and parameterization of segmentation and classification using two Bayesian Optimization stages. First, the pipeline selects a segmentation model and optimizes postprocessing parameters using a domain-adapted syntactic benchmark dataset. To ensure a concise evaluation of segmentation performance, we introduce a segmentation quality metric that serves as the objective function. Second, the pipeline optimizes design choices of a classifier, such as encoder and classifier head architectures, incorporation of prior knowledge, and pretraining strategies. To reduce manual annotation effort, this stage includes an assisted class-annotation workflow that extracts predicted instances from the segmentation results and sequentially presents them to the operator, eliminating the need for manual tracking. In four case studies, the 3D data Analysis Optimization Pipeline efficiently identifies effective model and parameter configurations for individual datasets.

