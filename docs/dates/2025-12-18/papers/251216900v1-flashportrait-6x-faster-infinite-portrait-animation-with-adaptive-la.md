---
layout: default
title: FlashPortrait: 6x Faster Infinite Portrait Animation with Adaptive Latent Prediction
---

# FlashPortrait: 6x Faster Infinite Portrait Animation with Adaptive Latent Prediction
**arXiv**：[2512.16900v1](https://arxiv.org/abs/2512.16900) · [PDF](https://arxiv.org/pdf/2512.16900.pdf)  
**作者**：Shuyuan Tu, Yueming Pan, Yinming Huang, Xintong Han, Zhen Xing, Qi Dai, Kai Qiu, Chong Luo, Zuxuan Wu  

**一句话要点**：提出FlashPortrait以解决长肖像动画中身份一致性和推理速度问题

**关键词**：肖像动画, 扩散模型, 身份一致性, 推理加速, 视频合成, 自适应预测

## 3 点简述
- 当前基于扩散的长肖像动画加速方法难以保证身份一致性
- FlashPortrait通过归一化面部表达块和自适应潜在预测实现身份稳定和6倍加速
- 实验在基准测试中验证了方法的有效性和加速效果

## 摘要（原文）

> Current diffusion-based acceleration methods for long-portrait animation struggle to ensure identity (ID) consistency. This paper presents FlashPortrait, an end-to-end video diffusion transformer capable of synthesizing ID-preserving, infinite-length videos while achieving up to 6x acceleration in inference speed. In particular, FlashPortrait begins by computing the identity-agnostic facial expression features with an off-the-shelf extractor. It then introduces a Normalized Facial Expression Block to align facial features with diffusion latents by normalizing them with their respective means and variances, thereby improving identity stability in facial modeling. During inference, FlashPortrait adopts a dynamic sliding-window scheme with weighted blending in overlapping areas, ensuring smooth transitions and ID consistency in long animations. In each context window, based on the latent variation rate at particular timesteps and the derivative magnitude ratio among diffusion layers, FlashPortrait utilizes higher-order latent derivatives at the current timestep to directly predict latents at future timesteps, thereby skipping several denoising steps and achieving 6x speed acceleration. Experiments on benchmarks show the effectiveness of FlashPortrait both qualitatively and quantitatively.

