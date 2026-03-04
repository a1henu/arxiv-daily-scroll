---
layout: default
title: Contextualized Privacy Defense for LLM Agents
---

# Contextualized Privacy Defense for LLM Agents
**arXiv**：[2603.02983v1](https://arxiv.org/abs/2603.02983) · [PDF](https://arxiv.org/pdf/2603.02983.pdf)  
**作者**：Yule Wen, Yanzhe Zhang, Jianxun Lian, Xiaoyuan Yi, Xing Xie, Diyi Yang  

**一句话要点**：提出情境化防御指导范式，通过强化学习优化指导模型，提升LLM代理的隐私保护与实用性平衡

**关键词**：LLM代理隐私, 情境化防御, 强化学习优化, 隐私-实用性权衡, 主动指导范式

## 3 点简述
- 现有LLM代理隐私防御多为静态被动方式，难以支持多步执行中的情境化主动决策
- 提出CDI范式，使用指导模型生成情境感知的隐私指导，主动塑造代理行为而非简单约束
- 通过强化学习框架优化指导模型，在模拟环境中实现94.2%隐私保护率与80.6%实用性

## 摘要（原文）

> LLM agents increasingly act on users' personal information, yet existing privacy defenses remain limited in both design and adaptability. Most prior approaches rely on static or passive defenses, such as prompting and guarding. These paradigms are insufficient for supporting contextual, proactive privacy decisions in multi-step agent execution. We propose Contextualized Defense Instructing (CDI), a new privacy defense paradigm in which an instructor model generates step-specific, context-aware privacy guidance during execution, proactively shaping actions rather than merely constraining or vetoing them. Crucially, CDI is paired with an experience-driven optimization framework that trains the instructor via reinforcement learning (RL), where we convert failure trajectories with privacy violations into learning environments. We formalize baseline defenses and CDI as distinct intervention points in a canonical agent loop, and compare their privacy-helpfulness trade-offs within a unified simulation framework. Results show that our CDI consistently achieves a better balance between privacy preservation (94.2%) and helpfulness (80.6%) than baselines, with superior robustness to adversarial conditions and generalization.

