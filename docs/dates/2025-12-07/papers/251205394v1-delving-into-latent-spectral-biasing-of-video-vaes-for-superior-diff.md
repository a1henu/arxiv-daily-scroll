---
layout: default
title: Delving into Latent Spectral Biasing of Video VAEs for Superior Diffusability
---

# Delving into Latent Spectral Biasing of Video VAEs for Superior Diffusability
**arXiv**：[2512.05394v1](https://arxiv.org/abs/2512.05394) · [PDF](https://arxiv.org/pdf/2512.05394.pdf)  
**作者**：Shizhan Liu, Xinran Deng, Zhuoyi Yang, Jiayan Teng, Xiaotao Gu, Jie Tang  

**一句话要点**：提出SSVAE以优化视频VAE的潜在结构，提升扩散模型训练效率与生成质量。

**关键词**：视频生成, 潜在扩散模型, VAE正则化, 频谱分析, 文本到视频

## 3 点简述
- 核心问题：现有视频VAE注重重建保真度，忽略潜在结构对扩散训练的影响。
- 方法要点：通过统计分析识别关键频谱特性，并引入局部相关正则化和潜在掩码重建正则化。
- 实验或效果：SSVAE实现文本到视频生成收敛速度提升3倍，视频奖励增益10%。

## 摘要（原文）

> Latent diffusion models pair VAEs with diffusion backbones, and the structure of VAE latents strongly influences the difficulty of diffusion training. However, existing video VAEs typically focus on reconstruction fidelity, overlooking latent structure. We present a statistical analysis of video VAE latent spaces and identify two spectral properties essential for diffusion training: a spatio-temporal frequency spectrum biased toward low frequencies, and a channel-wise eigenspectrum dominated by a few modes. To induce these properties, we propose two lightweight, backbone-agnostic regularizers: Local Correlation Regularization and Latent Masked Reconstruction. Experiments show that our Spectral-Structured VAE (SSVAE) achieves a $3\times$ speedup in text-to-video generation convergence and a 10\% gain in video reward, outperforming strong open-source VAEs. The code is available at https://github.com/zai-org/SSVAE.

