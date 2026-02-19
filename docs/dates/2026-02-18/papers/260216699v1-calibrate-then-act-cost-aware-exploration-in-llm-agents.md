---
layout: default
title: Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents
---

# Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents
**arXiv**：[2602.16699v1](https://arxiv.org/abs/2602.16699) · [PDF](https://arxiv.org/pdf/2602.16699.pdf)  
**作者**：Wenxuan Ding, Nicholas Tomlin, Greg Durrett  

**一句话要点**：提出Calibrate-Then-Act框架，以优化LLM代理在不确定环境中的成本感知探索策略。

**关键词**：LLM代理, 成本感知探索, 序列决策, 不确定性推理, 信息检索, 编程任务

## 3 点简述
- 核心问题：LLM代理在复杂任务中需权衡探索成本与不确定性，以决定何时停止探索并提交答案。
- 方法要点：通过提供额外上下文，使LLM显式推理成本-不确定性权衡，实现更优的序列决策。
- 实验或效果：在信息检索和简化编码任务中，CTA框架帮助代理发现更优策略，效果在强化学习训练后仍保持。

## 摘要（原文）

> LLMs are increasingly being used for complex problems which are not necessarily resolved in a single response, but require interacting with an environment to acquire information. In these scenarios, LLMs must reason about inherent cost-uncertainty tradeoffs in when to stop exploring and commit to an answer. For instance, on a programming task, an LLM should test a generated code snippet if it is uncertain about the correctness of that code; the cost of writing a test is nonzero, but typically lower than the cost of making a mistake. In this work, we show that we can induce LLMs to explicitly reason about balancing these cost-uncertainty tradeoffs, then perform more optimal environment exploration. We formalize multiple tasks, including information retrieval and coding, as sequential decision-making problems under uncertainty. Each problem has latent environment state that can be reasoned about via a prior which is passed to the LLM agent. We introduce a framework called Calibrate-Then-Act (CTA), where we feed the LLM this additional context to enable it to act more optimally. This improvement is preserved even under RL training of both the baseline and CTA. Our results on information-seeking QA and on a simplified coding task show that making cost-benefit tradeoffs explicit with CTA can help agents discover more optimal decision-making strategies.

