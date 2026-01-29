---
layout: default
title: MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment
---

# MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment
**arXiv**：[2601.20335v1](https://arxiv.org/abs/2601.20335) · [PDF](https://arxiv.org/pdf/2601.20335.pdf)  
**作者**：Qinzhuo Wu, Zhizhuo Yang, Hanhao Li, Pengzhi Gao, Wei Liu, Jian Luan  

**一句话要点**：提出MobileBench-OL在线基准，以评估移动GUI代理在真实环境中的综合能力。

**关键词**：移动GUI代理, 在线基准, 真实环境评估, 复杂推理, 噪声鲁棒性, 自动评估框架

## 3 点简述
- 核心问题：现有在线基准忽视代理的推理、探索能力和真实环境噪声，导致与真实环境脱节。
- 方法要点：构建包含1080个任务的在线基准，通过5个子集评估任务执行、复杂推理和噪声鲁棒性，并提供自动评估框架。
- 实验或效果：评估12个领先GUI代理显示其性能有显著提升空间，人类评估确认基准能可靠测量真实环境表现。

## 摘要（原文）

> Recent advances in mobile Graphical User Interface (GUI) agents highlight the growing need for comprehensive evaluation benchmarks. While new online benchmarks offer more realistic testing than offline ones, they tend to focus on the agents' task instruction-following ability while neglecting their reasoning and exploration ability. Moreover, these benchmarks do not consider the random noise in real-world mobile environments. This leads to a gap between benchmarks and real-world environments. To addressing these limitations, we propose MobileBench-OL, an online benchmark with 1080 tasks from 80 Chinese apps. It measures task execution, complex reasoning, and noise robustness of agents by including 5 subsets, which set multiple evaluation dimensions. We also provide an auto-eval framework with a reset mechanism, enabling stable and repeatable real-world benchmarking. Evaluating 12 leading GUI agents on MobileBench-OL shows significant room for improvement to meet real-world requirements. Human evaluation further confirms that MobileBench-OL can reliably measure the performance of leading GUI agents in real environments. Our data and code will be released upon acceptance.

