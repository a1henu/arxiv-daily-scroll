---
layout: default
title: One4D: Unified 4D Generation and Reconstruction via Decoupled LoRA Control
---

# One4D: Unified 4D Generation and Reconstruction via Decoupled LoRA Control
**arXiv**：[2511.18922v1](https://arxiv.org/abs/2511.18922) · [PDF](https://arxiv.org/pdf/2511.18922.pdf)  
**作者**：Zhenxing Mi, Yuxin Wang, Dan Xu  

**一句话要点**：提出One4D框架，通过解耦LoRA控制统一4D生成与重建

**关键词**：4D生成, 点云重建, LoRA适配器, 视频扩散模型, 统一框架

## 3 点简述
- 核心问题：传统扩散微调在联合RGB和点云生成时易导致模型退化
- 方法要点：使用模态特定LoRA适配器和零初始化控制链接实现解耦计算
- 实验效果：在合成与真实数据集上生成高质量RGB帧和精确点云

## 摘要（原文）

> We present One4D, a unified framework for 4D generation and reconstruction that produces dynamic 4D content as synchronized RGB frames and pointmaps. By consistently handling varying sparsities of conditioning frames through a Unified Masked Conditioning (UMC) mechanism, One4D can seamlessly transition between 4D generation from a single image, 4D reconstruction from a full video, and mixed generation and reconstruction from sparse frames. Our framework adapts a powerful video generation model for joint RGB and pointmap generation, with carefully designed network architectures. The commonly used diffusion finetuning strategies for depthmap or pointmap reconstruction often fail on joint RGB and pointmap generation, quickly degrading the base video model. To address this challenge, we introduce Decoupled LoRA Control (DLC), which employs two modality-specific LoRA adapters to form decoupled computation branches for RGB frames and pointmaps, connected by lightweight, zero-initialized control links that gradually learn mutual pixel-level consistency. Trained on a mixture of synthetic and real 4D datasets under modest computational budgets, One4D produces high-quality RGB frames and accurate pointmaps across both generation and reconstruction tasks. This work represents a step toward general, high-quality geometry-based 4D world modeling using video diffusion models. Project page: https://mizhenxing.github.io/One4D

