---
layout: default
title: PocketDP3: Efficient Pocket-Scale 3D Visuomotor Policy
---

# PocketDP3: Efficient Pocket-Scale 3D Visuomotor Policy
**arXiv**：[2601.22018v1](https://arxiv.org/abs/2601.22018) · [PDF](https://arxiv.org/pdf/2601.22018.pdf)  
**作者**：Jinhao Zhang, Zhexuan Zhou, Huizhe Li, Yichen Lai, Wenlong Xia, Haoming Song, Youmin Gong, Jie Me  

**一句话要点**：提出PocketDP3以解决3D视觉扩散策略中解码器参数浪费问题，实现高效机器人操作。

**关键词**：3D视觉策略, 扩散模型, 机器人操作, 轻量解码器, 高效推理, 点云编码

## 3 点简述
- 核心问题：现有3D视觉扩散策略中，高效点云编码器与庞大解码器不匹配，导致参数浪费。
- 方法要点：用基于MLP-Mixer块的轻量Diffusion Mixer替换条件U-Net解码器，实现时空和通道维度高效融合。
- 实验或效果：在模拟基准上以少于1%参数实现SOTA性能，支持两步推理加速，真实世界实验验证实用性。

## 摘要（原文）

> Recently, 3D vision-based diffusion policies have shown strong capability in learning complex robotic manipulation skills. However, a common architectural mismatch exists in these models: a tiny yet efficient point-cloud encoder is often paired with a massive decoder. Given a compact scene representation, we argue that this may lead to substantial parameter waste in the decoder. Motivated by this observation, we propose PocketDP3, a pocket-scale 3D diffusion policy that replaces the heavy conditional U-Net decoder used in prior methods with a lightweight Diffusion Mixer (DiM) built on MLP-Mixer blocks. This architecture enables efficient fusion across temporal and channel dimensions, significantly reducing model size. Notably, without any additional consistency distillation techniques, our method supports two-step inference without sacrificing performance, improving practicality for real-time deployment. Across three simulation benchmarks--RoboTwin2.0, Adroit, and MetaWorld--PocketDP3 achieves state-of-the-art performance with fewer than 1% of the parameters of prior methods, while also accelerating inference. Real-world experiments further demonstrate the practicality and transferability of our method in real-world settings. Code will be released.

