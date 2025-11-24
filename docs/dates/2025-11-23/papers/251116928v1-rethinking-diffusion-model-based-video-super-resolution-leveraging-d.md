---
layout: default
title: Rethinking Diffusion Model-Based Video Super-Resolution: Leveraging Dense Guidance from Aligned Features
---

# Rethinking Diffusion Model-Based Video Super-Resolution: Leveraging Dense Guidance from Aligned Features
**arXiv**：[2511.16928v1](https://arxiv.org/abs/2511.16928) · [PDF](https://arxiv.org/pdf/2511.16928.pdf)  
**作者**：Jingyi Xu, Meisong Zheng, Ying Chen, Minglang Qiao, Xin Deng, Mai Xu  

**一句话要点**：提出DGAF-VSR模型，利用对齐特征密集引导解决视频超分辨率中的误差累积与保真度权衡问题

**关键词**：视频超分辨率, 扩散模型, 特征对齐, 时序一致性, 光学引导变形

## 3 点简述
- 核心问题：基于扩散模型的视频超分辨率存在误差累积、空间伪影及感知质量与保真度权衡问题
- 方法要点：引入光学引导变形模块和特征域时序条件模块，在特征域进行密集引导与对齐
- 实验或效果：在合成和真实数据集上，感知质量、保真度和时序一致性均优于现有方法

## 摘要（原文）

> Diffusion model (DM) based Video Super-Resolution (VSR) approaches achieve impressive perceptual quality. However, they suffer from error accumulation, spatial artifacts, and a trade-off between perceptual quality and fidelity, primarily caused by inaccurate alignment and insufficient compensation between video frames. In this paper, within the DM-based VSR pipeline, we revisit the role of alignment and compensation between adjacent video frames and reveal two crucial observations: (a) the feature domain is better suited than the pixel domain for information compensation due to its stronger spatial and temporal correlations, and (b) warping at an upscaled resolution better preserves high-frequency information, but this benefit is not necessarily monotonic. Therefore, we propose a novel Densely Guided diffusion model with Aligned Features for Video Super-Resolution (DGAF-VSR), with an Optical Guided Warping Module (OGWM) to maintain high-frequency details in the aligned features and a Feature-wise Temporal Condition Module (FTCM) to deliver dense guidance in the feature domain. Extensive experiments on synthetic and real-world datasets demonstrate that DGAF-VSR surpasses state-of-the-art methods in key aspects of VSR, including perceptual quality (35.82\% DISTS reduction), fidelity (0.20 dB PSNR gain), and temporal consistency (30.37\% tLPIPS reduction).

