---
layout: default
title: PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models
---

# PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models
**arXiv**：[2602.20583v1](https://arxiv.org/abs/2602.20583) · [PDF](https://arxiv.org/pdf/2602.20583.pdf)  
**作者**：Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  

**一句话要点**：提出PropFly训练管道，利用预训练视频扩散模型动态监督，解决传播式视频编辑数据获取难题。

**关键词**：视频编辑, 传播学习, 动态监督, 潜在空间生成, 指导调制流匹配

## 3 点简述
- 核心问题：传播式视频编辑需大规模配对视频数据集，获取成本高且复杂。
- 方法要点：通过动态生成源与编辑潜在对，结合指导调制流匹配损失，训练适配器学习传播编辑。
- 实验或效果：在多种视频编辑任务中显著优于现有方法，生成高质量编辑结果。

## 摘要（原文）

> Propagation-based video editing enables precise user control by propagating a single edited frame into following frames while maintaining the original context such as motion and structures. However, training such models requires large-scale, paired (source and edited) video datasets, which are costly and complex to acquire. Hence, we propose the PropFly, a training pipeline for Propagation-based video editing, relying on on-the-Fly supervision from pre-trained video diffusion models (VDMs) instead of requiring off-the-shelf or precomputed paired video editing datasets. Specifically, our PropFly leverages one-step clean latent estimations from intermediate noised latents with varying Classifier-Free Guidance (CFG) scales to synthesize diverse pairs of 'source' (low-CFG) and 'edited' (high-CFG) latents on-the-fly. The source latent serves as structural information of the video, while the edited latent provides the target transformation for learning propagation. Our pipeline enables an additional adapter attached to the pre-trained VDM to learn to propagate edits via Guidance-Modulated Flow Matching (GMFM) loss, which guides the model to replicate the target transformation. Our on-the-fly supervision ensures the model to learn temporally consistent and dynamic transformations. Extensive experiments demonstrate that our PropFly significantly outperforms the state-of-the-art methods on various video editing tasks, producing high-quality editing results.

