---
layout: default
title: MASCOT: Towards Multi-Agent Socio-Collaborative Companion Systems
---

# MASCOT: Towards Multi-Agent Socio-Collaborative Companion Systems
**arXiv**：[2601.14230v1](https://arxiv.org/abs/2601.14230) · [PDF](https://arxiv.org/pdf/2601.14230.pdf)  
**作者**：Yiyang Wang, Yiqiao Jin, Alex Cabral, Josiah Hester  

**一句话要点**：提出MASCOT框架以解决多智能体系统中角色崩溃和社交谄媚问题

**关键词**：多智能体系统, 角色一致性, 协作对话优化, 双层优化, 社交智能

## 3 点简述
- 核心问题：多智能体系统易出现角色崩溃和社交谄媚，导致行为同质化和对话冗余。
- 方法要点：采用双层优化策略，包括基于RLAIF的角色感知行为对齐和群体奖励引导的协作对话优化。
- 实验或效果：在心理支持和职场领域评估中，MASCOT在角色一致性和社交贡献方面显著优于基线模型。

## 摘要（原文）

> Multi-agent systems (MAS) have recently emerged as promising socio-collaborative companions for emotional and cognitive support. However, these systems frequently suffer from persona collapse--where agents revert to generic, homogenized assistant behaviors--and social sycophancy, which produces redundant, non-constructive dialogue. We propose MASCOT, a generalizable framework for multi-perspective socio-collaborative companions. MASCOT introduces a novel bi-level optimization strategy to harmonize individual and collective behaviors: 1) Persona-Aware Behavioral Alignment, an RLAIF-driven pipeline that finetunes individual agents for strict persona fidelity to prevent identity loss; and 2) Collaborative Dialogue Optimization, a meta-policy guided by group-level rewards to ensure diverse and productive discourse. Extensive evaluations across psychological support and workplace domains demonstrate that MASCOT significantly outperforms state-of-the-art baselines, achieving improvements of up to +14.1 in Persona Consistency and +10.6 in Social Contribution. Our framework provides a practical roadmap for engineering the next generation of socially intelligent multi-agent systems.

