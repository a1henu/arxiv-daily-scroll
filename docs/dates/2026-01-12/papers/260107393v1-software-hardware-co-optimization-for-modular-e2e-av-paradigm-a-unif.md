---
layout: default
title: Software-Hardware Co-optimization for Modular E2E AV Paradigm: A Unified Framework of Optimization Approaches, Simulation Environment and Evaluation Metrics
---

# Software-Hardware Co-optimization for Modular E2E AV Paradigm: A Unified Framework of Optimization Approaches, Simulation Environment and Evaluation Metrics
**arXiv**：[2601.07393v1](https://arxiv.org/abs/2601.07393) · [PDF](https://arxiv.org/pdf/2601.07393.pdf)  
**作者**：Chengzhi Ji, Xingfeng Li, Zhaodong Lv, Hao Sun, Pan Liu, Hao Frank Yang, Ziyuan Pu  

**一句话要点**：提出软硬件协同优化框架以解决模块化端到端自动驾驶推理的延迟与能耗问题

**关键词**：模块化端到端自动驾驶, 软硬件协同优化, 推理加速, 系统级评估, 能耗优化

## 3 点简述
- 现有研究忽视系统级因素如延迟和能耗，导致模型复杂难以部署
- 框架联合软件模型优化与硬件计算优化，实现系统级目标统一
- 实验显示框架保持驾驶性能，显著降低延迟和能耗，提升系统整体效率

## 摘要（原文）

> Modular end-to-end (ME2E) autonomous driving paradigms combine modular interpretability with global optimization capability and have demonstrated strong performance. However, existing studies mainly focus on accuracy improvement, while critical system-level factors such as inference latency and energy consumption are often overlooked, resulting in increasingly complex model designs that hinder practical deployment. Prior efforts on model compression and acceleration typically optimize either the software or hardware side in isolation. Software-only optimization cannot fundamentally remove intermediate tensor access and operator scheduling overheads, whereas hardware-only optimization is constrained by model structure and precision. As a result, the real-world benefits of such optimizations are often limited. To address these challenges, this paper proposes a reusable software and hardware co-optimization and closed-loop evaluation framework for ME2E autonomous driving inference. The framework jointly integrates software-level model optimization with hardware-level computation optimization under a unified system-level objective. In addition, a multidimensional evaluation metric is introduced to assess system performance by jointly considering safety, comfort, efficiency, latency, and energy, enabling quantitative comparison of different optimization strategies. Experiments across multiple ME2E autonomous driving stacks show that the proposed framework preserves baseline-level driving performance while significantly reducing inference latency and energy consumption, achieving substantial overall system-level improvements. These results demonstrate that the proposed framework provides practical and actionable guidance for efficient deployment of ME2E autonomous driving systems.

