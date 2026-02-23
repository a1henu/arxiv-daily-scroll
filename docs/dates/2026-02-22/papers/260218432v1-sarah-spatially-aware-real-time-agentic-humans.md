---
layout: default
title: SARAH: Spatially Aware Real-time Agentic Humans
---

# SARAH: Spatially Aware Real-time Agentic Humans
**arXiv**：[2602.18432v1](https://arxiv.org/abs/2602.18432) · [PDF](https://arxiv.org/pdf/2602.18432.pdf)  
**作者**：Evonne Ng, Siwei Zhang, Zhang Chen, Michael Zollhoefer, Alexander Richard  

**一句话要点**：提出SARAH方法，实现实时空间感知的对话式全身运动，用于VR和数字人应用。

**关键词**：空间感知运动, 实时对话代理, 因果Transformer VAE, 流匹配模型, VR部署, 注视控制

## 3 点简述
- 核心问题：现有方法缺乏空间感知，无法使代理实时响应用户位置和运动。
- 方法要点：结合因果Transformer VAE和流匹配模型，处理音频和用户轨迹，并引入可调节的注视评分机制。
- 实验或效果：在Embody 3D数据集上达到SOTA运动质量，超过300 FPS，并在VR系统中实时部署验证。

## 摘要（原文）

> As embodied agents become central to VR, telepresence, and digital human applications, their motion must go beyond speech-aligned gestures: agents should turn toward users, respond to their movement, and maintain natural gaze. Current methods lack this spatial awareness. We close this gap with the first real-time, fully causal method for spatially-aware conversational motion, deployable on a streaming VR headset. Given a user's position and dyadic audio, our approach produces full-body motion that aligns gestures with speech while orienting the agent according to the user. Our architecture combines a causal transformer-based VAE with interleaved latent tokens for streaming inference and a flow matching model conditioned on user trajectory and audio. To support varying gaze preferences, we introduce a gaze scoring mechanism with classifier-free guidance to decouple learning from control: the model captures natural spatial alignment from data, while users can adjust eye contact intensity at inference time. On the Embody 3D dataset, our method achieves state-of-the-art motion quality at over 300 FPS -- 3x faster than non-causal baselines -- while capturing the subtle spatial dynamics of natural conversation. We validate our approach on a live VR system, bringing spatially-aware conversational agents to real-time deployment. Please see https://evonneng.github.io/sarah/ for details.

