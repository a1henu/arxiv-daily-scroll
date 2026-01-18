---
layout: default
title: Towards Efficient Low-rate Image Compression with Frequency-aware Diffusion Prior Refinement
---

# Towards Efficient Low-rate Image Compression with Frequency-aware Diffusion Prior Refinement
**arXiv**：[2601.10373v1](https://arxiv.org/abs/2601.10373) · [PDF](https://arxiv.org/pdf/2601.10373.pdf)  
**作者**：Yichong Xia, Yimin Zhou, Jinpeng Wang, Bin Chen  

**一句话要点**：提出DiffCR框架以解决基于扩散先验的低码率图像压缩中采样慢和比特分配次优问题

**关键词**：低码率图像压缩, 扩散先验, 频率感知, 一致性估计, 两步解码

## 3 点简述
- 现有扩散先验压缩方法存在采样过程慢和比特分配次优问题
- DiffCR引入频率感知跳跃估计模块和一致性估计器，实现高效两步解码
- 实验显示DiffCR在比特率节省和速度提升方面显著优于现有基线

## 摘要（原文）

> Recent advancements in diffusion-based generative priors have enabled visually plausible image compression at extremely low bit rates. However, existing approaches suffer from slow sampling processes and suboptimal bit allocation due to fragmented training paradigms. In this work, we propose Accelerate \textbf{Diff}usion-based Image Compression via \textbf{C}onsistency Prior \textbf{R}efinement (DiffCR), a novel compression framework for efficient and high-fidelity image reconstruction. At the heart of DiffCR is a Frequency-aware Skip Estimation (FaSE) module that refines the $ε$-prediction prior from a pre-trained latent diffusion model and aligns it with compressed latents at different timesteps via Frequency Decoupling Attention (FDA). Furthermore, a lightweight consistency estimator enables fast \textbf{two-step decoding} by preserving the semantic trajectory of diffusion sampling. Without updating the backbone diffusion model, DiffCR achieves substantial bitrate savings (27.2\% BD-rate (LPIPS) and 65.1\% BD-rate (PSNR)) and over $10\times$ speed-up compared to SOTA diffusion-based compression baselines.

