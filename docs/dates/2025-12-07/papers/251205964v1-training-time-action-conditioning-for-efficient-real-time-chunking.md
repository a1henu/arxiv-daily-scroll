---
layout: default
title: Training-Time Action Conditioning for Efficient Real-Time Chunking
---

# Training-Time Action Conditioning for Efficient Real-Time Chunking
**arXiv**：[2512.05964v1](https://arxiv.org/abs/2512.05964) · [PDF](https://arxiv.org/pdf/2512.05964.pdf)  
**作者**：Kevin Black, Allen Z. Ren, Michael Equi, Sergey Levine  

**一句话要点**：提出训练时动作条件化方法，以高效实现实时机器人控制中的动作分块生成。

**关键词**：实时分块, 动作条件化, 机器人控制, 训练优化, 推理延迟

## 3 点简述
- 核心问题：实时分块中推理时修复方法增加计算开销和延迟。
- 方法要点：在训练时模拟推理延迟，直接基于动作前缀进行条件化，无需修改模型架构。
- 实验或效果：在模拟和真实世界任务中，保持性能与速度，计算成本更低。

## 摘要（原文）

> Real-time chunking (RTC) enables vision-language-action models (VLAs) to generate smooth, reactive robot trajectories by asynchronously predicting action chunks and conditioning on previously committed actions via inference-time inpainting. However, this inpainting method introduces computational overhead that increases inference latency. In this work, we propose a simple alternative: simulating inference delay at training time and conditioning on action prefixes directly, eliminating any inference-time overhead. Our method requires no modifications to the model architecture or robot runtime, and can be implemented with only a few additional lines of code. In simulated experiments, we find that training-time RTC outperforms inference-time RTC at higher inference delays. In real-world experiments on box building and espresso making tasks with the $π_{0.6}$ VLA, we demonstrate that training-time RTC maintains both task performance and speed parity with inference-time RTC while being computationally cheaper. Our results suggest that training-time action conditioning is a practical drop-in replacement for inference-time inpainting in real-time robot control.

