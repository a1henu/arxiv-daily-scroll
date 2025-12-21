---
layout: default
title: Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics
---

# Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics
**arXiv**：[2512.16602v1](https://arxiv.org/abs/2512.16602) · [PDF](https://arxiv.org/pdf/2512.16602.pdf)  
**作者**：Iker García-Ferrero, David Montero, Roman Orus  

**一句话要点**：提出Refusal Steering方法，在推理时精细控制大语言模型对政治敏感话题的拒绝行为

**关键词**：激活引导, 拒绝行为控制, 推理时干预, 政治敏感话题, 岭正则化

## 3 点简述
- 核心问题：大语言模型对政治敏感话题的拒绝行为难以精细控制，现有方法依赖脆弱模式检测。
- 方法要点：使用LLM作为评判器分配拒绝置信度，提出岭正则化变体计算引导向量以隔离拒绝-顺从方向。
- 实验或效果：在Qwen3-Next-80B-A3B-Thinking上移除政治拒绝行为，保持安全对齐和基准性能，方法可泛化至不同规模模型。

## 摘要（原文）

> We introduce Refusal Steering, an inference-time method to exercise fine-grained control over Large Language Models refusal behaviour on politically sensitive topics without retraining. We replace fragile pattern-based refusal detection with an LLM-as-a-judge that assigns refusal confidence scores and we propose a ridge-regularized variant to compute steering vectors that better isolate the refusal--compliance direction. On Qwen3-Next-80B-A3B-Thinking, our method removes the refusal behaviour of the model around politically sensitive topics while maintaining safety on JailbreakBench and near-baseline performance on general benchmarks. The approach generalizes across 4B and 80B models and can also induce targeted refusals when desired. We analize the steering vectors and show that refusal signals concentrate in deeper layers of the transformer and are distributed across many dimensions. Together, these results demonstrate that activation steering can remove political refusal behaviour while retaining safety alignment for harmful content, offering a practical path to controllable, transparent moderation at inference time.

