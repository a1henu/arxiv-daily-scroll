---
layout: default
title: Improving Reconstruction of Representation Autoencoder
---

# Improving Reconstruction of Representation Autoencoder
**arXiv**：[2602.08620v1](https://arxiv.org/abs/2602.08620) · [PDF](https://arxiv.org/pdf/2602.08620.pdf)  
**作者**：Siyu Liu, Chujie Qin, Hubery Yin, Qixin Yan, Zheng-Peng Duan, Chen Li, Jing Lyu, Chun-Le Guo, Chongyi Li  

**一句话要点**：提出LV-RAE表示自编码器，通过增强语义特征的低级信息以提升潜在扩散模型的重建保真度与生成质量。

**关键词**：表示自编码器, 潜在扩散模型, 重建保真度, 语义特征增强, 解码器鲁棒性, 生成质量优化

## 3 点简述
- 核心问题：视觉基础模型作为图像编码器时，语义特征缺乏低级信息（如颜色和纹理），导致潜在扩散模型重建保真度下降。
- 方法要点：LV-RAE通过增强语义特征的低级信息，并微调解码器以增加鲁棒性，同时通过受控噪声注入平滑生成潜在。
- 实验或效果：实验表明LV-RAE显著改善重建保真度，保持语义抽象，并实现强生成质量。

## 摘要（原文）

> Recent work leverages Vision Foundation Models as image encoders to boost the generative performance of latent diffusion models (LDMs), as their semantic feature distributions are easy to learn. However, such semantic features often lack low-level information (\eg, color and texture), leading to degraded reconstruction fidelity, which has emerged as a primary bottleneck in further scaling LDMs. To address this limitation, we propose LV-RAE, a representation autoencoder that augments semantic features with missing low-level information, enabling high-fidelity reconstruction while remaining highly aligned with the semantic distribution. We further observe that the resulting high-dimensional, information-rich latent make decoders sensitive to latent perturbations, causing severe artifacts when decoding generated latent and consequently degrading generation quality. Our analysis suggests that this sensitivity primarily stems from excessive decoder responses along directions off the data manifold. Building on these insights, we propose fine-tuning the decoder to increase its robustness and smoothing the generated latent via controlled noise injection, thereby enhancing generation quality. Experiments demonstrate that LV-RAE significantly improves reconstruction fidelity while preserving the semantic abstraction and achieving strong generative quality. Our code is available at https://github.com/modyu-liu/LVRAE.

