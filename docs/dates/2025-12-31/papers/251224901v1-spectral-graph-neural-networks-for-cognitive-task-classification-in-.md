---
layout: default
title: Spectral Graph Neural Networks for Cognitive Task Classification in fMRI Connectomes
---

# Spectral Graph Neural Networks for Cognitive Task Classification in fMRI Connectomes
**arXiv**：[2512.24901v1](https://arxiv.org/abs/2512.24901) · [PDF](https://arxiv.org/pdf/2512.24901.pdf)  
**作者**：Debasis Maji, Arghya Banerjee, Debaditya Barman  

**一句话要点**：提出SpectralBrainGNN模型，基于图傅里叶变换对fMRI连接组进行认知任务分类。

**关键词**：认知任务分类, fMRI连接组, 图神经网络, 谱卷积, 图傅里叶变换, 脑网络分析

## 3 点简述
- 核心问题：从fMRI连接组中解码认知状态，传统方法可能忽略拓扑依赖和多尺度交互。
- 方法要点：采用谱卷积框架，通过归一化拉普拉斯特征分解计算图傅里叶变换，建模脑区为节点和功能连接为边。
- 实验或效果：在HCPTask数据集上实现96.25%的分类准确率，代码开源以支持可复现性。

## 摘要（原文）

> Cognitive task classification using machine learning plays a central role in decoding brain states from neuroimaging data. By integrating machine learning with brain network analysis, complex connectivity patterns can be extracted from functional magnetic resonance imaging connectomes. This process transforms raw blood-oxygen-level-dependent (BOLD) signals into interpretable representations of cognitive processes. Graph neural networks (GNNs) further advance this paradigm by modeling brain regions as nodes and functional connections as edges, capturing topological dependencies and multi-scale interactions that are often missed by conventional approaches. Our proposed SpectralBrainGNN model, a spectral convolution framework based on graph Fourier transforms (GFT) computed via normalized Laplacian eigendecomposition. Experiments on the Human Connectome Project-Task (HCPTask) dataset demonstrate the effectiveness of the proposed approach, achieving a classification accuracy of 96.25\%. The implementation is publicly available at https://github.com/gnnplayground/SpectralBrainGNN to support reproducibility and future research.

