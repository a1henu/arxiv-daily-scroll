---
layout: default
title: RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics
---

# RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics
**arXiv**：[2512.13660v1](https://arxiv.org/abs/2512.13660) · [PDF](https://arxiv.org/pdf/2512.13660.pdf)  
**作者**：Enshen Zhou, Cheng Chi, Yibo Li, Jingkun An, Jiayuan Zhang, Shanyu Rong, Yi Han, Yuheng Ji, Mengzhen Liu, Pengwei Wang, Zhongyuan Wang, Lu Sheng, Shanghang Zhang  

**一句话要点**：提出RoboTracer以解决机器人空间追踪中的多步度量推理与空间指代难题

**关键词**：空间追踪, 视觉语言模型, 度量推理, 强化微调, 机器人控制

## 3 点简述
- 核心问题：空间追踪需多步度量推理与复杂空间指代，现有方法难以处理。
- 方法要点：通过通用空间编码器和回归监督解码器增强尺度感知，结合度量敏感奖励进行强化微调。
- 实验或效果：在TraceSpatial-Bench上超越基线，平均成功率79.1%，优于Gemini-2.5-Pro 36%。

## 摘要（原文）

> Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.

