---
layout: default
title: MuRAL-CPD: Active Learning for Multiresolution Change Point Detection
---

# MuRAL-CPD: Active Learning for Multiresolution Change Point Detection
**arXiv**：[2601.20686v1](https://arxiv.org/abs/2601.20686) · [PDF](https://arxiv.org/pdf/2601.20686.pdf)  
**作者**：Stefano Bertolasi, Diego Carrera, Diego Stucchi, Pasqualina Fragneto, Luigi Amedeo Bianchi  

**一句话要点**：提出MuRAL-CPD，通过主动学习优化多分辨率变点检测，提升用户对齐与准确性。

**关键词**：变点检测, 主动学习, 多分辨率分析, 小波分解, 半监督学习

## 3 点简述
- 传统变点检测方法依赖无监督技术，缺乏对任务特定定义的自适应性和用户知识利用。
- MuRAL-CPD结合小波多分辨率分解和主动学习，迭代优化超参数以对齐用户定义的变化。
- 在多个真实数据集上实验显示，该方法在最小监督场景下优于现有先进方法。

## 摘要（原文）

> Change Point Detection (CPD) is a critical task in time series analysis, aiming to identify moments when the underlying data-generating process shifts. Traditional CPD methods often rely on unsupervised techniques, which lack adaptability to task-specific definitions of change and cannot benefit from user knowledge. To address these limitations, we propose MuRAL-CPD, a novel semi-supervised method that integrates active learning into a multiresolution CPD algorithm. MuRAL-CPD leverages a wavelet-based multiresolution decomposition to detect changes across multiple temporal scales and incorporates user feedback to iteratively optimize key hyperparameters. This interaction enables the model to align its notion of change with that of the user, improving both accuracy and interpretability. Our experimental results on several real-world datasets show the effectiveness of MuRAL-CPD against state-of-the-art methods, particularly in scenarios where minimal supervision is available.

