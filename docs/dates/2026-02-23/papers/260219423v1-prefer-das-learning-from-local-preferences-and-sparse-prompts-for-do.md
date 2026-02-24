---
layout: default
title: Prefer-DAS: Learning from Local Preferences and Sparse Prompts for Domain Adaptive Segmentation of Electron Microscopy
---

# Prefer-DAS: Learning from Local Preferences and Sparse Prompts for Domain Adaptive Segmentation of Electron Microscopy
**arXiv**：[2602.19423v1](https://arxiv.org/abs/2602.19423) · [PDF](https://arxiv.org/pdf/2602.19423.pdf)  
**作者**：Jiabao Chen, Shan Xiong, Jialin Peng  

**一句话要点**：提出Prefer-DAS，利用稀疏提示和局部偏好优化实现电子显微镜图像的领域自适应分割

**关键词**：领域自适应分割, 稀疏提示学习, 局部偏好优化, 电子显微镜图像, 弱监督学习, 交互式分割

## 3 点简述
- 核心问题：无监督领域自适应分割在电子显微镜图像中性能有限且偏差大，阻碍实际应用。
- 方法要点：开发Prefer-DAS，集成稀疏提示学习和局部偏好对齐，支持弱监督和无监督分割。
- 实验或效果：在四个挑战性任务上超越SAM类方法及现有自适应方法，接近或超过监督模型性能。

## 摘要（原文）

> Domain adaptive segmentation (DAS) is a promising paradigm for delineating intracellular structures from various large-scale electron microscopy (EM) without incurring extensive annotated data in each domain. However, the prevalent unsupervised domain adaptation (UDA) strategies often demonstrate limited and biased performance, which hinders their practical applications. In this study, we explore sparse points and local human preferences as weak labels in the target domain, thereby presenting a more realistic yet annotation-efficient setting. Specifically, we develop Prefer-DAS, which pioneers sparse promptable learning and local preference alignment. The Prefer-DAS is a promptable multitask model that integrates self-training and prompt-guided contrastive learning. Unlike SAM-like methods, the Prefer-DAS allows for the use of full, partial, and even no point prompts during both training and inference stages and thus enables interactive segmentation. Instead of using image-level human preference alignment for segmentation, we introduce Local direct Preference Optimization (LPO) and sparse LPO (SLPO), plug-and-play solutions for alignment with spatially varying human feedback or sparse feedback. To address potential missing feedback, we also introduce Unsupervised Preference Optimization (UPO), which leverages self-learned preferences. As a result, the Prefer-DAS model can effectively perform both weakly-supervised and unsupervised DAS, depending on the availability of points and human preferences. Comprehensive experiments on four challenging DAS tasks demonstrate that our model outperforms SAM-like methods as well as unsupervised and weakly-supervised DAS methods in both automatic and interactive segmentation modes, highlighting strong generalizability and flexibility. Additionally, the performance of our model is very close to or even exceeds that of supervised models.

