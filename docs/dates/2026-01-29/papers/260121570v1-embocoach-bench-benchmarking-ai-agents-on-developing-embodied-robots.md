---
layout: default
title: EmboCoach-Bench: Benchmarking AI Agents on Developing Embodied Robots
---

# EmboCoach-Bench: Benchmarking AI Agents on Developing Embodied Robots
**arXiv**：[2601.21570v1](https://arxiv.org/abs/2601.21570) · [PDF](https://arxiv.org/pdf/2601.21570.pdf)  
**作者**：Zixing Lei, Genjia Liu, Yuanshuo Zhang, Qipeng Liu, Chuan Wen, Shanghang Zhang, Wenzhao Lian, Siheng Chen  

**一句话要点**：提出EmboCoach-Bench基准，评估LLM代理在自主开发具身机器人策略中的能力。

**关键词**：具身AI, LLM代理, 基准测试, 自主工程, 策略优化, 仿真反馈

## 3 点简述
- 核心问题：具身AI领域依赖人工监督，阻碍了通用机器人系统的规模化发展。
- 方法要点：通过32个任务，以可执行代码为接口，评估代理在闭环工作流中迭代优化策略。
- 实验或效果：代理平均成功率超越人工基线26.5%，并展现出自我纠正能力，缩小开源与专有模型差距。

## 摘要（原文）

> The field of Embodied AI is witnessing a rapid evolution toward general-purpose robotic systems, fueled by high-fidelity simulation and large-scale data collection. However, this scaling capability remains severely bottlenecked by a reliance on labor-intensive manual oversight from intricate reward shaping to hyperparameter tuning across heterogeneous backends. Inspired by LLMs' success in software automation and science discovery, we introduce \textsc{EmboCoach-Bench}, a benchmark evaluating the capacity of LLM agents to autonomously engineer embodied policies. Spanning 32 expert-curated RL and IL tasks, our framework posits executable code as the universal interface. We move beyond static generation to assess a dynamic closed-loop workflow, where agents leverage environment feedback to iteratively draft, debug, and optimize solutions, spanning improvements from physics-informed reward design to policy architectures such as diffusion policies. Extensive evaluations yield three critical insights: (1) autonomous agents can qualitatively surpass human-engineered baselines by 26.5\% in average success rate; (2) agentic workflow with environment feedback effectively strengthens policy development and substantially narrows the performance gap between open-source and proprietary models; and (3) agents exhibit self-correction capabilities for pathological engineering cases, successfully resurrecting task performance from near-total failures through iterative simulation-in-the-loop debugging. Ultimately, this work establishes a foundation for self-evolving embodied intelligence, accelerating the paradigm shift from labor-intensive manual tuning to scalable, autonomous engineering in embodied AI field.

