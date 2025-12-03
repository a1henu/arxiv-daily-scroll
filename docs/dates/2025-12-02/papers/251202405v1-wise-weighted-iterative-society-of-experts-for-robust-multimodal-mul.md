---
layout: default
title: WISE: Weighted Iterative Society-of-Experts for Robust Multimodal Multi-Agent Debate
---

# WISE: Weighted Iterative Society-of-Experts for Robust Multimodal Multi-Agent Debate
**arXiv**：[2512.02405v1](https://arxiv.org/abs/2512.02405) · [PDF](https://arxiv.org/pdf/2512.02405.pdf)  
**作者**：Anoop Cherian, River Doyle, Eyal Ben-Dov, Suhas Lohit, Kuan-Chuan Peng  

**一句话要点**：提出WISE框架以增强多模态多智能体辩论的鲁棒性

**关键词**：多智能体辩论, 多模态推理, 加权聚合, 异构专家, 鲁棒性增强

## 3 点简述
- 研究多智能体辩论在视觉-语言推理任务中的应用，扩展至异构专家
- 设计加权迭代专家社会框架，包含求解器和反思器角色，集成反馈权重
- 在多个数据集上评估，准确率提升2-7%，优于现有方法

## 摘要（原文）

> Recent large language models (LLMs) are trained on diverse corpora and tasks, leading them to develop complementary strengths. Multi-agent debate (MAD) has emerged as a popular way to leverage these strengths for robust reasoning, though it has mostly been applied to language-only tasks, leaving its efficacy on multimodal problems underexplored. In this paper, we study MAD for solving vision-and-language reasoning problems. Our setup enables generalizing the debate protocol with heterogeneous experts that possess single- and multi-modal capabilities. To this end, we present Weighted Iterative Society-of-Experts (WISE), a generalized and modular MAD framework that partitions the agents into Solvers, that generate solutions, and Reflectors, that verify correctness, assign weights, and provide natural language feedback. To aggregate the agents' solutions across debate rounds, while accounting for variance in their responses and the feedback weights, we present a modified Dawid-Skene algorithm for post-processing that integrates our two-stage debate model. We evaluate WISE on SMART-840, VisualPuzzles, EvoChart-QA, and a new SMART-840++ dataset with programmatically generated problem instances of controlled difficulty. Our results show that WISE consistently improves accuracy by 2-7% over the state-of-the-art MAD setups and aggregation methods across diverse multimodal tasks and LLM configurations.

