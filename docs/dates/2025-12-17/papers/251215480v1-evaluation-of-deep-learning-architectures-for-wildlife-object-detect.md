---
layout: default
title: Evaluation of deep learning architectures for wildlife object detection: A comparative study of ResNet and Inception
---

# Evaluation of deep learning architectures for wildlife object detection: A comparative study of ResNet and Inception
**arXiv**：[2512.15480v1](https://arxiv.org/abs/2512.15480) · [PDF](https://arxiv.org/pdf/2512.15480.pdf)  
**作者**：Malach Obisa Amonga, Benard Osero, Edna Too  

**一句话要点**：评估ResNet-101与Inception v3在野生动物检测中的性能，为保护应用提供模型选择依据。

**关键词**：野生动物检测, 深度学习架构, ResNet-101, Inception v3, 平均精度均值, 计算机视觉应用

## 3 点简述
- 核心问题：野生动物检测受环境变化、物种视觉相似性和类内多样性挑战。
- 方法要点：使用ResNet-101和Inception v3架构，基于标准化预处理和70:30训练验证分割进行训练。
- 实验或效果：Inception v3略优，准确率95%，mAP 0.92；ResNet-101准确率94%，mAP 0.91，但均对相似物种和恶劣条件敏感。

## 摘要（原文）

> Wildlife object detection plays a vital role in biodiversity conservation, ecological monitoring, and habitat protection. However, this task is often challenged by environmental variability, visual similarities among species, and intra-class diversity. This study investigates the effectiveness of two individual deep learning architectures ResNet-101 and Inception v3 for wildlife object detection under such complex conditions. The models were trained and evaluated on a wildlife image dataset using a standardized preprocessing approach, which included resizing images to a maximum dimension of 800 pixels, converting them to RGB format, and transforming them into PyTorch tensors. A ratio of 70:30 training and validation split was used for model development. The ResNet-101 model achieved a classification accuracy of 94% and a mean Average Precision (mAP) of 0.91, showing strong performance in extracting deep hierarchical features. The Inception v3 model performed slightly better, attaining a classification accuracy of 95% and a mAP of 0.92, attributed to its efficient multi-scale feature extraction through parallel convolutions. Despite the strong results, both models exhibited challenges when detecting species with similar visual characteristics or those captured under poor lighting and occlusion. Nonetheless, the findings confirm that both ResNet-101 and Inception v3 are effective models for wildlife object detection tasks and provide a reliable foundation for conservation-focused computer vision applications.

