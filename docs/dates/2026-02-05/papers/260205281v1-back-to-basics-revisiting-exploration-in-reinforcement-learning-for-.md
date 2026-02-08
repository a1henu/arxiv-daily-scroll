---
layout: default
title: Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities
---

# Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities
**arXiv**：[2602.05281v1](https://arxiv.org/abs/2602.05281) · [PDF](https://arxiv.org/pdf/2602.05281.pdf)  
**作者**：Pengyi Li, Elizaveta Goncharova, Andrey Kuznetsov, Ivan Oseledets  

**一句话要点**：提出优势重加权机制以解决强化学习中大语言模型推理的探索不足问题

**关键词**：强化学习, 大语言模型推理, 探索与利用, 策略优化, 生成多样性

## 3 点简述
- 核心问题：标准策略优化方法导致低熵策略，引发模式崩溃和输出多样性受限
- 方法要点：通过提示困惑度和答案置信度动态调整奖励信号，平衡正确响应的置信水平
- 实验或效果：在数学和编码基准上显著提升生成多样性和响应熵，保持准确率竞争力

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an indispensable paradigm for enhancing reasoning in Large Language Models (LLMs). However, standard policy optimization methods, such as Group Relative Policy Optimization (GRPO), often converge to low-entropy policies, leading to severe mode collapse and limited output diversity. We analyze this issue from the perspective of sampling probability dynamics, identifying that the standard objective disproportionately reinforces the highest-likelihood paths, thereby suppressing valid alternative reasoning chains. To address this, we propose a novel Advantage Re-weighting Mechanism (ARM) designed to equilibrate the confidence levels across all correct responses. By incorporating Prompt Perplexity and Answer Confidence into the advantage estimation, our method dynamically reshapes the reward signal to attenuate the gradient updates of over-confident reasoning paths, while redistributing probability mass toward under-explored correct solutions. Empirical results demonstrate that our approach significantly enhances generative diversity and response entropy while maintaining competitive accuracy, effectively achieving a superior trade-off between exploration and exploitation in reasoning tasks. Empirical results on Qwen2.5 and DeepSeek models across mathematical and coding benchmarks show that ProGRPO significantly mitigates entropy collapse. Specifically, on Qwen2.5-7B, our method outperforms GRPO by 5.7% in Pass@1 and, notably, by 13.9% in Pass@32, highlighting its superior capability in generating diverse correct reasoning paths.

