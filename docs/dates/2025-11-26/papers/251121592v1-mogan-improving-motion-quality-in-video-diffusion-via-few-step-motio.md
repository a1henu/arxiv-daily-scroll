---
layout: default
title: MoGAN: Improving Motion Quality in Video Diffusion via Few-Step Motion Adversarial Post-Training
---

# MoGAN: Improving Motion Quality in Video Diffusion via Few-Step Motion Adversarial Post-Training
**arXiv**：[2511.21592v1](https://arxiv.org/abs/2511.21592) · [PDF](https://arxiv.org/pdf/2511.21592.pdf)  
**作者**：Haotian Xue, Qi Chen, Zhonghao Wang, Xun Huang, Eli Shechtman, Jinrong Xie, Yongxin Chen  

**一句话要点**：提出MoGAN后训练框架以提升视频扩散模型中的运动质量

**关键词**：视频扩散模型, 运动质量提升, 后训练框架, 光流判别器, 分布匹配正则化, 蒸馏训练

## 3 点简述
- 视频扩散模型存在运动不连贯、抖动和动态不真实问题，缺乏时间一致性监督
- 方法基于3步蒸馏模型，训练光流判别器区分真实与生成运动，并添加分布匹配正则化
- 实验显示在VBench和VideoJAM-Bench上运动分数显著提升，人类研究偏好MoGAN运动质量

## 摘要（原文）

> Video diffusion models achieve strong frame-level fidelity but still struggle with motion coherence, dynamics and realism, often producing jitter, ghosting, or implausible dynamics. A key limitation is that the standard denoising MSE objective provides no direct supervision on temporal consistency, allowing models to achieve low loss while still generating poor motion. We propose MoGAN, a motion-centric post-training framework that improves motion realism without reward models or human preference data. Built atop a 3-step distilled video diffusion model, we train a DiT-based optical-flow discriminator to differentiate real from generated motion, combined with a distribution-matching regularizer to preserve visual fidelity. With experiments on Wan2.1-T2V-1.3B, MoGAN substantially improves motion quality across benchmarks. On VBench, MoGAN boosts motion score by +7.3% over the 50-step teacher and +13.3% over the 3-step DMD model. On VideoJAM-Bench, MoGAN improves motion score by +7.4% over the teacher and +8.8% over DMD, while maintaining comparable or even better aesthetic and image-quality scores. A human study further confirms that MoGAN is preferred for motion quality (52% vs. 38% for the teacher; 56% vs. 29% for DMD). Overall, MoGAN delivers significantly more realistic motion without sacrificing visual fidelity or efficiency, offering a practical path toward fast, high-quality video generation. Project webpage is: https://xavihart.github.io/mogan.

