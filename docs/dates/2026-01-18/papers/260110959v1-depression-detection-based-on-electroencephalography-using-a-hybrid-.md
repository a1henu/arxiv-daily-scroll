---
layout: default
title: Depression Detection Based on Electroencephalography Using a Hybrid Deep Neural Network CNN-GRU and MRMR Feature Selection
---

# Depression Detection Based on Electroencephalography Using a Hybrid Deep Neural Network CNN-GRU and MRMR Feature Selection
**arXiv**：[2601.10959v1](https://arxiv.org/abs/2601.10959) · [PDF](https://arxiv.org/pdf/2601.10959.pdf)  
**作者**：Mohammad Reza Yousefi, Hajar Ismail Al-Tamimi, Amin Dehghani  

**一句话要点**：提出基于CNN-GRU和MRMR的混合深度学习框架，用于EEG信号的抑郁症早期检测。

**关键词**：抑郁症检测, 脑电图分析, 卷积神经网络, 门控循环单元, 特征选择, 深度学习框架

## 3 点简述
- 核心问题：抑郁症诊断依赖主观自评，需客观准确方法。
- 方法要点：结合CNN和GRU提取EEG时空特征，用MRMR算法优化特征选择。
- 实验或效果：模型在抑郁症检测中达到98.74%的总体准确率。

## 摘要（原文）

> This study investigates the detection and classification of depressive and non-depressive states using deep learning approaches. Depression is a prevalent mental health disorder that substantially affects quality of life, and early diagnosis can greatly enhance treatment effectiveness and patient care. However, conventional diagnostic methods rely heavily on self-reported assessments, which are often subjective and may lack reliability. Consequently, there is a strong need for objective and accurate techniques to identify depressive states. In this work, a deep learning based framework is proposed for the early detection of depression using EEG signals. EEG data, which capture underlying brain activity and are not influenced by external behavioral factors, can reveal subtle neural changes associated with depression. The proposed approach combines convolutional neural networks (CNNs) and gated recurrent units (GRUs) to jointly extract spatial and temporal features from EEG recordings. The minimum redundancy maximum relevance (MRMR) algorithm is then applied to select the most informative features, followed by classification using a fully connected neural network. The results demonstrate that the proposed model achieves high performance in accurately identifying depressive states, with an overall accuracy of 98.74%. By effectively integrating temporal and spatial information and employing optimized feature selection, this method shows strong potential as a reliable tool for clinical applications. Overall, the proposed framework not only enables accurate early detection of depression but also has the potential to support improved treatment strategies and patient outcomes.

