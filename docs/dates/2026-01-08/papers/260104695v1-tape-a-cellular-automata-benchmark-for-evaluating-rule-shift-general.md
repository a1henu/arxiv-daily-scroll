---
layout: default
title: Tape: A Cellular Automata Benchmark for Evaluating Rule-Shift Generalization in Reinforcement Learning
---

# Tape: A Cellular Automata Benchmark for Evaluating Rule-Shift Generalization in Reinforcement Learning
**arXiv**：[2601.04695v1](https://arxiv.org/abs/2601.04695) · [PDF](https://arxiv.org/pdf/2601.04695.pdf)  
**作者**：Enze Pan  

**一句话要点**：提出Tape基准以评估强化学习在规则转移下的泛化能力

**关键词**：强化学习基准, 规则转移泛化, 元胞自动机, 分布外评估, 统计报告, 不确定性分析

## 3 点简述
- 核心问题：强化学习模型在潜在规则转移时易出现分布外失败
- 方法要点：基于一维元胞自动机设计可控基准，固定观测和动作空间，改变转移规则
- 实验或效果：比较多种方法，发现强分布内性能方法在分布外可能崩溃，需统计评估

## 摘要（原文）

> We present Tape, a controlled reinforcement-learning benchmark designed to isolate out-of-distribution (OOD) failure under latent rule shifts.Tape is derived from one-dimensional cellular automata, enabling precise train/test splits where observation and action spaces are held fixed while transition rules change. Using a reproducible evaluation pipeline, we compare model-free baselines, model-based planning with learned world models, and task-inference (meta-RL) methods. A consistent pattern emerges: methods that are strong in-distribution (ID) can collapse under heldout-rule OOD, and high-variance OOD evaluation can make rankings unstable unless experiments are sufficiently replicated.We provide (i) standardized OOD protocols, (ii) statistical reporting requirements (seeds, confidence intervals, and hypothesis tests), and (iii) information-theoretic identities connecting entropy reduction to conditional mutual information and expected posterior KL divergence, clarifying what "uncertainty reduction" objectives can and cannot guarantee under rule shifts.

