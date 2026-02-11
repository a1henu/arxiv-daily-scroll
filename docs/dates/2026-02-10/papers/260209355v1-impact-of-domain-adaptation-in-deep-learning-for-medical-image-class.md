---
layout: default
title: Impact of domain adaptation in deep learning for medical image classifications
---

# Impact of domain adaptation in deep learning for medical image classifications
**arXiv**：[2602.09355v1](https://arxiv.org/abs/2602.09355) · [PDF](https://arxiv.org/pdf/2602.09355.pdf)  
**作者**：Yihang Wu, Ahmad Chaddad  

**一句话要点**：评估域适应在医学图像分类中的影响，涵盖多模态、噪声等场景

**关键词**：域适应, 医学图像分类, 深度学习, 多模态数据, 联邦学习, 模型可解释性

## 3 点简述
- 核心问题：域适应如何提升医学图像分类模型在目标域的性能，尤其在标签不足时
- 方法要点：使用10个深度学习模型模拟常见域适应技术，应用于四个医学图像数据集
- 实验或效果：在脑肿瘤数据集上，域适应使ResNet34性能提升4.7%，并降低噪声影响约3%

## 摘要（原文）

> Domain adaptation (DA) is a quickly expanding area in machine learning that involves adjusting a model trained in one domain to perform well in another domain. While there have been notable progressions, the fundamental concept of numerous DA methodologies has persisted: aligning the data from various domains into a shared feature space. In this space, knowledge acquired from labeled source data can improve the model training on target data that lacks sufficient labels. In this study, we demonstrate the use of 10 deep learning models to simulate common DA techniques and explore their application in four medical image datasets. We have considered various situations such as multi-modality, noisy data, federated learning (FL), interpretability analysis, and classifier calibration. The experimental results indicate that using DA with ResNet34 in a brain tumor (BT) data set results in an enhancement of 4.7\% in model performance. Similarly, the use of DA can reduce the impact of Gaussian noise, as it provides $\sim 3\%$ accuracy increase using ResNet34 on a BT dataset. Furthermore, simply introducing DA into FL framework shows limited potential (e.g., $\sim 0.3\%$ increase in performance) for skin cancer classification. In addition, the DA method can improve the interpretability of the models using the gradcam++ technique, which offers clinical values. Calibration analysis also demonstrates that using DA provides a lower expected calibration error (ECE) value $\sim 2\%$ compared to CNN alone on a multi-modality dataset.

