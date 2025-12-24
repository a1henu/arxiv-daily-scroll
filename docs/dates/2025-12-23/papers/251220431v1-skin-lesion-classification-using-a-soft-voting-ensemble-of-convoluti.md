---
layout: default
title: Skin Lesion Classification Using a Soft Voting Ensemble of Convolutional Neural Networks
---

# Skin Lesion Classification Using a Soft Voting Ensemble of Convolutional Neural Networks
**arXiv**：[2512.20431v1](https://arxiv.org/abs/2512.20431) · [PDF](https://arxiv.org/pdf/2512.20431.pdf)  
**作者**：Abdullah Al Shafi, Abdul Muntakim, Pintu Chandra Shill, Rowzatul Zannat, Abdullah Al-Amin  

**一句话要点**：提出基于软投票集成卷积神经网络的皮肤病变分类方法，用于早期皮肤癌检测。

**关键词**：皮肤病变分类, 卷积神经网络集成, 软投票, 医学图像分析, 早期癌症检测

## 3 点简述
- 核心问题：早期皮肤癌检测依赖人工诊断，准确率有限，需提升自动化分类精度。
- 方法要点：采用软投票集成MobileNetV2、VGG19和InceptionV3，结合数据预处理和分割技术优化特征提取。
- 实验或效果：在HAM10000、ISIC 2016和ISIC 2019数据集上分别达到96.32%、90.86%和93.92%的准确率。

## 摘要（原文）

> Skin cancer can be identified by dermoscopic examination and ocular inspection, but early detection significantly increases survival chances. Artificial intelligence (AI), using annotated skin images and Convolutional Neural Networks (CNNs), improves diagnostic accuracy. This paper presents an early skin cancer classification method using a soft voting ensemble of CNNs. In this investigation, three benchmark datasets, namely HAM10000, ISIC 2016, and ISIC 2019, were used. The process involved rebalancing, image augmentation, and filtering techniques, followed by a hybrid dual encoder for segmentation via transfer learning. Accurate segmentation focused classification models on clinically significant features, reducing background artifacts and improving accuracy. Classification was performed through an ensemble of MobileNetV2, VGG19, and InceptionV3, balancing accuracy and speed for real-world deployment. The method achieved lesion recognition accuracies of 96.32\%, 90.86\%, and 93.92\% for the three datasets. The system performance was evaluated using established skin lesion detection metrics, yielding impressive results.

