---
layout: default
title: A Multi-directional Meta-Learning Framework for Class-Generalizable Anomaly Detection
---

# A Multi-directional Meta-Learning Framework for Class-Generalizable Anomaly Detection
**arXiv**：[2601.19833v1](https://arxiv.org/abs/2601.19833) · [PDF](https://arxiv.org/pdf/2601.19833.pdf)  
**作者**：Padmaksha Roy, Lamine Mili, Almuatazbellah Boker  

**一句话要点**：提出多向元学习框架以解决类别泛化异常检测问题

**关键词**：异常检测, 元学习, 类别泛化, 决策面校准, 多向优化

## 3 点简述
- 核心问题：类别泛化异常检测，需用少量异常数据检测未见异常类
- 方法要点：内层学习正常数据流形，外层元调优校准决策面
- 实验或效果：通过多向训练增强泛化能力，适用于异常数据稀缺场景

## 摘要（原文）

> In this paper, we address the problem of class-generalizable anomaly detection, where the objective is to develop a unified model by focusing our learning on the available normal data and a small amount of anomaly data in order to detect the completely unseen anomalies, also referred to as the out-of-distribution (OOD) classes. Adding to this challenge is the fact that the anomaly data is rare and costly to label. To achieve this, we propose a multidirectional meta-learning algorithm -- at the inner level, the model aims to learn the manifold of the normal data (representation); at the outer level, the model is meta-tuned with a few anomaly samples to maximize the softmax confidence margin between the normal and anomaly samples (decision surface calibration), treating normals as in-distribution (ID) and anomalies as out-of-distribution (OOD). By iteratively repeating this process over multiple episodes of predominantly normal and a small number of anomaly samples, we realize a multidirectional meta-learning framework. This two-level optimization, enhanced by multidirectional training, enables stronger generalization to unseen anomaly classes.

