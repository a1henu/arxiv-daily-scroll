---
layout: default
title: Learning Adaptive LLM Decoding
---

# Learning Adaptive LLM Decoding
**arXiv**：[2603.09065v1](https://arxiv.org/abs/2603.09065) · [PDF](https://arxiv.org/pdf/2603.09065.pdf)  
**作者**：Chloe H. Su, Zhe Ye, Samuel Tenka, Aidan Yang, Soonho Kong, Udaya Ghai  

**一句话要点**：提出自适应解码策略以优化大语言模型在资源受限下的推理性能

**关键词**：大语言模型解码, 自适应采样, 强化学习, 资源优化, 序列级策略, 令牌级策略

## 3 点简述
- 核心问题：传统解码使用固定采样参数，无法适应任务难度和计算资源变化。
- 方法要点：通过强化学习训练轻量解码适配器，在序列和令牌级别动态选择解码策略。
- 实验效果：在MATH和CodeContests基准上，提升准确率-预算权衡，最高增益达10.2%。

## 摘要（原文）

> Decoding from large language models (LLMs) typically relies on fixed sampling hyperparameters (e.g., temperature, top-p), despite substantial variation in task difficulty and uncertainty across prompts and individual decoding steps. We propose to learn adaptive decoding policies that dynamically select sampling strategies at inference time, conditioned on available compute resources. Rather than fine-tuning the language model itself, we introduce lightweight decoding adapters trained with reinforcement learning and verifiable terminal rewards (e.g. correctness on math and coding tasks). At the sequence level, we frame decoding as a contextual bandit problem: a policy selects a decoding strategy (e.g. greedy, top-k, min-p) for each prompt, conditioned on the prompt embedding and a parallel sampling budget. At the token level, we model decoding as a partially observable Markov decision process (POMDP), where a policy selects sampling actions at each token step based on internal model features and the remaining token budget. Experiments on the MATH and CodeContests benchmarks show that the learned adapters improve the accuracy-budget tradeoff: on MATH, the token-level adapter improves Pass@1 accuracy by up to 10.2% over the best static baseline under a fixed token budget, while the sequence-level adapter yields 2-3% gains under fixed parallel sampling. Ablation analyses support the contribution of both sequence- and token-level adaptation.

