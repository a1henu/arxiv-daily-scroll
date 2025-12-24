---
layout: default
title: How I Met Your Bias: Investigating Bias Amplification in Diffusion Models
---

# How I Met Your Bias: Investigating Bias Amplification in Diffusion Models
**arXiv**：[2512.20233v1](https://arxiv.org/abs/2512.20233) · [PDF](https://arxiv.org/pdf/2512.20233.pdf)  
**作者**：Nathan Roos, Ekaterina Iakovleva, Ani Gjergji, Vito Paolo Pastore, Enzo Tartaglione  

**一句话要点**：分析扩散模型采样算法对偏差放大的影响，揭示超参数可调控偏差

**关键词**：扩散模型, 偏差放大, 采样算法, 超参数调控, 图像合成, 数据集偏差

## 3 点简述
- 核心问题：扩散模型在图像合成中复制和放大数据集偏差，机制未明
- 方法要点：首次研究采样算法及超参数如何影响偏差放大，而非视为固有特性
- 实验或效果：在Biased MNIST等数据集上实证采样超参数可诱导偏差减少或放大

## 摘要（原文）

> Diffusion-based generative models demonstrate state-of-the-art performance across various image synthesis tasks, yet their tendency to replicate and amplify dataset biases remains poorly understood. Although previous research has viewed bias amplification as an inherent characteristic of diffusion models, this work provides the first analysis of how sampling algorithms and their hyperparameters influence bias amplification. We empirically demonstrate that samplers for diffusion models -- commonly optimized for sample quality and speed -- have a significant and measurable effect on bias amplification. Through controlled studies with models trained on Biased MNIST, Multi-Color MNIST and BFFHQ, and with Stable Diffusion, we show that sampling hyperparameters can induce both bias reduction and amplification, even when the trained model is fixed. Source code is available at https://github.com/How-I-met-your-bias/how_i_met_your_bias.

