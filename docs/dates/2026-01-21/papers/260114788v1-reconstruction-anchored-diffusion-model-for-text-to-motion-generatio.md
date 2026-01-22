---
layout: default
title: Reconstruction-Anchored Diffusion Model for Text-to-Motion Generation
---

# Reconstruction-Anchored Diffusion Model for Text-to-Motion Generation
**arXiv**：[2601.14788v1](https://arxiv.org/abs/2601.14788) · [PDF](https://arxiv.org/pdf/2601.14788.pdf)  
**作者**：Yifei Liu, Changxing Ding, Ling Guo, Huaiguang Jiang, Qiong Cao  

**一句话要点**：提出重建锚定扩散模型以解决文本到运动生成中的表示差距和误差传播问题

**关键词**：文本到运动生成, 扩散模型, 运动潜在空间, 重构误差指导, 误差传播缓解, 自正则化

## 3 点简述
- 核心问题：现有运动扩散模型存在预训练文本编码器缺乏运动信息导致的表示差距，以及迭代去噪过程中的误差传播。
- 方法要点：引入运动潜在空间作为中间监督，通过自正则化和运动中心潜在对齐增强文本到运动映射；提出重构误差指导机制，利用扩散模型自校正能力减少误差传播。
- 实验或效果：广泛实验显示模型实现显著改进和最优性能，代码将发布。

## 摘要（原文）

> Diffusion models have seen widespread adoption for text-driven human motion generation and related tasks due to their impressive generative capabilities and flexibility. However, current motion diffusion models face two major limitations: a representational gap caused by pre-trained text encoders that lack motion-specific information, and error propagation during the iterative denoising process. This paper introduces Reconstruction-Anchored Diffusion Model (RAM) to address these challenges. First, RAM leverages a motion latent space as intermediate supervision for text-to-motion generation. To this end, RAM co-trains a motion reconstruction branch with two key objective functions: self-regularization to enhance the discrimination of the motion space and motion-centric latent alignment to enable accurate mapping from text to the motion latent space. Second, we propose Reconstructive Error Guidance (REG), a testing-stage guidance mechanism that exploits the diffusion model's inherent self-correction ability to mitigate error propagation. At each denoising step, REG uses the motion reconstruction branch to reconstruct the previous estimate, reproducing the prior error patterns. By amplifying the residual between the current prediction and the reconstructed estimate, REG highlights the improvements in the current prediction. Extensive experiments demonstrate that RAM achieves significant improvements and state-of-the-art performance. Our code will be released.

