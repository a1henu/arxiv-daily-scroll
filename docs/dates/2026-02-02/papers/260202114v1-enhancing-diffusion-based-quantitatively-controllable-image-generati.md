---
layout: default
title: Enhancing Diffusion-Based Quantitatively Controllable Image Generation via Matrix-Form EDM and Adaptive Vicinal Training
---

# Enhancing Diffusion-Based Quantitatively Controllable Image Generation via Matrix-Form EDM and Adaptive Vicinal Training
**arXiv**：[2602.02114v1](https://arxiv.org/abs/2602.02114) · [PDF](https://arxiv.org/pdf/2602.02114.pdf)  
**作者**：Xin Ding, Yun Chen, Sen Zhang, Kao Zhang, Nenglun Chen, Peibei Cao, Yongwei Wang, Fei Wu  

**一句话要点**：提出iCCDM框架，通过矩阵形式EDM和自适应邻域训练增强基于扩散的定量可控图像生成

**关键词**：扩散模型, 可控图像生成, EDM框架, 自适应训练, 采样效率, 图像生成质量

## 3 点简述
- 核心问题：CCDM依赖过时扩散框架和长采样轨迹，导致生成质量受限和采样效率低
- 方法要点：引入改进的EDM框架，采用矩阵形式EDM和自适应邻域训练策略
- 实验或效果：在多个基准数据集上超越现有方法，包括大型文本到图像扩散模型，提高质量并降低采样成本

## 摘要（原文）

> Continuous Conditional Diffusion Model (CCDM) is a diffusion-based framework designed to generate high-quality images conditioned on continuous regression labels. Although CCDM has demonstrated clear advantages over prior approaches across a range of datasets, it still exhibits notable limitations and has recently been surpassed by a GAN-based method, namely CcGAN-AVAR. These limitations mainly arise from its reliance on an outdated diffusion framework and its low sampling efficiency due to long sampling trajectories. To address these issues, we propose an improved CCDM framework, termed iCCDM, which incorporates the more advanced \textit{Elucidated Diffusion Model} (EDM) framework with substantial modifications to improve both generation quality and sampling efficiency. Specifically, iCCDM introduces a novel matrix-form EDM formulation together with an adaptive vicinal training strategy. Extensive experiments on four benchmark datasets, spanning image resolutions from $64\times64$ to $256\times256$, demonstrate that iCCDM consistently outperforms existing methods, including state-of-the-art large-scale text-to-image diffusion models (e.g., Stable Diffusion 3, FLUX.1, and Qwen-Image), achieving higher generation quality while significantly reducing sampling cost.

