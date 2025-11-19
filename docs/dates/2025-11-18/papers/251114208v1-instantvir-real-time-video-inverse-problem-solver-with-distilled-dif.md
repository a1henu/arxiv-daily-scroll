---
layout: default
title: InstantViR: Real-Time Video Inverse Problem Solver with Distilled Diffusion Prior
---

# InstantViR: Real-Time Video Inverse Problem Solver with Distilled Diffusion Prior
**arXiv**：[2511.14208v1](https://arxiv.org/abs/2511.14208) · [PDF](https://arxiv.org/pdf/2511.14208.pdf)  
**作者**：Weimin Bai, Suzhe Xu, Yiwei Ren, Jinhua Hao, Ming Sun, Wenzheng Chen, He Sun  

**一句话要点**：提出InstantViR以解决实时视频重建问题，通过蒸馏扩散先验实现高效推理。

**关键词**：视频逆问题, 扩散模型, 知识蒸馏, 实时推理, 视频重建, 潜在空间处理

## 3 点简述
- 视频逆问题需高感知质量与低延迟，但现有扩散方法存在时间伪影或速度慢。
- 方法蒸馏双向视频扩散模型为因果自回归学生，单次前向传递完成重建。
- 实验显示在多种任务中质量匹配或超越基线，运行速度达35 FPS以上。

## 摘要（原文）

> Video inverse problems are fundamental to streaming, telepresence, and AR/VR, where high perceptual quality must coexist with tight latency constraints. Diffusion-based priors currently deliver state-of-the-art reconstructions, but existing approaches either adapt image diffusion models with ad hoc temporal regularizers - leading to temporal artifacts - or rely on native video diffusion models whose iterative posterior sampling is far too slow for real-time use. We introduce InstantViR, an amortized inference framework for ultra-fast video reconstruction powered by a pre-trained video diffusion prior. We distill a powerful bidirectional video diffusion model (teacher) into a causal autoregressive student that maps a degraded video directly to its restored version in a single forward pass, inheriting the teacher's strong temporal modeling while completely removing iterative test-time optimization. The distillation is prior-driven: it only requires the teacher diffusion model and known degradation operators, and does not rely on externally paired clean/noisy video data. To further boost throughput, we replace the video-diffusion backbone VAE with a high-efficiency LeanVAE via an innovative teacher-space regularized distillation scheme, enabling low-latency latent-space processing. Across streaming random inpainting, Gaussian deblurring and super-resolution, InstantViR matches or surpasses the reconstruction quality of diffusion-based baselines while running at over 35 FPS on NVIDIA A100 GPUs, achieving up to 100 times speedups over iterative video diffusion solvers. These results show that diffusion-based video reconstruction is compatible with real-time, interactive, editable, streaming scenarios, turning high-quality video restoration into a practical component of modern vision systems.

