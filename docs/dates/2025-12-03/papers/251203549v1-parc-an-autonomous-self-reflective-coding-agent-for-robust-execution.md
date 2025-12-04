---
layout: default
title: PARC: An Autonomous Self-Reflective Coding Agent for Robust Execution of Long-Horizon Tasks
---

# PARC: An Autonomous Self-Reflective Coding Agent for Robust Execution of Long-Horizon Tasks
**arXiv**：[2512.03549v1](https://arxiv.org/abs/2512.03549) · [PDF](https://arxiv.org/pdf/2512.03549.pdf)  
**作者**：Yuki Orimo, Iori Kurata, Hodaka Mori, Ryuhei Okuno, Ryohto Sawada, Daisuke Okanohara  

**一句话要点**：提出PARC自主编码代理，通过分层多代理架构与自评估反馈机制，实现长时程计算任务的鲁棒执行。

**关键词**：自主编码代理, 分层多代理系统, 自评估反馈, 长时程任务执行, 计算科学, 数据科学

## 3 点简述
- 核心问题：长时程计算任务中，AI系统需自主检测和纠正高层策略错误，以维持进展。
- 方法要点：采用分层多代理架构，集成任务规划、执行和自评估反馈机制，实现独立上下文中的动作评估与修正。
- 实验或效果：在材料科学中自主复现锂离子传导和合金偏析研究结果，管理数十个并行模拟任务；在Kaggle实验中，从自然语言指令出发，生成与人工基线竞争的数据分析解决方案。

## 摘要（原文）

> We introduce PARC, a coding agent for the autonomous and robust execution of long-horizon computational tasks. PARC is built on a hierarchical multi-agent architecture incorporating task planning, execution, and a mechanism that evaluates its own actions and their outcomes from an independent context and provides feedback, namely self-assessment and self-feedback. This design enables PARC to detect and correct high-level strategic errors and sustain progress without human intervention. We evaluate PARC across computational science and data science tasks. In materials science, it autonomously reproduces key results from studies on lithium-ion conduction and alloy segregation. In particular, it coordinates dozens of parallel simulation tasks, each requiring roughly 43 hours of computation, managing orchestration, monitoring, and error correction end-to-end. In Kaggle-based experiments, starting from minimal natural-language instructions, PARC conducts data analysis and implements search strategies, producing solutions competitive with human-engineered baselines. These results highlight the potential of integrating a hierarchical multi-agent system with self-assessment and self-feedback to enable AI systems capable of independent, large-scale scientific and analytical work.

