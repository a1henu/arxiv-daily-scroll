---
layout: default
title: Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop
---

# Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop
**arXiv**：[2601.05184v1](https://arxiv.org/abs/2601.05184) · [PDF](https://arxiv.org/pdf/2601.05184.pdf)  
**作者**：Yaxuan Wang, Zhongteng Cai, Yujia Bao, Xueru Zhang, Yang Liu  

**一句话要点**：提出自消耗表演循环概念，研究合成数据在动态迭代训练中塑造偏见的作用，并设计奖励拒绝采样策略缓解偏见。

**关键词**：大语言模型偏见, 自消耗循环, 合成数据训练, 表演反馈, 偏见缓解, 动态系统

## 3 点简述
- 核心问题：大语言模型在自消耗循环中训练于自身输出，可能导致性能下降和偏见演化。
- 方法要点：引入自消耗表演循环概念，在受控表演反馈下分析偏见演化，包括典型重训练和增量微调设置。
- 实验或效果：在三个真实任务上实验，发现表演循环增加偏好偏见、减少差异偏见，奖励拒绝采样策略有效缓解偏见。

## 摘要（原文）

> The rapid advancement of large language models (LLMs) has led to growing interest in using synthetic data to train future models. However, this creates a self-consuming retraining loop, where models are trained on their own outputs and may cause performance drops and induce emerging biases. In real-world applications, previously deployed LLMs may influence the data they generate, leading to a dynamic system driven by user feedback. For example, if a model continues to underserve users from a group, less query data will be collected from this particular demographic of users. In this study, we introduce the concept of \textbf{S}elf-\textbf{C}onsuming \textbf{P}erformative \textbf{L}oop (\textbf{SCPL}) and investigate the role of synthetic data in shaping bias during these dynamic iterative training processes under controlled performative feedback. This controlled setting is motivated by the inaccessibility of real-world user preference data from dynamic production systems, and enables us to isolate and analyze feedback-driven bias evolution in a principled manner. We focus on two types of loops, including the typical retraining setting and the incremental fine-tuning setting, which is largely underexplored. Through experiments on three real-world tasks, we find that the performative loop increases preference bias and decreases disparate bias. We design a reward-based rejection sampling strategy to mitigate the bias, moving towards more trustworthy self-improving systems.

