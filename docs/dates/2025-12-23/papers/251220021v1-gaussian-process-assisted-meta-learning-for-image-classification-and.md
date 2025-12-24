---
layout: default
title: Gaussian Process Assisted Meta-learning for Image Classification and Object Detection Models
---

# Gaussian Process Assisted Meta-learning for Image Classification and Object Detection Models
**arXiv**：[2512.20021v1](https://arxiv.org/abs/2512.20021) · [PDF](https://arxiv.org/pdf/2512.20021.pdf)  
**作者**：Anna R. Flowers, Christopher T. Franck, Robert B. Gramacy, Justin A. Krometis  

**一句话要点**：提出基于高斯过程的元学习方法，通过元数据指导数据采集以提升图像分类与目标检测模型性能。

**关键词**：元学习, 高斯过程, 数据采集优化, 图像分类, 目标检测, 元数据利用

## 3 点简述
- 核心问题：收集真实操作数据成本高，模型在元数据不足条件下性能下降。
- 方法要点：利用训练数据元数据变化评估模型，拟合高斯过程代理以优化新数据采集。
- 实验或效果：相比随机元数据选择，该方法在经典学习和航空图像应用中提升模型性能。

## 摘要（原文）

> Collecting operationally realistic data to inform machine learning models can be costly. Before collecting new data, it is helpful to understand where a model is deficient. For example, object detectors trained on images of rare objects may not be good at identification in poorly represented conditions. We offer a way of informing subsequent data acquisition to maximize model performance by leveraging the toolkit of computer experiments and metadata describing the circumstances under which the training data was collected (e.g., season, time of day, location). We do this by evaluating the learner as the training data is varied according to its metadata. A Gaussian process (GP) surrogate fit to that response surface can inform new data acquisitions. This meta-learning approach offers improvements to learner performance as compared to data with randomly selected metadata, which we illustrate on both classic learning examples, and on a motivating application involving the collection of aerial images in search of airplanes.

