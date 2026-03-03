---
layout: default
title: Unifying Language-Action Understanding and Generation for Autonomous Driving
---

# Unifying Language-Action Understanding and Generation for Autonomous Driving
**arXiv**：[2603.01441v1](https://arxiv.org/abs/2603.01441) · [PDF](https://arxiv.org/pdf/2603.01441.pdf)  
**作者**：Xinyang Wang, Qian Liu, Wenjie Ding, Zhao Yang, Wei Li, Chang Liu, Bailin Li, Kun Zhan, Xianpeng Lang, Wei Chen  

**一句话要点**：提出LinkVLA架构以解决自动驾驶中语言-动作对齐与生成效率问题

**关键词**：自动驾驶, 视觉-语言-动作模型, 多模态对齐, 动作生成, 推理效率

## 3 点简述
- 核心问题：现有VLA模型存在语言指令与动作输出不对齐及自回归生成效率低的问题
- 方法要点：通过共享离散码书统一语言与动作表示，并引入动作理解目标增强语义映射
- 实验或效果：在闭环驾驶基准测试中提升指令遵循准确性与驾驶性能，推理时间减少86%

## 摘要（原文）

> Vision-Language-Action (VLA) models are emerging as a promising paradigm for end-to-end autonomous driving, valued for their potential to leverage world knowledge and reason about complex driving scenes. However, existing methods suffer from two critical limitations: a persistent misalignment between language instructions and action outputs, and the inherent inefficiency of typical auto-regressive action generation. In this paper, we introduce LinkVLA, a novel architecture that directly addresses these challenges to enhance both alignment and efficiency. First, we establish a structural link by unifying language and action tokens into a shared discrete codebook, processed within a single multi-modal model. This structurally enforces cross-modal consistency from the ground up. Second, to create a deep semantic link, we introduce an auxiliary action understanding objective that trains the model to generate descriptive captions from trajectories, fostering a bidirectional language-action mapping. Finally, we replace the slow, step-by-step generation with a two-step coarse-to-fine generation method C2F that efficiently decodes the action sequence, saving 86% inference time. Experiments on closed-loop driving benchmarks show consistent gains in instruction following accuracy and driving performance, alongside reduced inference latency.

