---
layout: default
title: Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions
---

# Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions
**arXiv**：[2601.04170v1](https://arxiv.org/abs/2601.04170) · [PDF](https://arxiv.org/pdf/2601.04170.pdf)  
**作者**：Abhishek Rath  

**一句话要点**：提出Agent Drift概念与Agent Stability Index以量化多智能体LLM系统长期交互中的行为退化

**关键词**：多智能体系统, 大语言模型, 行为退化, Agent Drift, Agent Stability Index, 漂移缓解

## 3 点简述
- 核心问题：多智能体LLM系统在长期交互中行为退化，包括语义、协调和行为漂移
- 方法要点：引入Agent Stability Index，通过十二维度复合指标量化漂移，并提出三种缓解策略
- 实验或效果：基于模拟分析，漂移导致任务准确率下降，缓解策略可减少错误并保持系统吞吐

## 摘要（原文）

> Multi-agent Large Language Model (LLM) systems have emerged as powerful architectures for complex task decomposition and collaborative problem-solving. However, their long-term behavioral stability remains largely unexamined. This study introduces the concept of agent drift, defined as the progressive degradation of agent behavior, decision quality, and inter-agent coherence over extended interaction sequences. We present a comprehensive theoretical framework for understanding drift phenomena, proposing three distinct manifestations: semantic drift (progressive deviation from original intent), coordination drift (breakdown in multi-agent consensus mechanisms), and behavioral drift (emergence of unintended strategies).
>   We introduce the Agent Stability Index (ASI), a novel composite metric framework for quantifying drift across twelve dimensions, including response consistency, tool usage patterns, reasoning pathway stability, and inter-agent agreement rates. Through simulation-based analysis and theoretical modeling, we demonstrate how unchecked agent drift can lead to substantial reductions in task completion accuracy and increased human intervention requirements.
>   We propose three mitigation strategies: episodic memory consolidation, drift-aware routing protocols, and adaptive behavioral anchoring. Theoretical analysis suggests these approaches can significantly reduce drift-related errors while maintaining system throughput. This work establishes a foundational methodology for monitoring, measuring, and mitigating agent drift in production agentic AI systems, with direct implications for enterprise deployment reliability and AI safety research.

