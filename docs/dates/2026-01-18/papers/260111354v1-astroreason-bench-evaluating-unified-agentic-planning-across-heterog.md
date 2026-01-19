---
layout: default
title: AstroReason-Bench: Evaluating Unified Agentic Planning across Heterogeneous Space Planning Problems
---

# AstroReason-Bench: Evaluating Unified Agentic Planning across Heterogeneous Space Planning Problems
**arXiv**：[2601.11354v1](https://arxiv.org/abs/2601.11354) · [PDF](https://arxiv.org/pdf/2601.11354.pdf)  
**作者**：Weiyi Wang, Xinchi Chen, Jingjing Gong, Xuanjing Huang, Xipeng Qiu  

**一句话要点**：提出AstroReason-Bench以评估异构空间规划问题中的统一智能体规划能力

**关键词**：智能体规划, 空间规划问题, 物理约束, 长时程决策, 基准评估, 异构目标

## 3 点简述
- 现有智能体基准多关注符号或弱接地环境，缺乏物理约束真实领域评估
- AstroReason-Bench集成多种调度机制，提供统一智能体交互协议
- 实验显示当前智能体在现实约束下显著落后于专用求解器

## 摘要（原文）

> Recent advances in agentic Large Language Models (LLMs) have positioned them as generalist planners capable of reasoning and acting across diverse tasks. However, existing agent benchmarks largely focus on symbolic or weakly grounded environments, leaving their performance in physics-constrained real-world domains underexplored. We introduce AstroReason-Bench, a comprehensive benchmark for evaluating agentic planning in Space Planning Problems (SPP), a family of high-stakes problems with heterogeneous objectives, strict physical constraints, and long-horizon decision-making. AstroReason-Bench integrates multiple scheduling regimes, including ground station communication and agile Earth observation, and provides a unified agent-oriented interaction protocol. Evaluating on a range of state-of-the-art open- and closed-source agentic LLM systems, we find that current agents substantially underperform specialized solvers, highlighting key limitations of generalist planning under realistic constraints. AstroReason-Bench offers a challenging and diagnostic testbed for future agentic research.

