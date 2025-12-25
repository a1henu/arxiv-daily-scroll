---
layout: default
title: A Unified Framework for EEG Seizure Detection Using Universum-Integrated Generalized Eigenvalues Proximal Support Vector Machine
---

# A Unified Framework for EEG Seizure Detection Using Universum-Integrated Generalized Eigenvalues Proximal Support Vector Machine
**arXiv**：[2512.21170v1](https://arxiv.org/abs/2512.21170) · [PDF](https://arxiv.org/pdf/2512.21170.pdf)  
**作者**：Yogesh Kumar, Vrushank Ahire, M. A. Ganaie  

**一句话要点**：提出Universum增强的广义特征值近端支持向量机框架，用于EEG信号分类以解决非平稳性和数据有限问题。

**关键词**：EEG信号分类, Universum学习, 广义特征值分解, 近端支持向量机, 癫痫检测

## 3 点简述
- 核心问题：EEG信号分析面临非平稳性、低信噪比和标记数据有限等挑战。
- 方法要点：引入Universum学习，通过比率目标函数和加权差公式增强分类器稳定性和泛化能力。
- 实验或效果：在Bonn数据集上，IU-GEPSVM在健康与癫痫分类任务中达到最高85%准确率，优于基线方法。

## 摘要（原文）

> The paper presents novel Universum-enhanced classifiers: the Universum Generalized Eigenvalue Proximal Support Vector Machine (U-GEPSVM) and the Improved U-GEPSVM (IU-GEPSVM) for EEG signal classification. Using the computational efficiency of generalized eigenvalue decomposition and the generalization benefits of Universum learning, the proposed models address critical challenges in EEG analysis: non-stationarity, low signal-to-noise ratio, and limited labeled data. U-GEPSVM extends the GEPSVM framework by incorporating Universum constraints through a ratio-based objective function, while IU-GEPSVM enhances stability through a weighted difference-based formulation that provides independent control over class separation and Universum alignment. The models are evaluated on the Bonn University EEG dataset across two binary classification tasks: (O vs S)-healthy (eyes closed) vs seizure, and (Z vs S)-healthy (eyes open) vs seizure. IU-GEPSVM achieves peak accuracies of 85% (O vs S) and 80% (Z vs S), with mean accuracies of 81.29% and 77.57% respectively, outperforming baseline methods.

