---
layout: default
title: TFTF: Training-Free Targeted Flow for Conditional Sampling
---

# TFTF: Training-Free Targeted Flow for Conditional Sampling
**arXiv**：[2602.12932v1](https://arxiv.org/abs/2602.12932) · [PDF](https://arxiv.org/pdf/2602.12932.pdf)  
**作者**：Qianqian Qu, Jun S. Liu  

**一句话要点**：提出训练自由目标流方法，基于重要性采样改进流匹配模型的条件采样

**关键词**：条件采样, 流匹配模型, 重要性采样, 序贯蒙特卡洛, 训练自由方法, 文本到图像生成

## 3 点简述
- 核心问题：高维条件下重要性采样易出现权重退化，影响条件采样效果
- 方法要点：结合序贯蒙特卡洛重采样和可调噪声随机流，避免训练额外模型
- 实验或效果：在MNIST和CIFAR-10上优于现有方法，并扩展到CelebA-HQ文本到图像生成

## 摘要（原文）

> We propose a training-free conditional sampling method for flow matching models based on importance sampling. Because a naïve application of importance sampling suffers from weight degeneracy in high-dimensional settings, we modify and incorporate a resampling technique in sequential Monte Carlo (SMC) during intermediate stages of the generation process. To encourage generated samples to diverge along distinct trajectories, we derive a stochastic flow with adjustable noise strength to replace the deterministic flow at the intermediate stage. Our framework requires no additional training, while providing theoretical guarantees of asymptotic accuracy. Experimentally, our method significantly outperforms existing approaches on conditional sampling tasks for MNIST and CIFAR-10. We further demonstrate the applicability of our approach in higher-dimensional, multimodal settings through text-to-image generation experiments on CelebA-HQ.

