---
layout: default
title: Group Diffusion: Enhancing Image Generation by Unlocking Cross-Sample Collaboration
---

# Group Diffusion: Enhancing Image Generation by Unlocking Cross-Sample Collaboration
**arXiv**：[2512.10954v1](https://arxiv.org/abs/2512.10954) · [PDF](https://arxiv.org/pdf/2512.10954.pdf)  
**作者**：Sicheng Mo, Thao Nguyen, Richard Zhang, Nick Kolkin, Siddharth Srinivasan Iyer, Eli Shechtman, Krishna Kumar Singh, Yong Jae Lee, Bolei Zhou, Yuheng Li  

**一句话要点**：提出Group Diffusion，通过跨样本协作增强扩散模型图像生成质量。

**关键词**：扩散模型, 注意力机制, 图像生成, 跨样本协作, 联合去噪, FID改进

## 3 点简述
- 核心问题：扩散模型推理时样本独立生成，未利用跨样本协作信号。
- 方法要点：解锁注意力机制，使其在图像间共享，实现联合去噪。
- 实验或效果：在ImageNet-256x256上FID提升达32.2%，组大小与质量正相关。

## 摘要（原文）

> In this work, we explore an untapped signal in diffusion model inference. While all previous methods generate images independently at inference, we instead ask if samples can be generated collaboratively. We propose Group Diffusion, unlocking the attention mechanism to be shared across images, rather than limited to just the patches within an image. This enables images to be jointly denoised at inference time, learning both intra and inter-image correspondence. We observe a clear scaling effect - larger group sizes yield stronger cross-sample attention and better generation quality. Furthermore, we introduce a qualitative measure to capture this behavior and show that its strength closely correlates with FID. Built on standard diffusion transformers, our GroupDiff achieves up to 32.2% FID improvement on ImageNet-256x256. Our work reveals cross-sample inference as an effective, previously unexplored mechanism for generative modeling.

