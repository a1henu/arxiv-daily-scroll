---
layout: default
title: Boosting Fidelity for Pre-Trained-Diffusion-Based Low-Light Image Enhancement via Condition Refinement
---

# Boosting Fidelity for Pre-Trained-Diffusion-Based Low-Light Image Enhancement via Condition Refinement
**arXiv**：[2510.17105v1](https://arxiv.org/abs/2510.17105) · [PDF](https://arxiv.org/pdf/2510.17105.pdf)  
**作者**：Xiaogang Xu, Jian Wang, Yunfan Lu, Ruihang Chu, Ruixing Wang, Jiafei Wu, Bei Yu, Liang Lin  

**一句话要点**：提出条件优化策略以提升预训练扩散模型在低光图像增强中的保真度

**关键词**：低光图像增强, 预训练扩散模型, 条件优化, 潜在细化, 动态交互, 保真度提升

## 3 点简述
- 预训练扩散方法在低光场景下因条件建模不足和交互缺失导致保真度下降
- 引入潜在细化管道和动态交互机制，恢复空间细节并增强控制
- 实验显示该方法可无缝集成现有网络，显著提升保真度

## 摘要（原文）

> Diffusion-based methods, leveraging pre-trained large models like Stable
> Diffusion via ControlNet, have achieved remarkable performance in several
> low-level vision tasks. However, Pre-Trained Diffusion-Based (PTDB) methods
> often sacrifice content fidelity to attain higher perceptual realism. This
> issue is exacerbated in low-light scenarios, where severely degraded
> information caused by the darkness limits effective control. We identify two
> primary causes of fidelity loss: the absence of suitable conditional latent
> modeling and the lack of bidirectional interaction between the conditional
> latent and noisy latent in the diffusion process. To address this, we propose a
> novel optimization strategy for conditioning in pre-trained diffusion models,
> enhancing fidelity while preserving realism and aesthetics. Our method
> introduces a mechanism to recover spatial details lost during VAE encoding,
> i.e., a latent refinement pipeline incorporating generative priors.
> Additionally, the refined latent condition interacts dynamically with the noisy
> latent, leading to improved restoration performance. Our approach is
> plug-and-play, seamlessly integrating into existing diffusion networks to
> provide more effective control. Extensive experiments demonstrate significant
> fidelity improvements in PTDB methods.

