---
layout: default
title: Improving Supervised Machine Learning Performance in Optical Quality Control via Generative AI for Dataset Expansion
---

# Improving Supervised Machine Learning Performance in Optical Quality Control via Generative AI for Dataset Expansion
**arXiv**：[2601.22961v1](https://arxiv.org/abs/2601.22961) · [PDF](https://arxiv.org/pdf/2601.22961.pdf)  
**作者**：Dennis Sprute, Hanna Senke, Holger Flatt  

**一句话要点**：提出使用生成式AI扩展数据集以提升光学质量控制中监督机器学习性能

**关键词**：光学质量控制, 监督机器学习, 数据集不平衡, 生成式AI, 图像分割, 热图像分析

## 3 点简述
- 核心问题：工业生产中光学质量控制数据集高度不平衡，缺陷样本稀少影响模型性能。
- 方法要点：探索Stable Diffusion和CycleGAN作为生成模型，用于扩展热图像数据集以改善分割。
- 实验或效果：Stable Diffusion扩展数据集使分割性能提升4.6%，Mean IoU达84.6%。

## 摘要（原文）

> Supervised machine learning algorithms play a crucial role in optical quality control within industrial production. These approaches require representative datasets for effective model training. However, while non-defective components are frequent, defective parts are rare in production, resulting in highly imbalanced datasets that adversely impact model performance. Existing strategies to address this challenge, such as specialized loss functions or traditional data augmentation techniques, have limitations, including the need for careful hyperparameter tuning or the alteration of only simple image features. Therefore, this work explores the potential of generative artificial intelligence (GenAI) as an alternative method for expanding limited datasets and enhancing supervised machine learning performance. Specifically, we investigate Stable Diffusion and CycleGAN as image generation models, focusing on the segmentation of combine harvester components in thermal images for subsequent defect detection. Our results demonstrate that dataset expansion using Stable Diffusion yields the most significant improvement, enhancing segmentation performance by 4.6 %, resulting in a Mean Intersection over Union (Mean IoU) of 84.6 %.

