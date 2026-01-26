---
layout: default
title: Reward-Forcing: Autoregressive Video Generation with Reward Feedback
---

# Reward-Forcing: Autoregressive Video Generation with Reward Feedback
**arXiv**：[2601.16933v1](https://arxiv.org/abs/2601.16933) · [PDF](https://arxiv.org/pdf/2601.16933.pdf)  
**作者**：Jingran Zhang, Ning Li, Yuanhao Ban, Andrew Bai, Justin Cui  

**一句话要点**：提出Reward-Forcing方法，利用奖励信号引导自回归视频生成，以提升效率和质量。

**关键词**：自回归视频生成, 奖励信号引导, 时序一致性, 视觉保真度, VBench基准

## 3 点简述
- 核心问题：自回归视频生成依赖教师模型，性能受限且落后于双向模型。
- 方法要点：使用奖励信号指导生成过程，简化训练并保持视觉保真度和时序一致性。
- 实验或效果：在VBench上总分为84.92，媲美先进自回归方法，有时超越类似规模双向模型。

## 摘要（原文）

> While most prior work in video generation relies on bidirectional architectures, recent efforts have sought to adapt these models into autoregressive variants to support near real-time generation. However, such adaptations often depend heavily on teacher models, which can limit performance, particularly in the absence of a strong autoregressive teacher, resulting in output quality that typically lags behind their bidirectional counterparts. In this paper, we explore an alternative approach that uses reward signals to guide the generation process, enabling more efficient and scalable autoregressive generation. By using reward signals to guide the model, our method simplifies training while preserving high visual fidelity and temporal consistency. Through extensive experiments on standard benchmarks, we find that our approach performs comparably to existing autoregressive models and, in some cases, surpasses similarly sized bidirectional models by avoiding constraints imposed by teacher architectures. For example, on VBench, our method achieves a total score of 84.92, closely matching state-of-the-art autoregressive methods that score 84.31 but require significant heterogeneous distillation.

