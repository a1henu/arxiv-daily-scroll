---
layout: default
title: EvolveGen: Algorithmic Level Hardware Model Checking Benchmark Generation through Reinforcement Learning
---

# EvolveGen: Algorithmic Level Hardware Model Checking Benchmark Generation through Reinforcement Learning
**arXiv**：[2602.22609v1](https://arxiv.org/abs/2602.22609) · [PDF](https://arxiv.org/pdf/2602.22609.pdf)  
**作者**：Guangyu Hu, Xiaofeng Zhou, Wei Zhang, Hongce Zhang  

**一句话要点**：提出EvolveGen框架，通过强化学习生成硬件模型检查基准以解决基准集不足问题

**关键词**：硬件模型检查, 基准生成, 强化学习, 高层次合成, 算法级抽象, 性能评估

## 3 点简述
- 硬件模型检查面临基准集数量有限、偏向极端难度且缺乏原始RTL设计的问题
- 结合强化学习与高层次合成，在算法层面构建计算图以生成功能等效但结构不同的硬件设计
- 实验表明能高效生成多样化基准，揭示先进模型检查器的性能瓶颈

## 摘要（原文）

> Progress in hardware model checking depends critically on high-quality benchmarks. However, the community faces a significant benchmark gap: existing suites are limited in number, often distributed only in representations such as BTOR2 without access to the originating register-transfer-level (RTL) designs, and biased toward extreme difficulty where instances are either trivial or intractable. These limitations hinder rigorous evaluation of new verification techniques and encourage overfitting of solver heuristics to a narrow set of problems. To address this, we introduce EvolveGen, a framework for generating hardware model checking benchmarks by combining reinforcement learning (RL) with high-level synthesis (HLS). Our approach operates at an algorithmic level of abstraction in which an RL agent learns to construct computation graphs. By compiling these graphs under different synthesis directives, we produce pairs of functionally equivalent but structurally distinct hardware designs, inducing challenging model checking instances. Solver runtime is used as the reward signal, enabling the agent to autonomously discover and generate small-but-hard instances that expose solver-specific weaknesses. Experiments show that EvolveGen efficiently creates a diverse benchmark set in standard formats (e.g., AIGER and BTOR2) and effectively reveals performance bottlenecks in state-of-the-art model checkers.

