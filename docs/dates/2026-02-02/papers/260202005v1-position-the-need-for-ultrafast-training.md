---
layout: default
title: Position: The Need for Ultrafast Training
---

# Position: The Need for Ultrafast Training
**arXiv**：[2602.02005v1](https://arxiv.org/abs/2602.02005) · [PDF](https://arxiv.org/pdf/2602.02005.pdf)  
**作者**：Duc Hoang  

**一句话要点**：提出超快片上学习以解决非平稳高频环境中模型更新延迟问题

**关键词**：超快片上学习, FPGA加速, 实时系统, 非平稳环境, 亚微秒延迟, 闭环控制

## 3 点简述
- 核心问题：现有FPGA加速器仅支持静态模型离线推理，学习与适应依赖慢速CPU/GPU，限制实时系统性能。
- 方法要点：倡导从仅推理加速转向超快片上学习，在FPGA架构内实现确定性的亚微秒级延迟推理与训练。
- 实验或效果：未知，但预期应用包括量子纠错、等离子体控制和自主科学实验等闭环系统。

## 摘要（原文）

> Domain-specialized FPGAs have delivered unprecedented performance for low-latency inference across scientific and industrial workloads, yet nearly all existing accelerators assume static models trained offline, relegating learning and adaptation to slower CPUs or GPUs. This separation fundamentally limits systems that must operate in non-stationary, high-frequency environments, where model updates must occur at the timescale of the underlying physics. In this paper, I argue for a shift from inference-only accelerators to ultrafast on-chip learning, in which both inference and training execute directly within the FPGA fabric under deterministic, sub-microsecond latency constraints. Bringing learning into the same real-time datapath as inference would enable closed-loop systems that adapt as fast as the physical processes they control, with applications spanning quantum error correction, cryogenic qubit calibration, plasma and fusion control, accelerator tuning, and autonomous scientific experiments. Enabling such regimes requires rethinking algorithms, architectures, and toolflows jointly, but promises to transform FPGAs from static inference engines into real-time learning machines.

