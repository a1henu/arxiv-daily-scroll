---
layout: default
title: Preventing Shortcut Learning in Medical Image Analysis through Intermediate Layer Knowledge Distillation from Specialist Teachers
---

# Preventing Shortcut Learning in Medical Image Analysis through Intermediate Layer Knowledge Distillation from Specialist Teachers
**arXiv**：[2511.17421v1](https://arxiv.org/abs/2511.17421) · [PDF](https://arxiv.org/pdf/2511.17421.pdf)  
**作者**：Christopher Boland, Sotirios Tsaftaris, Sonia Dahdouh  

**一句话要点**：提出中间层知识蒸馏框架以解决医学图像分析中的捷径学习问题

**关键词**：医学图像分析, 捷径学习, 知识蒸馏, 中间层学习, 稳健性提升, 深度学习

## 3 点简述
- 核心问题：深度学习模型易学习训练数据中虚假相关特征，导致医学图像预测缺乏稳健性。
- 方法要点：利用任务相关数据微调的教师网络，指导学生网络中间层，缓解捷径学习。
- 实验或效果：在多个数据集上优于传统方法，接近无偏数据基线，提升泛化能力。

## 摘要（原文）

> Deep learning models are prone to learning shortcut solutions to problems using spuriously correlated yet irrelevant features of their training data. In high-risk applications such as medical image analysis, this phenomenon may prevent models from using clinically meaningful features when making predictions, potentially leading to poor robustness and harm to patients. We demonstrate that different types of shortcuts (those that are diffuse and spread throughout the image, as well as those that are localized to specific areas) manifest distinctly across network layers and can, therefore, be more effectively targeted through mitigation strategies that target the intermediate layers. We propose a novel knowledge distillation framework that leverages a teacher network fine-tuned on a small subset of task-relevant data to mitigate shortcut learning in a student network trained on a large dataset corrupted with a bias feature. Through extensive experiments on CheXpert, ISIC 2017, and SimBA datasets using various architectures (ResNet-18, AlexNet, DenseNet-121, and 3D CNNs), we demonstrate consistent improvements over traditional Empirical Risk Minimization, augmentation-based bias-mitigation, and group-based bias-mitigation approaches. In many cases, we achieve comparable performance with a baseline model trained on bias-free data, even on out-of-distribution test data. Our results demonstrate the practical applicability of our approach to real-world medical imaging scenarios where bias annotations are limited and shortcut features are difficult to identify a priori.

