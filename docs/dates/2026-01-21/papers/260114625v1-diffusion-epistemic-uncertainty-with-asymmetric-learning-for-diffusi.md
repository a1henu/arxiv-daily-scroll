---
layout: default
title: Diffusion Epistemic Uncertainty with Asymmetric Learning for Diffusion-Generated Image Detection
---

# Diffusion Epistemic Uncertainty with Asymmetric Learning for Diffusion-Generated Image Detection
**arXiv**：[2601.14625v1](https://arxiv.org/abs/2601.14625) · [PDF](https://arxiv.org/pdf/2601.14625.pdf)  
**作者**：Yingsong Huang, Hui Guo, Jing Huang, Bing Bai, Qi Xiong  

**一句话要点**：提出DEUA框架，通过估计扩散认知不确定性并采用非对称学习，提升扩散生成图像的检测性能

**关键词**：扩散模型检测, 认知不确定性, 非对称学习, 图像伪造检测, 拉普拉斯近似

## 3 点简述
- 核心问题：现有检测方法忽略认知不确定性与偶然不确定性对重建误差的不同影响，影响检测效果
- 方法要点：引入拉普拉斯近似估计扩散认知不确定性，并设计非对称损失函数训练平衡分类器
- 实验或效果：在大规模基准测试中验证了方法的先进性能，增强了检测器的泛化能力

## 摘要（原文）

> The rapid progress of diffusion models highlights the growing need for detecting generated images. Previous research demonstrates that incorporating diffusion-based measurements, such as reconstruction error, can enhance the generalizability of detectors. However, ignoring the differing impacts of aleatoric and epistemic uncertainty on reconstruction error can undermine detection performance. Aleatoric uncertainty, arising from inherent data noise, creates ambiguity that impedes accurate detection of generated images. As it reflects random variations within the data (e.g., noise in natural textures), it does not help distinguish generated images. In contrast, epistemic uncertainty, which represents the model's lack of knowledge about unfamiliar patterns, supports detection. In this paper, we propose a novel framework, Diffusion Epistemic Uncertainty with Asymmetric Learning~(DEUA), for detecting diffusion-generated images. We introduce Diffusion Epistemic Uncertainty~(DEU) estimation via the Laplace approximation to assess the proximity of data to the manifold of diffusion-generated samples. Additionally, an asymmetric loss function is introduced to train a balanced classifier with larger margins, further enhancing generalizability. Extensive experiments on large-scale benchmarks validate the state-of-the-art performance of our method.

