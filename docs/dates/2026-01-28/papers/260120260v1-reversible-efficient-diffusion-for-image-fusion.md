---
layout: default
title: Reversible Efficient Diffusion for Image Fusion
---

# Reversible Efficient Diffusion for Image Fusion
**arXiv**：[2601.20260v1](https://arxiv.org/abs/2601.20260) · [PDF](https://arxiv.org/pdf/2601.20260.pdf)  
**作者**：Xingxin Xu, Bing Cao, DongDong Li, Qinghua Hu, Pengfei Zhu  

**一句话要点**：提出可逆高效扩散模型以解决多模态图像融合中的细节损失与计算效率问题

**关键词**：多模态图像融合, 扩散模型, 可逆高效扩散, 显式监督训练, 细节保留

## 3 点简述
- 核心问题：扩散模型在图像融合中因马尔可夫过程噪声累积导致细节损失和结果退化
- 方法要点：引入显式监督训练框架，继承扩散模型生成能力，避免分布估计
- 实验或效果：未知，但旨在提升融合图像的细节保留和视觉保真度

## 摘要（原文）

> Multi-modal image fusion aims to consolidate complementary information from diverse source images into a unified representation. The fused image is expected to preserve fine details and maintain high visual fidelity. While diffusion models have demonstrated impressive generative capabilities in image generation, they often suffer from detail loss when applied to image fusion tasks. This issue arises from the accumulation of noise errors inherent in the Markov process, leading to inconsistency and degradation in the fused results. However, incorporating explicit supervision into end-to-end training of diffusion-based image fusion introduces challenges related to computational efficiency. To address these limitations, we propose the Reversible Efficient Diffusion (RED) model - an explicitly supervised training framework that inherits the powerful generative capability of diffusion models while avoiding the distribution estimation.

