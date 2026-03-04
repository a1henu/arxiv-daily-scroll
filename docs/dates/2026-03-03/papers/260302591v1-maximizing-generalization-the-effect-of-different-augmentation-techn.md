---
layout: default
title: Maximizing Generalization: The Effect of Different Augmentation Techniques on Lightweight Vision Transformer for Bengali Character Classification
---

# Maximizing Generalization: The Effect of Different Augmentation Techniques on Lightweight Vision Transformer for Bengali Character Classification
**arXiv**：[2603.02591v1](https://arxiv.org/abs/2603.02591) · [PDF](https://arxiv.org/pdf/2603.02591.pdf)  
**作者**：Rafi Hassan Chowdhury, Naimul Haque, Kaniz Fatiha  

**一句话要点**：评估多种图像增强技术对轻量级视觉Transformer在孟加拉语字符分类中泛化性能的影响

**关键词**：图像增强, 轻量级视觉Transformer, 孟加拉语字符分类, 数据稀缺, 泛化性能, 手写字符识别

## 3 点简述
- 针对孟加拉语手写字符数据稀缺问题，研究图像增强技术以提升模型泛化能力
- 评估CLAHE、随机旋转、随机仿射、颜色抖动及其组合对轻量模型EfficientViT的性能影响
- 在Ekush和AIBangla数据集上，随机仿射与颜色抖动组合取得最佳准确率，分别为97.48%和97.57%

## 摘要（原文）

> Deep learning models have proven to be highly effective in computer vision, with deep convolutional neural networks achieving impressive results across various computer vision tasks. However, these models rely heavily on large datasets to avoid overfitting. When a model learns features with either low or high variance, it can lead to underfitting or overfitting on the training data. Unfortunately, large-scale datasets may not be available in many domains, particularly for resource-limited languages such as Bengali. In this experiment, a series of tests were conducted in the field of image data augmentation as an approach to addressing the limited data problem for Bengali handwritten characters. The study also provides an in-depth analysis of the performance of different augmentation techniques. Data augmentation refers to a set of techniques applied to data to increase its size and diversity, making it more suitable for training deep learning models. The image augmentation techniques evaluated in this study include CLAHE, Random Rotation, Random Affine, Color Jitter, and their combinations. The study further explores the use of augmentation methods with a lightweight model such as EfficientViT. Among the different augmentation strategies, the combination of Random Affine and Color Jitter produced the best accuracy on the Ekush [1] and AIBangla [2] datasets, achieving accuracies of 97.48% and 97.57%, respectively. This combination outperformed all other individual and combined augmentation techniques. Overall, this analysis presents a thorough examination of the impact of image data augmentation in resource-scarce languages, particularly in the context of Bengali handwritten character recognition using lightweight models.

