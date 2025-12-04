---
layout: default
title: Learning Steerable Clarification Policies with Collaborative Self-play
---

# Learning Steerable Clarification Policies with Collaborative Self-play
**arXiv**：[2512.04068v1](https://arxiv.org/abs/2512.04068) · [PDF](https://arxiv.org/pdf/2512.04068.pdf)  
**作者**：Jonathan Berant, Maximillian Chen, Adam Fisch, Reza Aghajani, Fantine Huot, Mirella Lapata, Jacob Eisenstein  

**一句话要点**：提出基于自博弈的可调控澄清策略，以处理AI助手在不确定查询下的响应决策问题。

**关键词**：不确定性管理, 自博弈训练, 可调控策略, 强化自训练, 澄清策略

## 3 点简述
- 核心问题：AI助手需在不确定查询时决定何时猜测意图、枚举意图或提问澄清，策略受用户偏好和模态等因素影响。
- 方法要点：使用自博弈训练可调控策略，输入澄清问题和生成词的成本，通过强化自训练最大化成本惩罚后的准确率奖励。
- 实验或效果：策略能根据成本可预测地调整行为，提高奖励和准确率，并泛化到训练时未见的成本值。

## 摘要（原文）

> To handle underspecified or ambiguous queries, AI assistants need a policy for managing their uncertainty to determine (a) when to guess the user intent and answer directly, (b) when to enumerate and answer multiple possible intents, and (c) when to ask a clarifying question. However, such policies are contextually dependent on factors such as user preferences or modality. For example, enumerating multiple possible user intentions is cumbersome on small screens or in a voice setting. In this work, we propose to train steerable policies for managing this uncertainty using self-play. Given two agents, one simulating a user and the other an AI assistant, we generate conversations where the user issues a potentially ambiguous query, and the assistant needs to determine how to respond. Importantly, the model takes as input the numerical cost of each clarification question, and each generated word, and is asked to take the action that will maximize its final reward, which is the cost-penalized accuracy. We use Reinforced Self-Training (ReST) to train our model to achieve high reward and show this leads to a steerable policy that changes its behavior predictably conditioned on the provided costs, leading to higher reward and accuracy. Moreover, our procedure also generalizes to numerical cost values that were unobserved at training time.

