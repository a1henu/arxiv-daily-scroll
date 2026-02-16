---
layout: default
title: Universal Transformation of One-Class Classifiers for Unsupervised Anomaly Detection
---

# Universal Transformation of One-Class Classifiers for Unsupervised Anomaly Detection
**arXiv**：[2602.13091v1](https://arxiv.org/abs/2602.13091) · [PDF](https://arxiv.org/pdf/2602.13091.pdf)  
**作者**：Declan McIntosh, Alexandra Branzan Albu  

**一句话要点**：提出数据集折叠方法，将任意单分类器异常检测器转化为无监督方法，适用于图像和视频异常检测。

**关键词**：无监督异常检测, 单分类器, 数据集过滤, 图像异常检测, 视频异常检测, 工业检测

## 3 点简述
- 核心问题：单分类异常检测依赖训练数据仅含正常样本，易受标签噪声影响。
- 方法要点：基于异常罕见且异质的弱假设，利用多个独立训练的单分类器过滤训练数据中的异常。
- 实验或效果：在MVTec AD、ViSA和MVTec Loco AD数据集上实现无监督异常检测的先进性能。

## 摘要（原文）

> Detecting anomalies in images and video is an essential task for multiple real-world problems, including industrial inspection, computer-assisted diagnosis, and environmental monitoring. Anomaly detection is typically formulated as a one-class classification problem, where the training data consists solely of nominal values, leaving methods built on this assumption susceptible to training label noise. We present a dataset folding method that transforms an arbitrary one-class classifier-based anomaly detector into a fully unsupervised method. This is achieved by making a set of key weak assumptions: that anomalies are uncommon in the training dataset and generally heterogeneous. These assumptions enable us to utilize multiple independently trained instances of a one-class classifier to filter the training dataset for anomalies. This transformation requires no modifications to the underlying anomaly detector; the only changes are algorithmically selected data subsets used for training. We demonstrate that our method can transform a wide variety of one-class classifier anomaly detectors for both images and videos into unsupervised ones. Our method creates the first unsupervised logical anomaly detectors by transforming existing methods. We also demonstrate that our method achieves state-of-the-art performance for unsupervised anomaly detection on the MVTec AD, ViSA, and MVTec Loco AD datasets. As improvements to one-class classifiers are made, our method directly transfers those improvements to the unsupervised domain, linking the domains.

