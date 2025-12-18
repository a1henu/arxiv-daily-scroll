---
layout: default
title: Stepwise Think-Critique: A Unified Framework for Robust and Interpretable LLM Reasoning
---

# Stepwise Think-Critique: A Unified Framework for Robust and Interpretable LLM Reasoning
**arXiv**：[2512.15662v1](https://arxiv.org/abs/2512.15662) · [PDF](https://arxiv.org/pdf/2512.15662.pdf)  
**作者**：Jiaqi Xu, Cuiling Lan, Xuejin Chen, Yan LU  

**一句话要点**：提出Stepwise Think-Critique框架，在单模型中交织推理与自批判以增强LLM鲁棒性和可解释性

**关键词**：大语言模型推理, 自批判机制, 混合强化学习, 可解释人工智能, 数学推理

## 3 点简述
- 现有LLM常将推理与验证分离，缺乏即时反馈或增加系统复杂性
- STC框架在每一步推理中交织自批判，通过混合强化学习联合优化推理质量和自评估
- 在数学推理基准测试中，STC展现出强批判思维能力和更可解释的推理轨迹

## 摘要（原文）

> Human beings solve complex problems through critical thinking, where reasoning and evaluation are intertwined to converge toward correct solutions. However, most existing large language models (LLMs) decouple reasoning from verification: they either generate reasoning without explicit self-checking or rely on external verifiers to detect errors post hoc. The former lacks immediate feedback, while the latter increases system complexity and hinders synchronized learning. Motivated by human critical thinking, we propose Stepwise Think-Critique (STC), a unified framework that interleaves reasoning and self-critique at each step within a single model. STC is trained with a hybrid reinforcement learning objective combining reasoning rewards and critique-consistency rewards to jointly optimize reasoning quality and self-evaluation. Experiments on mathematical reasoning benchmarks show that STC demonstrates strong critic-thinking capabilities and produces more interpretable reasoning traces, representing a step toward LLMs with built-in critical thinking.

