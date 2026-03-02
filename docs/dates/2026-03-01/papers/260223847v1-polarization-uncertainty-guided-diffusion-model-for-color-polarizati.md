---
layout: default
title: Polarization Uncertainty-Guided Diffusion Model for Color Polarization Image Demosaicking
---

# Polarization Uncertainty-Guided Diffusion Model for Color Polarization Image Demosaicking
**arXiv**：[2602.23847v1](https://arxiv.org/abs/2602.23847) · [PDF](https://arxiv.org/pdf/2602.23847.pdf)  
**作者**：Chenggong Li, Yidong Luo, Junchao Zhang, Degui Yang  

**一句话要点**：提出基于偏振不确定性引导扩散模型的方法，以解决彩色偏振图像去马赛克中偏振特性重建误差大的问题。

**关键词**：彩色偏振图像去马赛克, 扩散模型, 偏振不确定性建模, 图像重建, 计算机视觉

## 3 点简述
- 核心问题：现有网络方法在彩色偏振去马赛克中能有效恢复强度信息，但偏振特性（偏振度和偏振角）重建误差显著。
- 方法要点：引入文本到图像模型的扩散先验，建模偏振不确定性，并用不确定性引导扩散模型恢复高误差区域。
- 实验或效果：实验表明，该方法能准确恢复场景偏振特性，具有高保真度和强视觉感知。

## 摘要（原文）

> Color polarization demosaicking (CPDM) aims to reconstruct full-resolution polarization images of four directions from the color-polarization filter array (CPFA) raw image. Due to the challenge of predicting numerous missing pixels and the scarcity of high-quality training data, existing network-based methods, despite effectively recovering scene intensity information, still exhibit significant errors in reconstructing polarization characteristics (degree of polarization, DOP, and angle of polarization, AOP). To address this problem, we introduce the image diffusion prior from text-to-image (T2I) models to overcome the performance bottleneck of network-based methods, with the additional diffusion prior compensating for limited representational capacity caused by restricted data distribution. To effectively leverage the diffusion prior, we explicitly model the polarization uncertainty during reconstruction and use uncertainty to guide the diffusion model in recovering high error regions. Extensive experiments demonstrate that the proposed method accurately recovers scene polarization characteristics with both high fidelity and strong visual perception.

