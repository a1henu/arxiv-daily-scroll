---
layout: default
title: Enhancing diffusion models with Gaussianization preprocessing
---

# Enhancing diffusion models with Gaussianization preprocessing
**arXiv**：[2512.21020v1](https://arxiv.org/abs/2512.21020) · [PDF](https://arxiv.org/pdf/2512.21020.pdf)  
**作者**：Li Cunzhi, Louis Kang, Hideaki Shimazaki  

**一句话要点**：提出高斯化预处理以增强扩散模型在小网络中的生成质量

**关键词**：扩散模型, 高斯化预处理, 生成质量, 小网络架构, 采样效率

## 3 点简述
- 扩散模型因轨迹分叉延迟导致早期生成质量下降
- 通过高斯化预处理使目标分布更接近独立高斯分布
- 实验表明该方法提升小网络早期重建的稳定性和效率

## 摘要（原文）

> Diffusion models are a class of generative models that have demonstrated remarkable success in tasks such as image generation. However, one of the bottlenecks of these models is slow sampling due to the delay before the onset of trajectory bifurcation, at which point substantial reconstruction begins. This issue degrades generation quality, especially in the early stages. Our primary objective is to mitigate bifurcation-related issues by preprocessing the training data to enhance reconstruction quality, particularly for small-scale network architectures. Specifically, we propose applying Gaussianization preprocessing to the training data to make the target distribution more closely resemble an independent Gaussian distribution, which serves as the initial density of the reconstruction process. This preprocessing step simplifies the model's task of learning the target distribution, thereby improving generation quality even in the early stages of reconstruction with small networks. The proposed method is, in principle, applicable to a broad range of generative tasks, enabling more stable and efficient sampling processes.

