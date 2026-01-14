---
layout: default
title: Teaching Robots Like Dogs: Learning Agile Navigation from Luring, Gesture, and Speech
---

# Teaching Robots Like Dogs: Learning Agile Navigation from Luring, Gesture, and Speech
**arXiv**：[2601.08422v1](https://arxiv.org/abs/2601.08422) · [PDF](https://arxiv.org/pdf/2601.08422.pdf)  
**作者**：Taerim Yoon, Dongho Kang, Jin Cheng, Fatemeh Zargarbashi, Yijiang Huang, Minsung Ahn, Stelian Coros, Sungjoon Choi  

**一句话要点**：提出人机交互框架，使腿式机器人通过多模态输入学习敏捷导航

**关键词**：腿式机器人导航, 人机交互学习, 多模态输入控制, 物理仿真训练, 渐进目标提示

## 3 点简述
- 核心问题：物理人机交互数据收集负担重，影响机器人学习效率。
- 方法要点：基于物理仿真重建交互场景，采用渐进目标提示策略优化训练。
- 实验或效果：在六种真实场景中实现97.15%任务成功率，数据需求低于1小时。

## 摘要（原文）

> In this work, we aim to enable legged robots to learn how to interpret human social cues and produce appropriate behaviors through physical human guidance. However, learning through physical engagement can place a heavy burden on users when the process requires large amounts of human-provided data. To address this, we propose a human-in-the-loop framework that enables robots to acquire navigational behaviors in a data-efficient manner and to be controlled via multimodal natural human inputs, specifically gestural and verbal commands. We reconstruct interaction scenes using a physics-based simulation and aggregate data to mitigate distributional shifts arising from limited demonstration data. Our progressive goal cueing strategy adaptively feeds appropriate commands and navigation goals during training, leading to more accurate navigation and stronger alignment between human input and robot behavior. We evaluate our framework across six real-world agile navigation scenarios, including jumping over or avoiding obstacles. Our experimental results show that our proposed method succeeds in almost all trials across these scenarios, achieving a 97.15% task success rate with less than 1 hour of demonstration data in total.

