---
layout: default
title: A Difference-in-Difference Approach to Detecting AI-Generated Images
---

# A Difference-in-Difference Approach to Detecting AI-Generated Images
**arXiv**：[2602.23732v1](https://arxiv.org/abs/2602.23732) · [PDF](https://arxiv.org/pdf/2602.23732.pdf)  
**作者**：Xinyi Qi, Kai Ye, Chengchun Shi, Ying Yang, Hongyi Zhou, Jin Zhu  

**一句话要点**：提出差异中的差异方法以提升AI生成图像检测的泛化性能

**关键词**：AI生成图像检测, 扩散模型, 重构误差, 差异中的差异, 泛化性能

## 3 点简述
- 核心问题：扩散模型生成的图像与真实图像高度相似，传统基于重构误差的检测器效果下降
- 方法要点：计算重构误差的差异（二阶差异），而非直接使用重构误差（一阶差异），以降低方差
- 实验或效果：广泛实验表明该方法在生成AI时代能实现可靠的检测，具有强泛化性能

## 摘要（原文）

> Diffusion models are able to produce AI-generated images that are almost indistinguishable from real ones. This raises concerns about their potential misuse and poses substantial challenges for detecting them. Many existing detectors rely on reconstruction error -- the difference between the input image and its reconstructed version -- as the basis for distinguishing real from fake images. However, these detectors become less effective as modern AI-generated images become increasingly similar to real ones. To address this challenge, we propose a novel difference-in-difference method. Instead of directly using the reconstruction error (a first-order difference), we compute the difference in reconstruction error -- a second-order difference -- for variance reduction and improving detection accuracy. Extensive experiments demonstrate that our method achieves strong generalization performance, enabling reliable detection of AI-generated images in the era of generative AI.

