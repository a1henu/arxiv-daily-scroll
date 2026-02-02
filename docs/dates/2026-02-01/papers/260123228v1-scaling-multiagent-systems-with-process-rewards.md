---
layout: default
title: Scaling Multiagent Systems with Process Rewards
---

# Scaling Multiagent Systems with Process Rewards
**arXiv**：[2601.23228v1](https://arxiv.org/abs/2601.23228) · [PDF](https://arxiv.org/pdf/2601.23228.pdf)  
**作者**：Ed Li, Junyu Ren, Cat Yan  

**一句话要点**：提出基于AI反馈的每动作过程奖励微调方法，以解决多智能体系统中的信用分配和样本效率问题。

**关键词**：多智能体系统, 过程奖励, 信用分配, 样本效率, AI反馈, 微调方法

## 3 点简述
- 核心问题：多智能体系统同时微调面临信用分配和样本效率挑战。
- 方法要点：使用每动作过程奖励进行细粒度监督，无需真实标签，最大化训练信号。
- 实验或效果：在数学竞赛和数据分析任务上验证，性能提升显著，如AIME准确率提高5.0-17.5个百分点。

## 摘要（原文）

> While multiagent systems have shown promise for tackling complex tasks via specialization, finetuning multiple agents simultaneously faces two key challenges: (1) credit assignment across agents, and (2) sample efficiency of expensive multiagent rollouts. In this work, we propose finetuning multiagent systems with per-action process rewards from AI feedback (MAPPA) to address both. Through assigning credit to individual agent actions rather than only at task completion, MAPPA enables fine-grained supervision without ground truth labels while extracting maximal training signal from each rollout. We demonstrate our approach on competition math problems and tool-augmented data analysis tasks. On unseen math problems, MAPPA achieves +5.0--17.5pp on AIME and +7.8--17.2pp on AMC. For data analysis tasks, our method improves success rate by +12.5pp while quality metrics improve by up to 30%, validating that per-action supervision can lead to improvements across different multiagent system on various domains. By addressing these challenges, our work takes a first step toward scaling multiagent systems for complex, long-horizon tasks with minimal human supervision.

