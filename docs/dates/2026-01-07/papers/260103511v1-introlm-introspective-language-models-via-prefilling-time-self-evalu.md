---
layout: default
title: IntroLM: Introspective Language Models via Prefilling-Time Self-Evaluation
---

# IntroLM: Introspective Language Models via Prefilling-Time Self-Evaluation
**arXiv**：[2601.03511v1](https://arxiv.org/abs/2601.03511) · [PDF](https://arxiv.org/pdf/2601.03511.pdf)  
**作者**：Hossein Hosseini Kasnavieh, Gholamreza Haffari, Chris Leckie, Adel N. Toosi  

**一句话要点**：提出IntroLM方法，使因果语言模型在预填充阶段自评估输出质量，以优化多模型路由系统性能。

**关键词**：自省语言模型, 输出质量预测, 令牌条件LoRA, 多模型路由, 预填充阶段评估, 计算效率优化

## 3 点简述
- 核心问题：现有方法依赖外部分类器预测LLM输出质量，存在上下文窗口限制、计算开销大等问题。
- 方法要点：通过引入仅对自省令牌激活的令牌条件LoRA，模型在预填充阶段预测输出质量，不影响生成且无需外部评估器。
- 实验或效果：在问答基准上，IntroLM应用于Qwen3 8B实现90% ROC AUC，优于DeBERTa分类器14%，集成路由系统可降低延迟33%和大模型使用50%。

## 摘要（原文）

> A major challenge for the operation of large language models (LLMs) is how to predict whether a specific LLM will produce sufficiently high-quality output for a given query. Existing approaches rely on external classifiers, most commonly BERT based models, which suffer from limited context windows, constrained representational capacity, and additional computational overhead. We propose IntroLM, a method that enables causal language models to predict their own output quality during the prefilling phase without affecting generation using introspective tokens. By introducing token conditional LoRA that activates only for the introspective token, the model learns to predict the output quality for a given query while preserving the original backbone behavior and avoiding external evaluators. On question answering benchmarks, IntroLM applied to Qwen3 8B achieves a ROC AUC of 90 precent for success prediction, outperforming a DeBERTa classifier by 14 precent. When integrated into multi model routing systems, IntroLM achieves superior cost performance tradeoffs, reducing latency by up to 33 precent and large model usage by up to 50 precent at matched reliability.

