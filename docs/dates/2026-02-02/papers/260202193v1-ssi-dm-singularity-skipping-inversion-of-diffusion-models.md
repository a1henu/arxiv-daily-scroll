---
layout: default
title: SSI-DM: Singularity Skipping Inversion of Diffusion Models
---

# SSI-DM: Singularity Skipping Inversion of Diffusion Models
**arXiv**：[2602.02193v1](https://arxiv.org/abs/2602.02193) · [PDF](https://arxiv.org/pdf/2602.02193.pdf)  
**作者**：Chen Min, Enze Jiang, Jishen Peng, Zheng Ma  

**一句话要点**：提出SSI-DM方法，通过跳过奇异区域解决扩散模型反演中的噪声非高斯性问题

**关键词**：扩散模型反演, 奇异区域跳过, 高斯噪声生成, 图像编辑, 重建保真度, 即插即用技术

## 3 点简述
- 核心问题：扩散模型反演因数学奇异性导致早期去噪步骤不准确，产生非高斯噪声，影响编辑效果
- 方法要点：在标准反演前添加小噪声以绕过奇异区域，生成具有高斯性质的噪声，保持重建保真度
- 实验或效果：作为即插即用技术，在公共图像数据集上实现优越的重建和插值性能

## 摘要（原文）

> Inverting real images into the noise space is essential for editing tasks using diffusion models, yet existing methods produce non-Gaussian noise with poor editability due to the inaccuracy in early noising steps. We identify the root cause: a mathematical singularity that renders inversion fundamentally ill-posed. We propose Singularity Skipping Inversion of Diffusion Models (SSI-DM), which bypasses this singular region by adding small noise before standard inversion. This simple approach produces inverted noise with natural Gaussian properties while maintaining reconstruction fidelity. As a plug-and-play technique compatible with general diffusion models, our method achieves superior performance on public image datasets for reconstruction and interpolation tasks, providing a principled and efficient solution to diffusion model inversion.

