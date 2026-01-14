---
layout: default
title: ZeroDVFS: Zero-Shot LLM-Guided Core and Frequency Allocation for Embedded Platforms
---

# ZeroDVFS: Zero-Shot LLM-Guided Core and Frequency Allocation for Embedded Platforms
**arXiv**：[2601.08166v1](https://arxiv.org/abs/2601.08166) · [PDF](https://arxiv.org/pdf/2601.08166.pdf)  
**作者**：Mohammad Pivezhandi, Mahdi Banisharif, Abusayeed Saifullah, Ali Jannesari  

**一句话要点**：提出基于LLM和多智能体强化学习的零样本调度框架，用于嵌入式平台的热能与能耗管理。

**关键词**：动态电压频率缩放, 多智能体强化学习, 零样本学习, 嵌入式系统调度, 热能管理

## 3 点简述
- 核心问题：现有DVFS和核心分配方法依赖启发式或离线分析，无法适应动态运行时环境。
- 方法要点：采用分层多智能体强化学习，结合LLM提取语义特征，实现零样本部署和快速决策。
- 实验或效果：在多个嵌入式平台上，相比Linux ondemand governor，能效提升7.09倍，调度时间缩短4.0倍。

## 摘要（原文）

> Dynamic voltage and frequency scaling (DVFS) and task-to-core allocation are critical for thermal management and balancing energy and performance in embedded systems. Existing approaches either rely on utilization-based heuristics that overlook stall times, or require extensive offline profiling for table generation, preventing runtime adaptation. We propose a model-based hierarchical multi-agent reinforcement learning (MARL) framework for thermal- and energy-aware scheduling on multi-core platforms. Two collaborative agents decompose the exponential action space, achieving 358ms latency for subsequent decisions. First decisions require 3.5 to 8.0s including one-time LLM feature extraction. An accurate environment model leverages regression techniques to predict thermal dynamics and performance states. When combined with LLM-extracted semantic features, the environment model enables zero-shot deployment for new workloads on trained platforms by generating synthetic training data without requiring workload-specific profiling samples. We introduce LLM-based semantic feature extraction that characterizes OpenMP programs through 13 code-level features without execution. The Dyna-Q-inspired framework integrates direct reinforcement learning with model-based planning, achieving 20x faster convergence than model-free methods. Experiments on BOTS and PolybenchC benchmarks across NVIDIA Jetson TX2, Jetson Orin NX, RubikPi, and Intel Core i7 demonstrate 7.09x better energy efficiency and 4.0x better makespan than Linux ondemand governor. First-decision latency is 8,300x faster than table-based profiling, enabling practical deployment in dynamic embedded systems.

