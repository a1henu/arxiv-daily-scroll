---
layout: default
title: Model-Aware Rate-Distortion Limits for Task-Oriented Source Coding
---

# Model-Aware Rate-Distortion Limits for Task-Oriented Source Coding
**arXiv**：[2602.12866v1](https://arxiv.org/abs/2602.12866) · [PDF](https://arxiv.org/pdf/2602.12866.pdf)  
**作者**：Andriy Enttsel, Vincent Corlay  

**一句话要点**：提出任务模型感知的率失真界限，以优化面向任务的源编码在现实部署中的性能。

**关键词**：面向任务的源编码, 率失真理论, 任务模型感知, 间接率失真, 分类基准, 发射端复杂度

## 3 点简述
- 核心问题：现有面向任务的源编码率失真界限依赖强假设，忽略任务模型不完美性和架构约束。
- 方法要点：基于间接率失真理论，引入任务模型感知的率失真界限，考虑模型次优性和约束。
- 实验或效果：在标准分类基准上验证，当前学习型方案远未达到界限，发射端复杂度是关键瓶颈。

## 摘要（原文）

> Task-Oriented Source Coding (TOSC) has emerged as a paradigm for efficient visual data communication in machine-centric inference systems, where bitrate, latency, and task performance must be jointly optimized under resource constraints. While recent works have proposed rate-distortion bounds for coding for machines, these results often rely on strong assumptions on task identifiability and neglect the impact of deployed task models. In this work, we revisit the fundamental limits of single-TOSC through the lens of indirect rate-distortion theory. We highlight the conditions under which existing rate-distortion bounds are achievable and show their limitations in realistic settings. We then introduce task model-aware rate-distortion bounds that account for task model suboptimality and architectural constraints. Experiments on standard classification benchmarks confirm that current learned TOSC schemes operate far from these limits, highlighting transmitter-side complexity as a key bottleneck.

