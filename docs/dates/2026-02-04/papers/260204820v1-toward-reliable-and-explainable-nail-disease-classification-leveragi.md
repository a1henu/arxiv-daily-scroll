---
layout: default
title: Toward Reliable and Explainable Nail Disease Classification: Leveraging Adversarial Training and Grad-CAM Visualization
---

# Toward Reliable and Explainable Nail Disease Classification: Leveraging Adversarial Training and Grad-CAM Visualization
**arXiv**：[2602.04820v1](https://arxiv.org/abs/2602.04820) · [PDF](https://arxiv.org/pdf/2602.04820.pdf)  
**作者**：Farzia Hossain, Samanta Ghosh, Shahida Begum, B. M. Shahria Alam, Mohammad Tahmid Noor, Md Parvez Mia, Nishat Tasnim Niloy  

**一句话要点**：提出基于对抗训练和SHAP可视化的机器学习模型，以提升指甲疾病分类的可靠性与可解释性。

**关键词**：指甲疾病分类, 对抗训练, SHAP可视化, 卷积神经网络, 医学图像分析

## 3 点简述
- 核心问题：指甲疾病视觉差异小，早期检测困难，需自动化分类支持诊断。
- 方法要点：使用InceptionV3等CNN模型，结合对抗训练增强鲁棒性，SHAP提供特征可视化。
- 实验或效果：在3835张图像数据集上，InceptionV3准确率达95.57%，模型可辅助医生快速诊断。

## 摘要（原文）

> Human nail diseases are gradually observed over all age groups, especially among older individuals, often going ignored until they become severe. Early detection and accurate diagnosis of such conditions are important because they sometimes reveal our body's health problems. But it is challenging due to the inferred visual differences between disease types. This paper presents a machine learning-based model for automated classification of nail diseases based on a publicly available dataset, which contains 3,835 images scaling six categories. In 224x224 pixels, all images were resized to ensure consistency. To evaluate performance, four well-known CNN models-InceptionV3, DenseNet201, EfficientNetV2, and ResNet50 were trained and analyzed. Among these, InceptionV3 outperformed the others with an accuracy of 95.57%, while DenseNet201 came next with 94.79%. To make the model stronger and less likely to make mistakes on tricky or noisy images, we used adversarial training. To help understand how the model makes decisions, we used SHAP to highlight important features in the predictions. This system could be a helpful support for doctors, making nail disease diagnosis more accurate and faster.

