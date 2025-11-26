---
layout: default
title: Gated Uncertainty-Aware Runtime Dual Invariants for Neural Signal-Controlled Robotics
---

# Gated Uncertainty-Aware Runtime Dual Invariants for Neural Signal-Controlled Robotics
**arXiv**：[2511.20570v1](https://arxiv.org/abs/2511.20570) · [PDF](https://arxiv.org/pdf/2511.20570.pdf)  
**作者**：Tasha Kim, Oiwi Parker Jones  

**一句话要点**：提出GUARDIAN框架以解决神经信号控制机器人系统的安全与可靠性问题

**关键词**：神经信号控制, 运行时监控, 安全验证, 脑机接口, 机器人系统

## 3 点简述
- 核心问题：神经信号控制的安全关键辅助系统需确保可靠性和信任
- 方法要点：结合置信度校准脑信号解码与符号目标接地及双层运行时监控
- 实验或效果：在BNCI2014数据集上实现94-97%安全率，延迟低于毫秒级

## 摘要（原文）

> Safety-critical assistive systems that directly decode user intent from neural signals require rigorous guarantees of reliability and trust. We present GUARDIAN (Gated Uncertainty-Aware Runtime Dual Invariants), a framework for real-time neuro-symbolic verification for neural signal-controlled robotics. GUARDIAN enforces both logical safety and physiological trust by coupling confidence-calibrated brain signal decoding with symbolic goal grounding and dual-layer runtime monitoring. On the BNCI2014 motor imagery electroencephalogram (EEG) dataset with 9 subjects and 5,184 trials, the system performs at a high safety rate of 94-97% even with lightweight decoder architectures with low test accuracies (27-46%) and high ECE confidence miscalibration (0.22-0.41). We demonstrate 1.7x correct interventions in simulated noise testing versus at baseline. The monitor operates at 100Hz and sub-millisecond decision latency, making it practically viable for closed-loop neural signal-based systems. Across 21 ablation results, GUARDIAN exhibits a graduated response to signal degradation, and produces auditable traces from intent, plan to action, helping to link neural evidence to verifiable robot action.

