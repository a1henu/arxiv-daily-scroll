---
layout: default
title: PersonaLedger: Generating Realistic Financial Transactions with Persona Conditioned LLMs and Rule Grounded Feedback
---

# PersonaLedger: Generating Realistic Financial Transactions with Persona Conditioned LLMs and Rule Grounded Feedback
**arXiv**：[2601.03149v1](https://arxiv.org/abs/2601.03149) · [PDF](https://arxiv.org/pdf/2601.03149.pdf)  
**作者**：Dehao Yuan, Tyler Farnan, Stefan Tesliuc, Doron L Bergman, Yulun Wu, Xiaoyu Liu, Minghui Liu, James Montgomery, Nam H Nguyen, C. Bayan Bruss, Furong Huang  

**一句话要点**：提出PersonaLedger，结合LLM与规则引擎生成多样且逻辑正确的金融交易数据以解决隐私限制问题。

**关键词**：金融交易合成数据, 大型语言模型, 规则引擎, 隐私保护, 异常检测

## 3 点简述
- 核心问题：隐私法规限制真实交易数据访问，现有合成数据生成器难以兼顾行为多样性和逻辑正确性。
- 方法要点：使用基于用户角色的LLM生成交易流，配合可配置规则引擎闭环交互确保金融约束。
- 实验或效果：创建包含3000万交易的公开数据集和基准测试，支持预测与异常检测模型评估。

## 摘要（原文）

> Strict privacy regulations limit access to real transaction data, slowing open research in financial AI. Synthetic data can bridge this gap, but existing generators do not jointly achieve behavioral diversity and logical groundedness. Rule-driven simulators rely on hand-crafted workflows and shallow stochasticity, which miss the richness of human behavior. Learning-based generators such as GANs capture correlations yet often violate hard financial constraints and still require training on private data. We introduce PersonaLedger, a generation engine that uses a large language model conditioned on rich user personas to produce diverse transaction streams, coupled with an expert configurable programmatic engine that maintains correctness. The LLM and engine interact in a closed loop: after each event, the engine updates the user state, enforces financial rules, and returns a context aware "nextprompt" that guides the LLM toward feasible next actions. With this engine, we create a public dataset of 30 million transactions from 23,000 users and a benchmark suite with two tasks, illiquidity classification and identity theft segmentation. PersonaLedger offers a realistic, privacy preserving resource that supports rigorous evaluation of forecasting and anomaly detection models. PersonaLedger offers the community a rich, realistic, and privacy preserving resource -- complete with code, rules, and generation logs -- to accelerate innovation in financial AI and enable rigorous, reproducible evaluation.

