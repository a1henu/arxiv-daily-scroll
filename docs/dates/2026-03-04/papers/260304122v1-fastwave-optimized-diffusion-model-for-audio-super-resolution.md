---
layout: default
title: FastWave: Optimized Diffusion Model for Audio Super-Resolution
---

# FastWave: Optimized Diffusion Model for Audio Super-Resolution
**arXiv**：[2603.04122v1](https://arxiv.org/abs/2603.04122) · [PDF](https://arxiv.org/pdf/2603.04122.pdf)  
**作者**：Nikita Kuznetsov, Maksim Kaledin  

**一句话要点**：提出FastWave扩散模型以优化音频超分辨率，降低计算成本并提升效率

**关键词**：音频超分辨率, 扩散模型, 计算优化, 低参数网络, 高效训练

## 3 点简述
- 音频超分辨率现有方法如扩散模型和GANs计算成本高，训练和推理资源需求大
- FastWave重新考虑扩散模型训练进展，应用于任意采样率到48kHz的超分辨率
- 模型计算复杂度约50 GFLOPs，参数1.3M，训练更快，性能优于NU-Wave 2，与SOTA相当

## 摘要（原文）

> Audio Super-Resolution is a set of techniques aimed at high-quality estimation of the given signal as if it would be sampled with higher sample rate. Among suggested methods there are diffusion and flow models (which are considered slower), generative adversarial networks (which are considered faster), however both approaches are currently presented by high-parametric networks, requiring high computational costs both for training and inference. We propose a solution to both these problems by re-considering the recent advances in the training of diffusion models and applying them to super-resolution from any to 48 kHz sample rate. Our approach shows better results than NU-Wave 2 and is comparable to state-of-the-art models. Our model called FastWave has around 50 GFLOPs of computational complexity and 1.3 M parameters and can be trained with less resources and significantly faster than the majority of recently proposed diffusion- and flow-based solutions. The code has been made publicly available.

