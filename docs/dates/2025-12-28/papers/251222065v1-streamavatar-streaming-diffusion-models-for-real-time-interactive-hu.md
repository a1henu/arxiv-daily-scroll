---
layout: default
title: StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars
---

# StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars
**arXiv**：[2512.22065v1](https://arxiv.org/abs/2512.22065) · [PDF](https://arxiv.org/pdf/2512.22065.pdf)  
**作者**：Zhiyao Sun, Ziqiao Peng, Yifeng Ma, Yi Chen, Zhengguang Zhou, Zixiang Zhou, Guozhen Zhang, Youliang Zhang, Yuan Zhou, Qinglin Lu, Yong-Jin Liu  

**一句话要点**：提出两阶段自回归适应与加速框架，实现实时交互式全身数字人化身生成

**关键词**：实时交互化身, 扩散模型蒸馏, 自回归生成, 全身动作生成, 对抗精炼, 一致性保持

## 3 点简述
- 核心问题：现有扩散模型非因果架构与高计算成本不适合实时流式交互，且交互方法多限于头肩区域
- 方法要点：通过自回归蒸馏和对抗精炼，结合参考汇、参考锚定位置重编码和一致性感知判别器确保长期稳定性
- 实验或效果：在生成质量、实时效率和交互自然度上超越现有方法，支持自然说话与倾听行为及连贯手势

## 摘要（原文）

> Real-time, streaming interactive avatars represent a critical yet challenging goal in digital human research. Although diffusion-based human avatar generation methods achieve remarkable success, their non-causal architecture and high computational costs make them unsuitable for streaming. Moreover, existing interactive approaches are typically limited to head-and-shoulder region, limiting their ability to produce gestures and body motions. To address these challenges, we propose a two-stage autoregressive adaptation and acceleration framework that applies autoregressive distillation and adversarial refinement to adapt a high-fidelity human video diffusion model for real-time, interactive streaming. To ensure long-term stability and consistency, we introduce three key components: a Reference Sink, a Reference-Anchored Positional Re-encoding (RAPR) strategy, and a Consistency-Aware Discriminator. Building on this framework, we develop a one-shot, interactive, human avatar model capable of generating both natural talking and listening behaviors with coherent gestures. Extensive experiments demonstrate that our method achieves state-of-the-art performance, surpassing existing approaches in generation quality, real-time efficiency, and interaction naturalness. Project page: https://streamavatar.github.io .

