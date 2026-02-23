---
layout: default
title: TempoNet: Slack-Quantized Transformer-Guided Reinforcement Scheduler for Adaptive Deadline-Centric Real-Time Dispatchs
---

# TempoNet: Slack-Quantized Transformer-Guided Reinforcement Scheduler for Adaptive Deadline-Centric Real-Time Dispatchs
**arXiv**：[2602.18109v1](https://arxiv.org/abs/2602.18109) · [PDF](https://arxiv.org/pdf/2602.18109.pdf)  
**作者**：Rong Fu, Yibo Meng, Guangzhen Yao, Jiaxuan Lu, Zeyu Zhang, Zhaolu Kang, Ziming Guo, Jia Yee Tan, Xiaojing Du, Simon James Fong  

**一句话要点**：提出TempoNet，一种基于Transformer和深度Q学习的强化学习调度器，用于自适应截止时间导向的实时调度。

**关键词**：实时调度, 强化学习, Transformer, 深度Q学习, 截止时间导向, 多处理器调度

## 3 点简述
- 核心问题：实时调度需在严格计算预算下处理紧截止时间，传统方法可能不足。
- 方法要点：结合Transformer和深度Q学习，通过Urgency Tokenizer量化时间松弛度，并采用稀疏注意力实现高效推理。
- 实验或效果：在工业混合关键性追踪和多处理器设置中，相比分析调度器和神经基线，提高了截止时间满足率和优化稳定性。

## 摘要（原文）

> Real-time schedulers must reason about tight deadlines under strict compute budgets. We present TempoNet, a reinforcement learning scheduler that pairs a permutation-invariant Transformer with a deep Q-approximation. An Urgency Tokenizer discretizes temporal slack into learnable embeddings, stabilizing value learning and capturing deadline proximity. A latency-aware sparse attention stack with blockwise top-k selection and locality-sensitive chunking enables global reasoning over unordered task sets with near-linear scaling and sub-millisecond inference. A multicore mapping layer converts contextualized Q-scores into processor assignments through masked-greedy selection or differentiable matching. Extensive evaluations on industrial mixed-criticality traces and large multiprocessor settings show consistent gains in deadline fulfillment over analytic schedulers and neural baselines, together with improved optimization stability. Diagnostics include sensitivity analyses for slack quantization, attention-driven policy interpretation, hardware-in-the-loop and kernel micro-benchmarks, and robustness under stress with simple runtime mitigations; we also report sample-efficiency benefits from behavioral-cloning pretraining and compatibility with an actor-critic variant without altering the inference pipeline. These results establish a practical framework for Transformer-based decision making in high-throughput real-time scheduling.

