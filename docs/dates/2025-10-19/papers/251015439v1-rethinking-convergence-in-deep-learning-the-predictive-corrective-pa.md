---
layout: default
title: Rethinking Convergence in Deep Learning: The Predictive-Corrective Paradigm for Anatomy-Informed Brain MRI Segmentation
---

# Rethinking Convergence in Deep Learning: The Predictive-Corrective Paradigm for Anatomy-Informed Brain MRI Segmentation
**arXiv**：[2510.15439v1](https://arxiv.org/abs/2510.15439) · [PDF](https://arxiv.org/pdf/2510.15439.pdf)  
**作者**：Feifei Zhang, Zhenhong Jia, Sensen Song, Fei Shi, Dayong Ren  

**一句话要点**：提出预测-校正范式以加速数据稀缺的脑MRI分割

**关键词**：脑MRI分割, 预测-校正范式, 深度学习收敛, 医学影像, 解剖知识集成

## 3 点简述
- 端到端深度学习收敛慢且依赖大数据，限制医学影像应用
- 预测模块生成粗近似，校正模块学习残差，聚焦关键区域
- 实验显示PCMambaNet在1-5轮内收敛，达到高精度

## 摘要（原文）

> Despite the remarkable success of the end-to-end paradigm in deep learning,
> it often suffers from slow convergence and heavy reliance on large-scale
> datasets, which fundamentally limits its efficiency and applicability in
> data-scarce domains such as medical imaging. In this work, we introduce the
> Predictive-Corrective (PC) paradigm, a framework that decouples the modeling
> task to fundamentally accelerate learning. Building upon this paradigm, we
> propose a novel network, termed PCMambaNet. PCMambaNet is composed of two
> synergistic modules. First, the Predictive Prior Module (PPM) generates a
> coarse approximation at low computational cost, thereby anchoring the search
> space. Specifically, the PPM leverages anatomical knowledge-bilateral
> symmetry-to predict a 'focus map' of diagnostically relevant asymmetric
> regions. Next, the Corrective Residual Network (CRN) learns to model the
> residual error, focusing the network's full capacity on refining these
> challenging regions and delineating precise pathological boundaries. Extensive
> experiments on high-resolution brain MRI segmentation demonstrate that
> PCMambaNet achieves state-of-the-art accuracy while converging within only 1-5
> epochs-a performance unattainable by conventional end-to-end models. This
> dramatic acceleration highlights that by explicitly incorporating domain
> knowledge to simplify the learning objective, PCMambaNet effectively mitigates
> data inefficiency and overfitting.

