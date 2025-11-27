---
layout: default
title: Data-Driven Assessment of Concrete Slab Integrity via Impact-Echo Signals and Neural Networks
---

# Data-Driven Assessment of Concrete Slab Integrity via Impact-Echo Signals and Neural Networks
**arXiv**：[2511.21080v1](https://arxiv.org/abs/2511.21080) · [PDF](https://arxiv.org/pdf/2511.21080.pdf)  
**作者**：Yeswanth Ravichandran, Duoduo Liao, Charan Teja Kurakula  

**一句话要点**：提出基于机器学习的冲击回波框架，用于自动检测混凝土桥面板缺陷

**关键词**：冲击回波信号处理, 长短期记忆网络, 混凝土缺陷分类, 非破坏性评估, 数据驱动监测

## 3 点简述
- 核心问题：混凝土桥面板内部缺陷难以可靠检测，影响结构耐久性。
- 方法要点：将冲击回波信号转换为频域特征，使用LSTM网络进行多类缺陷分类。
- 实验或效果：在实验室和现场验证中，模型达到73%准确率，并展示良好泛化能力。

## 摘要（原文）

> Subsurface defects such as delamination, voids, and honeycombing critically affect the durability of concrete bridge decks but are difficult to detect reliably using visual inspection or manual sounding. This paper presents a machine learning based Impact Echo (IE) framework that automates both defect localization and multi-class classification of common concrete defects. Raw IE signals from Federal Highway Administration (FHWA) laboratory slabs and in-service bridge decks are transformed via Fast Fourier Transform (FFT) into dominant peak-frequency features and interpolated into spatial maps for defect zone visualization. Unsupervised k-means clustering highlights low-frequency, defect-prone regions, while Ground Truth Masks (GTMs) derived from seeded lab defects are used to validate spatial accuracy and generate high-confidence training labels. From these validated regions, spatially ordered peak-frequency sequences are constructed and fed into a stacked Long Short-Term Memory (LSTM) network that classifies four defect types shallow delamination, deep delamination, voids, and honeycombing with 73% overall accuracy. Field validation on the bridge deck demonstrates that models trained on laboratory data generalize under realistic coupling, noise, and environmental variability. The proposed framework enhances the objectivity, scalability, and repeatability of Non-Destructive Evaluation (NDE), supporting intelligent, data-driven bridge health monitoring at a network scale.

