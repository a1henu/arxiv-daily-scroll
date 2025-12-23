---
layout: default
title: Patlak Parametric Image Estimation from Dynamic PET Using Diffusion Model Prior
---

# Patlak Parametric Image Estimation from Dynamic PET Using Diffusion Model Prior
**arXiv**：[2512.19584v1](https://arxiv.org/abs/2512.19584) · [PDF](https://arxiv.org/pdf/2512.19584.pdf)  
**作者**：Ziqian Huang, Boxiao Yu, Siqi Li, Savas Ozdemir, Sangjin Bae, Jae Sung Lee, Guobao Wang, Kuang Gong  

**一句话要点**：提出基于扩散模型先验的动力学建模框架，以提升全身动态PET中Patlak参数图像质量。

**关键词**：动态PET, 参数成像, 扩散模型, Patlak模型, 图像质量提升

## 3 点简述
- 核心问题：动态PET参数图像因拟合不适定性和全身扫描计数有限导致质量低下。
- 方法要点：利用预训练扩散模型作为先验，结合Patlak模型作为数据一致性约束进行参数估计。
- 实验或效果：在不同剂量水平的全身动态PET数据集上验证了框架的可行性和性能提升。

## 摘要（原文）

> Dynamic PET enables the quantitative estimation of physiology-related parameters and is widely utilized in research and increasingly adopted in clinical settings. Parametric imaging in dynamic PET requires kinetic modeling to estimate voxel-wise physiological parameters based on specific kinetic models. However, parametric images estimated through kinetic model fitting often suffer from low image quality due to the inherently ill-posed nature of the fitting process and the limited counts resulting from non-continuous data acquisition across multiple bed positions in whole-body PET. In this work, we proposed a diffusion model-based kinetic modeling framework for parametric image estimation, using the Patlak model as an example. The score function of the diffusion model was pre-trained on static total-body PET images and served as a prior for both Patlak slope and intercept images by leveraging their patch-wise similarity. During inference, the kinetic model was incorporated as a data-consistency constraint to guide the parametric image estimation. The proposed framework was evaluated on total-body dynamic PET datasets with different dose levels, demonstrating the feasibility and promising performance of the proposed framework in improving parametric image quality.

