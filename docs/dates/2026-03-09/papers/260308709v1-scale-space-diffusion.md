---
layout: default
title: Scale Space Diffusion
---

# Scale Space Diffusion
**arXiv**：[2603.08709v1](https://arxiv.org/abs/2603.08709) · [PDF](https://arxiv.org/pdf/2603.08709.pdf)  
**作者**：Soumik Mukhopadhyay, Prateksha Udhayanan, Abhinav Shrivastava  

**一句话要点**：提出Scale Space Diffusion，通过融合尺度空间理论优化扩散模型的计算效率。

**关键词**：扩散模型, 尺度空间理论, 计算效率优化, 分辨率自适应, 图像生成

## 3 点简述
- 核心问题：扩散模型在高度噪声状态下处理全分辨率图像可能计算冗余，信息与下采样图像相似。
- 方法要点：引入广义线性退化，将尺度空间融入扩散过程，并设计Flexi-UNet进行分辨率自适应去噪。
- 实验或效果：在CelebA和ImageNet上评估，分析模型在不同分辨率和网络深度下的缩放行为。

## 摘要（原文）

> Diffusion models degrade images through noise, and reversing this process reveals an information hierarchy across timesteps. Scale-space theory exhibits a similar hierarchy via low-pass filtering. We formalize this connection and show that highly noisy diffusion states contain no more information than small, downsampled images - raising the question of why they must be processed at full resolution. To address this, we fuse scale spaces into the diffusion process by formulating a family of diffusion models with generalized linear degradations and practical implementations. Using downsampling as the degradation yields our proposed Scale Space Diffusion. To support Scale Space Diffusion, we introduce Flexi-UNet, a UNet variant that performs resolution-preserving and resolution-increasing denoising using only the necessary parts of the network. We evaluate our framework on CelebA and ImageNet and analyze its scaling behavior across resolutions and network depths. Our project website ( https://prateksha.github.io/projects/scale-space-diffusion/ ) is available publicly.

