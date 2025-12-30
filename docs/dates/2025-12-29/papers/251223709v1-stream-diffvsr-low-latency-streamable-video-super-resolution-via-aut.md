---
layout: default
title: Stream-DiffVSR: Low-Latency Streamable Video Super-Resolution via Auto-Regressive Diffusion
---

# Stream-DiffVSR: Low-Latency Streamable Video Super-Resolution via Auto-Regressive Diffusion
**arXiv**：[2512.23709v1](https://arxiv.org/abs/2512.23709) · [PDF](https://arxiv.org/pdf/2512.23709.pdf)  
**作者**：Hau-Shiang Shiu, Chin-Yang Lin, Zhixiang Wang, Chi-Wei Hsiao, Po-Fan Yu, Yu-Chih Chen, Yu-Lun Liu  

**一句话要点**：提出Stream-DiffVSR，通过自回归扩散实现低延迟可流式视频超分辨率

**关键词**：视频超分辨率, 扩散模型, 低延迟处理, 在线部署, 因果条件框架, 蒸馏去噪

## 3 点简述
- 基于扩散的视频超分辨率方法依赖未来帧和多步去噪，导致高延迟，不适用于在线场景。
- 结合四步蒸馏去噪器、自回归时间引导模块和轻量级时间感知解码器，实现因果条件扩散框架。
- 在RTX4090 GPU上处理720p帧仅需0.328秒，显著提升感知质量并降低延迟超过130倍。

## 摘要（原文）

> Diffusion-based video super-resolution (VSR) methods achieve strong perceptual quality but remain impractical for latency-sensitive settings due to reliance on future frames and expensive multi-step denoising. We propose Stream-DiffVSR, a causally conditioned diffusion framework for efficient online VSR. Operating strictly on past frames, it combines a four-step distilled denoiser for fast inference, an Auto-regressive Temporal Guidance (ARTG) module that injects motion-aligned cues during latent denoising, and a lightweight temporal-aware decoder with a Temporal Processor Module (TPM) that enhances detail and temporal coherence. Stream-DiffVSR processes 720p frames in 0.328 seconds on an RTX4090 GPU and significantly outperforms prior diffusion-based methods. Compared with the online SOTA TMP, it boosts perceptual quality (LPIPS +0.095) while reducing latency by over 130x. Stream-DiffVSR achieves the lowest latency reported for diffusion-based VSR, reducing initial delay from over 4600 seconds to 0.328 seconds, thereby making it the first diffusion VSR method suitable for low-latency online deployment. Project page: https://jamichss.github.io/stream-diffvsr-project-page/

