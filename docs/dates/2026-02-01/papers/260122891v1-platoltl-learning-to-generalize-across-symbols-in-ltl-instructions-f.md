---
layout: default
title: PlatoLTL: Learning to Generalize Across Symbols in LTL Instructions for Multi-Task RL
---

# PlatoLTL: Learning to Generalize Across Symbols in LTL Instructions for Multi-Task RL
**arXiv**：[2601.22891v1](https://arxiv.org/abs/2601.22891) · [PDF](https://arxiv.org/pdf/2601.22891.pdf)  
**作者**：Jacques Cloete, Mathias Jackermeier, Ioannis Havoutis, Alessandro Abate  

**一句话要点**：提出PlatoLTL方法，通过参数化谓词实现多任务强化学习中LTL指令的符号泛化

**关键词**：多任务强化学习, 线性时序逻辑, 符号泛化, 零样本学习, 参数化谓词

## 3 点简述
- 核心问题：现有LTL引导的多任务RL方法无法泛化到未见过的命题符号，限制任务扩展性
- 方法要点：将命题视为参数化谓词而非离散符号，设计嵌入和组合架构以学习共享结构
- 实验或效果：在挑战性环境中展示了对新命题和任务的零样本泛化能力

## 摘要（原文）

> A central challenge in multi-task reinforcement learning (RL) is to train generalist policies capable of performing tasks not seen during training. To facilitate such generalization, linear temporal logic (LTL) has recently emerged as a powerful formalism for specifying structured, temporally extended tasks to RL agents. While existing approaches to LTL-guided multi-task RL demonstrate successful generalization across LTL specifications, they are unable to generalize to unseen vocabularies of propositions (or "symbols"), which describe high-level events in LTL. We present PlatoLTL, a novel approach that enables policies to zero-shot generalize not only compositionally across LTL formula structures, but also parametrically across propositions. We achieve this by treating propositions as instances of parameterized predicates rather than discrete symbols, allowing policies to learn shared structure across related propositions. We propose a novel architecture that embeds and composes predicates to represent LTL specifications, and demonstrate successful zero-shot generalization to novel propositions and tasks across challenging environments.

