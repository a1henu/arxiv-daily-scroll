---
layout: default
title: EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection
---

# EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection
**arXiv**：[2603.04900v1](https://arxiv.org/abs/2603.04900) · [PDF](https://arxiv.org/pdf/2603.04900.pdf)  
**作者**：Shuo Yang, Soyeon Caren Han, Xueqi Ma, Yan Li, Mohammad Reza Ghasemi Madani, Eduard Hovy  

**一句话要点**：提出EvoTool框架，通过进化算法优化LLM代理的模块化工具使用策略，解决延迟监督和信用分配问题。

**关键词**：LLM代理, 工具使用策略, 进化算法, 模块化优化, 信用分配, 自我进化

## 3 点简述
- 核心问题：LLM代理工具使用策略优化面临延迟监督和长轨迹信用分配困难，现有方法易行为纠缠或忽略跨模块错误传播。
- 方法要点：将策略分解为四个模块，采用轨迹归因、反馈引导突变和多样性选择机制进行无梯度进化优化。
- 实验或效果：在四个基准测试中，EvoTool在GPT-4.1和Qwen3-8B上超越基线超过5点，效率和可转移性更优。

## 摘要（原文）

> LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

