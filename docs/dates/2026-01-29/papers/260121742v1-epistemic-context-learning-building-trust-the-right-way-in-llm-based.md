---
layout: default
title: Epistemic Context Learning: Building Trust the Right Way in LLM-Based Multi-Agent Systems
---

# Epistemic Context Learning: Building Trust the Right Way in LLM-Based Multi-Agent Systems
**arXiv**：[2601.21742v1](https://arxiv.org/abs/2601.21742) · [PDF](https://arxiv.org/pdf/2601.21742.pdf)  
**作者**：Ruiwen Zhou, Maojia Song, Xiaobao Wu, Sitao Cheng, Xunjian Yin, Yuxi Xie, Zhuoqun Hao, Wenyue Hua, Liangming Pan, Soujanya Poria, Min-Yen Kan  

**一句话要点**：提出Epistemic Context Learning以解决多智能体系统中智能体盲从误导同伴的问题

**关键词**：多智能体系统, 可靠性评估, 历史感知学习, 强化学习优化, 信任建模

## 3 点简述
- 核心问题：多智能体系统中个体智能体因盲从和评估同伴可靠性能力不足而缺乏鲁棒性
- 方法要点：通过历史交互构建同伴档案，基于历史评估可靠性并学习可信同伴，使用强化学习优化框架
- 实验或效果：ECL使小模型超越大基线模型，提升前沿模型至近完美性能，并展示良好泛化能力

## 摘要（原文）

> Individual agents in multi-agent (MA) systems often lack robustness, tending to blindly conform to misleading peers. We show this weakness stems from both sycophancy and inadequate ability to evaluate peer reliability. To address this, we first formalize the learning problem of history-aware reference, introducing the historical interactions of peers as additional input, so that agents can estimate peer reliability and learn from trustworthy peers when uncertain. This shifts the task from evaluating peer reasoning quality to estimating peer reliability based on interaction history. We then develop Epistemic Context Learning (ECL): a reasoning framework that conditions predictions on explicitly-built peer profiles from history. We further optimize ECL by reinforcement learning using auxiliary rewards. Our experiments reveal that our ECL enables small models like Qwen 3-4B to outperform a history-agnostic baseline 8x its size (Qwen 3-30B) by accurately identifying reliable peers. ECL also boosts frontier models to near-perfect (100%) performance. We show that ECL generalizes well to various MA configurations and we find that trust is modeled well by LLMs, revealing a strong correlation in trust modeling accuracy and final answer quality.

