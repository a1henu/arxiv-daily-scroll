---
layout: default
title: Diffusion-Based sRGB Real Noise Generation via Prompt-Driven Noise Representation Learning
---

# Diffusion-Based sRGB Real Noise Generation via Prompt-Driven Noise Representation Learning
**arXiv**：[2603.04870v1](https://arxiv.org/abs/2603.04870) · [PDF](https://arxiv.org/pdf/2603.04870.pdf)  
**作者**：Jaekyun Ko, Dongjin Kim, Soomin Lee, Guanghui Wang, Tae Hyun Kim  

**一句话要点**：提出提示驱动噪声生成框架以解决sRGB图像去噪中真实噪声数据稀缺问题

**关键词**：sRGB图像去噪, 噪声生成, 扩散模型, 提示驱动学习, 元数据无关

## 3 点简述
- 核心问题：sRGB图像去噪因真实噪声-干净图像对稀缺而受限，现有生成方法依赖相机元数据，通用性差
- 方法要点：基于扩散模型学习高维提示特征捕获输入噪声特性，无需显式元数据，生成多样真实噪声图像
- 实验或效果：在多个基准数据集上验证模型能有效合成真实噪声图像，并成功应用于真实世界噪声去除

## 摘要（原文）

> Denoising in the sRGB image space is challenging due to noise variability. Although end-to-end methods perform well, their effectiveness in real-world scenarios is limited by the scarcity of real noisy-clean image pairs, which are expensive and difficult to collect. To address this limitation, several generative methods have been developed to synthesize realistic noisy images from limited data. These generative approaches often rely on camera metadata during both training and testing to synthesize real-world noise. However, the lack of metadata or inconsistencies between devices restricts their usability. Therefore, we propose a novel framework called Prompt-Driven Noise Generation (PNG). This model is capable of acquiring high-dimensional prompt features that capture the characteristics of real-world input noise and creating a variety of realistic noisy images consistent with the distribution of the input noise. By eliminating the dependency on explicit camera metadata, our approach significantly enhances the generalizability and applicability of noise synthesis. Comprehensive experiments reveal that our model effectively produces realistic noisy images and show the successful application of these generated images in removing real-world noise across various benchmark datasets.

