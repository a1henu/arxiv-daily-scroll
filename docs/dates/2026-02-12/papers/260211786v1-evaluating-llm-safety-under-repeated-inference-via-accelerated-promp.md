---
layout: default
title: Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing
---

# Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing
**arXiv**：[2602.11786v1](https://arxiv.org/abs/2602.11786) · [PDF](https://arxiv.org/pdf/2602.11786.pdf)  
**作者**：Keita Broadwater  

**一句话要点**：提出加速提示压力测试以评估大语言模型在重复推理下的安全可靠性

**关键词**：大语言模型安全评估, 重复推理可靠性, 加速提示压力测试, 伯努利模型, 操作风险分析, 基准测试补充

## 3 点简述
- 核心问题：传统基准测试侧重广度评估，忽略重复推理下的操作风险，如幻觉和不一致拒绝
- 方法要点：引入APST框架，通过重复采样相同提示，用伯努利和二项模型量化每次推理的失败概率
- 实验或效果：应用于多个指令调优LLM，发现相似基准分数的模型在重复采样下失败率差异显著，温度升高时更明显

## 摘要（原文）

> Traditional benchmarks for large language models (LLMs) primarily assess safety risk through breadth-oriented evaluation across diverse tasks. However, real-world deployment exposes a different class of risk: operational failures arising from repeated inference on identical or near-identical prompts rather than broad task generalization. In high-stakes settings, response consistency and safety under sustained use are critical. We introduce Accelerated Prompt Stress Testing (APST), a depth-oriented evaluation framework inspired by reliability engineering. APST repeatedly samples identical prompts under controlled operational conditions (e.g., decoding temperature) to surface latent failure modes including hallucinations, refusal inconsistency, and unsafe completions. Rather than treating failures as isolated events, APST models them as stochastic outcomes of independent inference events. We formalize safety failures using Bernoulli and binomial models to estimate per-inference failure probabilities, enabling quantitative comparison of reliability across models and decoding configurations. Applying APST to multiple instruction-tuned LLMs evaluated on AIR-BENCH-derived safety prompts, we find that models with similar benchmark-aligned scores can exhibit substantially different empirical failure rates under repeated sampling, particularly as temperature increases. These results demonstrate that shallow, single-sample evaluation can obscure meaningful reliability differences under sustained use. APST complements existing benchmarks by providing a practical framework for evaluating LLM safety and reliability under repeated inference, bridging benchmark alignment and deployment-oriented risk assessment.

