---
layout: default
title: Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic
---

# Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic
**arXiv**：[2601.16486v1](https://arxiv.org/abs/2601.16486) · [PDF](https://arxiv.org/pdf/2601.16486.pdf)  
**作者**：Yichuan Ma, Linyang Li, Yongkang chen, Peiji Li, Xiaozhe Li, Qipeng Guo, Dahua Lin, Kai Chen  

**一句话要点**：提出Timely Machine以解决代理场景中基于生成长度的测试时间定义失效问题

**关键词**：测试时间缩放, 代理场景, 时间预算感知, 强化学习, 工具调用延迟, 基准测试

## 3 点简述
- 核心问题：代理场景中工具调用延迟导致传统基于生成长度的测试时间定义失效
- 方法要点：重新定义测试时间为挂钟时间，引入Timely-RL增强时间预算感知
- 实验或效果：通过Timely-Eval基准测试，Timely-RL提升时间预算意识并一致提升性能

## 摘要（原文）

> As large language models (LLMs) increasingly tackle complex reasoning tasks, test-time scaling has become critical for enhancing capabilities. However, in agentic scenarios with frequent tool calls, the traditional generation-length-based definition breaks down: tool latency decouples inference time from generation length. We propose Timely Machine, redefining test-time as wall-clock time, where models dynamically adjust strategies based on time budgets. We introduce Timely-Eval, a benchmark spanning high-frequency tool calls, low-frequency tool calls, and time-constrained reasoning. By varying tool latency, we find smaller models excel with fast feedback through more interactions, while larger models dominate high-latency settings via superior interaction quality. Moreover, existing models fail to adapt reasoning to time budgets. We propose Timely-RL to address this gap. After cold-start supervised fine-tuning, we use reinforcement learning to enhance temporal planning. Timely-RL improves time budget awareness and consistently boosts performance across Timely-Eval. We hope our work offers a new perspective on test-time scaling for the agentic era.

