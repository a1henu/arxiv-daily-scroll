---
layout: default
title: ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents
---

# ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents
**arXiv**：[2602.01869v1](https://arxiv.org/abs/2602.01869) · [PDF](https://arxiv.org/pdf/2602.01869.pdf)  
**作者**：Qirui Mi, Zhijian Ma, Mengyue Yang, Haoxuan Li, Yisen Wang, Haifeng Zhang, Jun Wang  

**一句话要点**：提出ProcMEM框架，通过非参数PPO从经验中学习可重用程序记忆，提升LLM智能体长期自主性

**关键词**：程序记忆学习, 非参数强化学习, 技能形式化, 经验复用, LLM智能体, 长期自主性

## 3 点简述
- LLM智能体在序列决策中依赖即时推理，重复场景下经验复用不足导致计算冗余和执行不稳定
- 通过Skill-MDP形式化，将经验叙事转化为可执行技能，采用非参数PPO进行高质量候选生成和验证
- 实验显示在跨任务、跨智能体场景中实现高复用率和性能提升，并保持极简记忆压缩

## 摘要（原文）

> LLM-driven agents demonstrate strong performance in sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and execution instability. To bridge this gap, we propose ProcMEM, a framework that enables agents to autonomously learn procedural memory from interaction experiences without parameter updates. By formalizing a Skill-MDP, ProcMEM transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, ProcMEM sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that ProcMEM achieves superior reuse rates and significant performance gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how ProcMEM transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

