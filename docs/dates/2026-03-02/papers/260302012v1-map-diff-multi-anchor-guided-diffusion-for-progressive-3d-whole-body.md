---
layout: default
title: MAP-Diff: Multi-Anchor Guided Diffusion for Progressive 3D Whole-Body Low-Dose PET Denoising
---

# MAP-Diff: Multi-Anchor Guided Diffusion for Progressive 3D Whole-Body Low-Dose PET Denoising
**arXiv**：[2603.02012v1](https://arxiv.org/abs/2603.02012) · [PDF](https://arxiv.org/pdf/2603.02012.pdf)  
**作者**：Peiyuan Jing, Chun-Wun Cheng, Liutao Yang, Zhenxuan Zhang, Thiago V. Lima, Klaus Strobel, Antoine Leimgruber, Angelica Aviles-Rivero, Guang Yang, Javier A. Montoya-Zegarra  

**一句话要点**：提出MAP-Diff，通过多锚点引导扩散模型实现渐进式3D全身低剂量PET去噪。

**关键词**：低剂量PET去噪, 扩散模型, 渐进式重建, 多锚点引导, 3D医学图像处理

## 3 点简述
- 低剂量PET成像存在严重噪声和定量退化，扩散模型去噪轨迹未对齐剂量形成过程。
- MAP-Diff引入临床中间剂量扫描作为锚点，通过时间步依赖监督正则化反向过程。
- 在内部和跨扫描仪数据集上，MAP-Diff在PSNR、SSIM和NMAE指标上优于多种基线方法。

## 摘要（原文）

> Low-dose Positron Emission Tomography (PET) reduces radiation exposure but suffers from severe noise and quantitative degradation. Diffusion-based denoising models achieve strong final reconstructions, yet their reverse trajectories are typically unconstrained and not aligned with the progressive nature of PET dose formation. We propose MAP-Diff, a multi-anchor guided diffusion framework for progressive 3D whole-body PET denoising. MAP-Diff introduces clinically observed intermediate-dose scans as trajectory anchors and enforces timestep-dependent supervision to regularize the reverse process toward dose-aligned intermediate states. Anchor timesteps are calibrated via degradation matching between simulated diffusion corruption and real multi-dose PET pairs, and a timestep-weighted anchor loss stabilizes stage-wise learning. At inference, the model requires only ultra-low-dose input while enabling progressive, dose-consistent intermediate restoration. Experiments on internal (Siemens Biograph Vision Quadra) and cross-scanner (United Imaging uEXPLORER) datasets show consistent improvements over strong CNN-, Transformer-, GAN-, and diffusion-based baselines. On the internal dataset, MAP-Diff improves PSNR from 42.48 dB to 43.71 dB (+1.23 dB), increases SSIM to 0.986, and reduces NMAE from 0.115 to 0.103 (-0.012) compared to 3D DDPM. Performance gains generalize across scanners, achieving 34.42 dB PSNR and 0.141 NMAE on the external cohort, outperforming all competing methods.

