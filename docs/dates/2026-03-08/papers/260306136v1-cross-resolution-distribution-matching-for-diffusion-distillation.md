---
layout: default
title: Cross-Resolution Distribution Matching for Diffusion Distillation
---

# Cross-Resolution Distribution Matching for Diffusion Distillation
**arXiv**：[2603.06136v1](https://arxiv.org/abs/2603.06136) · [PDF](https://arxiv.org/pdf/2603.06136.pdf)  
**作者**：Feiyang Chen, Hongpeng Pan, Haonan Xu, Xinyu Duan, Yang Yang, Zhefeng Wang  

**一句话要点**：提出跨分辨率分布匹配蒸馏以解决扩散蒸馏中跨分辨率分布差距问题，实现高保真多分辨率快速推理。

**关键词**：扩散蒸馏, 跨分辨率分布匹配, 多分辨率推理, 加速生成, 高保真图像生成

## 3 点简述
- 核心问题：现有扩散蒸馏方法在部分时间步低分辨率生成时，因跨分辨率分布差距导致质量下降。
- 方法要点：基于logSNR曲线划分时间步间隔，引入分布匹配和噪声重注入机制，补偿分辨率变化。
- 实验或效果：在SDXL和Wan2.1-14B上分别实现33.4倍和25.6倍加速，同时保持高视觉保真度。

## 摘要（原文）

> Diffusion distillation is central to accelerating image and video generation, yet existing methods are fundamentally limited by the denoising process, where step reduction has largely saturated. Partial timestep low-resolution generation can further accelerate inference, but it suffers noticeable quality degradation due to cross-resolution distribution gaps. We propose Cross-Resolution Distribution Matching Distillation (RMD), a novel distillation framework that bridges cross-resolution distribution gaps for high-fidelity, few-step multi-resolution cascaded inference. Specifically, RMD divides the timestep intervals for each resolution using logarithmic signal-to-noise ratio (logSNR) curves, and introduces logSNR-based mapping to compensate for resolution-induced shifts. Distribution matching is conducted along resolution trajectories to reduce the gap between low-resolution generator distributions and the teacher's high-resolution distribution. In addition, a predicted-noise re-injection mechanism is incorporated during upsampling to stabilize training and improve synthesis quality. Quantitative and qualitative results show that RMD preserves high-fidelity generation while accelerating inference across various backbones. Notably, RMD achieves up to 33.4X speedup on SDXL and 25.6X on Wan2.1-14B, while preserving high visual fidelity.

