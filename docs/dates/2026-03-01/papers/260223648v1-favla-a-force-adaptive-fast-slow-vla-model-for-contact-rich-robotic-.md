---
layout: default
title: FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation
---

# FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation
**arXiv**：[2602.23648v1](https://arxiv.org/abs/2602.23648) · [PDF](https://arxiv.org/pdf/2602.23648.pdf)  
**作者**：Yao Li, Peiyuan Tang, Wuyang Zhang, Chengyang Zhu, Yifan Duan, Weikai Shi, Xiaodong Zhang, Zijiang Yang, Jianmin Ji, Yanyong Zhang  

**一句话要点**：提出FAVLA模型，通过力自适应快慢VLA架构解决接触丰富机器人操作中的反应延迟问题。

**关键词**：机器人操作, 视觉语言动作模型, 力反馈, 快慢架构, 接触感知控制

## 3 点简述
- 核心问题：现有VLA模型统一频率融合模态，忽略传感器采样率不匹配，导致接触反馈响应延迟。
- 方法要点：采用快慢解耦架构，慢VLM低频规划，快AE高频控制，并引入力适配器动态调整执行频率。
- 实验或效果：在接触丰富任务中显著优于基线，提升反应性和成功率，尤其在较小接触力下表现更优。

## 摘要（原文）

> Force/torque feedback can substantially improve Vision-Language-Action (VLA) models on contact-rich manipulation, but most existing approaches fuse all modalities at a single operating frequency. This design ignores the mismatched sampling rates of real robot sensors, forcing downsampling of the high-frequency contact cues needed for reactive correction. Combined with common VLM-action-expert (AE) pipelines that execute action chunks largely open loop between expensive VLM updates, unified-frequency fusion often yields delayed responses to impacts, stick-slip, and force spikes. We propose FAVLA, a force-adaptive fast-slow VLA that decouples slow perception planning from fast contact-aware control. FAVLA runs a slow VLM at a fixed low frequency to encode modalities to produce latent representations and to predict near-future force variation. A fast AE then executes at a variable high frequency, conditioning on the latest force sequence data to generate reactive actions. We further introduce a force adapter that injects high-frequency force features into multiple AE layers, and adaptively schedules the AE's execution frequency based on the VLM's predicted force variation. Extensive experiments on contact-rich tasks demonstrate that FAVLA significantly outperforms baselines, achieving superior reactivity and success rates, especially with a smaller contact force during manipulation.

