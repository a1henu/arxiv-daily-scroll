---
layout: default
title: Semantically Labelled Automata for Multi-Task Reinforcement Learning with LTL Instructions
---

# Semantically Labelled Automata for Multi-Task Reinforcement Learning with LTL Instructions
**arXiv**：[2602.06746v1](https://arxiv.org/abs/2602.06746) · [PDF](https://arxiv.org/pdf/2602.06746.pdf)  
**作者**：Alessandro Abate, Giuseppe De Giacomo, Mathias Jackermeier, Jan Kretínský, Maximilian Prokop, Christoph Weinhuber  

**一句话要点**：提出基于语义标记自动机的任务嵌入技术，以解决多任务强化学习中LTL指令的通用策略学习问题。

**关键词**：多任务强化学习, 线性时序逻辑, 语义自动机, 任务嵌入, 通用策略学习

## 3 点简述
- 研究多任务强化学习，任务以线性时序逻辑公式指定，支持泛化至未知任务。
- 利用语义LTL到自动机翻译，生成语义标记自动机，实现高效计算和表达性任务嵌入。
- 实验表明，该方法在复杂规范下达到先进性能，优于现有方法。

## 摘要（原文）

> We study multi-task reinforcement learning (RL), a setting in which an agent learns a single, universal policy capable of generalising to arbitrary, possibly unseen tasks. We consider tasks specified as linear temporal logic (LTL) formulae, which are commonly used in formal methods to specify properties of systems, and have recently been successfully adopted in RL. In this setting, we present a novel task embedding technique leveraging a new generation of semantic LTL-to-automata translations, originally developed for temporal synthesis. The resulting semantically labelled automata contain rich, structured information in each state that allow us to (i) compute the automaton efficiently on-the-fly, (ii) extract expressive task embeddings used to condition the policy, and (iii) naturally support full LTL. Experimental results in a variety of domains demonstrate that our approach achieves state-of-the-art performance and is able to scale to complex specifications where existing methods fail.

