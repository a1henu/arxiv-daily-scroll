---
layout: default
title: TABX: A High-Throughput Sandbox Battle Simulator for Multi-Agent Reinforcement Learning
---

# TABX: A High-Throughput Sandbox Battle Simulator for Multi-Agent Reinforcement Learning
**arXiv**：[2602.01665v1](https://arxiv.org/abs/2602.01665) · [PDF](https://arxiv.org/pdf/2602.01665.pdf)  
**作者**：Hayeong Lee, JunHyeok Oh, Byung-Jun Lee  

**一句话要点**：提出TABX沙盒模拟器以支持可重构多智能体强化学习任务的高通量评估

**关键词**：多智能体强化学习, 沙盒模拟器, JAX加速, 环境模块化, 高通量评估

## 3 点简述
- 现有MARL基准缺乏模块化，难以设计自定义评估场景
- TABX基于JAX实现硬件加速，提供环境参数细粒度控制和并行化
- 框架快速可扩展，促进复杂结构化领域中MARL代理行为研究

## 摘要（原文）

> The design of environments plays a critical role in shaping the development and evaluation of cooperative multi-agent reinforcement learning (MARL) algorithms. While existing benchmarks highlight critical challenges, they often lack the modularity required to design custom evaluation scenarios. We introduce the Totally Accelerated Battle Simulator in JAX (TABX), a high-throughput sandbox designed for reconfigurable multi-agent tasks. TABX provides granular control over environmental parameters, permitting a systematic investigation into emergent agent behaviors and algorithmic trade-offs across a diverse spectrum of task complexities. Leveraging JAX for hardware-accelerated execution on GPUs, TABX enables massive parallelization and significantly reduces computational overhead. By providing a fast, extensible, and easily customized framework, TABX facilitates the study of MARL agents in complex structured domains and serves as a scalable foundation for future research. Our code is available at: https://anonymous.4open.science/r/TABX-00CA.

