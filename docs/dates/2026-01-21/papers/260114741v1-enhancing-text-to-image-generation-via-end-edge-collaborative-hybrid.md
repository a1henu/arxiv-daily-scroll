---
layout: default
title: Enhancing Text-to-Image Generation via End-Edge Collaborative Hybrid Super-Resolution
---

# Enhancing Text-to-Image Generation via End-Edge Collaborative Hybrid Super-Resolution
**arXiv**：[2601.14741v1](https://arxiv.org/abs/2601.14741) · [PDF](https://arxiv.org/pdf/2601.14741.pdf)  
**作者**：Chongbin Yi, Yuxin Liang, Ziqi Zhou, Peng Yang  

**一句话要点**：提出端边协同混合超分辨率框架以降低文本到图像生成延迟并保持图像质量

**关键词**：文本到图像生成, 超分辨率, 端边协同, 混合模型, 延迟优化

## 3 点简述
- 核心问题：高分辨率文本到图像生成面临延迟与图像保真度之间的权衡挑战
- 方法要点：采用端边协同框架，结合扩散模型和轻量学习模型进行区域感知混合超分辨率
- 实验或效果：实验显示系统相比基线减少33%服务延迟，同时保持竞争性图像质量

## 摘要（原文）

> Artificial Intelligence-Generated Content (AIGC) has made significant strides, with high-resolution text-to-image (T2I) generation becoming increasingly critical for improving users' Quality of Experience (QoE). Although resource-constrained edge computing adequately supports fast low-resolution T2I generations, achieving high-resolution output still faces the challenge of ensuring image fidelity at the cost of latency. To address this, we first investigate the performance of super-resolution (SR) methods for image enhancement, confirming a fundamental trade-off that lightweight learning-based SR struggles to recover fine details, while diffusion-based SR achieves higher fidelity at a substantial computational cost. Motivated by these observations, we propose an end-edge collaborative generation-enhancement framework. Upon receiving a T2I generation task, the system first generates a low-resolution image based on adaptively selected denoising steps and super-resolution scales at the edge side, which is then partitioned into patches and processed by a region-aware hybrid SR policy. This policy applies a diffusion-based SR model to foreground patches for detail recovery and a lightweight learning-based SR model to background patches for efficient upscaling, ultimately stitching the enhanced ones into the high-resolution image. Experiments show that our system reduces service latency by 33% compared with baselines while maintaining competitive image quality.

