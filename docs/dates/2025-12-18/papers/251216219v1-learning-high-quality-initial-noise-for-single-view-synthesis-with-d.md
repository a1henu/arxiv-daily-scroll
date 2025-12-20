---
layout: default
title: Learning High-Quality Initial Noise for Single-View Synthesis with Diffusion Models
---

# Learning High-Quality Initial Noise for Single-View Synthesis with Diffusion Models
**arXiv**：[2512.16219v1](https://arxiv.org/abs/2512.16219) · [PDF](https://arxiv.org/pdf/2512.16219.pdf)  
**作者**：Zhihao Zhang, Xuejun Yang, Weihua Liu, Mouquan Shen  

**一句话要点**：提出基于编码器-解码器网络的框架，学习高质量初始噪声以提升单视图合成性能

**关键词**：单视图合成, 扩散模型, 初始噪声学习, 编码器-解码器网络, 欧拉反演

## 3 点简述
- 核心问题：单视图新视图合成中，扩散模型缺乏学习高质量初始噪声的专用框架
- 方法要点：设计离散化欧拉反演法构建噪声配对数据集，并训练编码器-解码器网络转换随机噪声
- 实验或效果：框架可无缝集成到SV3D等模型，在多个数据集上显著提升性能

## 摘要（原文）

> Single-view novel view synthesis (NVS) models based on diffusion models have recently attracted increasing attention, as they can generate a series of novel view images from a single image prompt and camera pose information as conditions. It has been observed that in diffusion models, certain high-quality initial noise patterns lead to better generation results than others. However, there remains a lack of dedicated learning frameworks that enable NVS models to learn such high-quality noise. To obtain high-quality initial noise from random Gaussian noise, we make the following contributions. First, we design a discretized Euler inversion method to inject image semantic information into random noise, thereby constructing paired datasets of random and high-quality noise. Second, we propose a learning framework based on an encoder-decoder network (EDN) that directly transforms random noise into high-quality noise. Experiments demonstrate that the proposed EDN can be seamlessly plugged into various NVS models, such as SV3D and MV-Adapter, achieving significant performance improvements across multiple datasets. Code is available at: https://github.com/zhihao0512/EDN.

