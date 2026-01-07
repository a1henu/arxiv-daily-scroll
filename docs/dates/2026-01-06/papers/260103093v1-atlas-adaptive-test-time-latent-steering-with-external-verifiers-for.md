---
layout: default
title: ATLAS: Adaptive Test-Time Latent Steering with External Verifiers for Enhancing LLMs Reasoning
---

# ATLAS: Adaptive Test-Time Latent Steering with External Verifiers for Enhancing LLMs Reasoning
**arXiv**：[2601.03093v1](https://arxiv.org/abs/2601.03093) · [PDF](https://arxiv.org/pdf/2601.03093.pdf)  
**作者**：Tuc Nguyen, Thai Le  

**一句话要点**：提出ATLAS框架，通过外部验证器动态控制隐层导向以增强大语言模型推理

**关键词**：隐层导向, 推理增强, 自适应控制, 外部验证器, 测试时优化, 大语言模型

## 3 点简述
- 现有隐层导向方法依赖固定策略，导致鲁棒性不足和过度或不足导向问题
- ATLAS使用轻量级外部验证器预测推理质量，动态调整导向决策和强度
- 在数学推理基准测试中，ATLAS提高准确性并显著减少推理时令牌使用

## 摘要（原文）

> Recent work on activation and latent steering has demonstrated that modifying internal representations can effectively guide large language models (LLMs) toward improved reasoning and efficiency without additional training. However, most existing approaches rely on fixed steering policies and static intervention strengths, which limit their robustness across problem instances and often result in over- or under-steering. We propose Adaptive Test-time Latent Steering, called (ATLAS), a task- specific framework that dynamically controls steering decisions at inference time using an external, lightweight latent verifier. Given intermediate hidden states, the verifier predicts the quality of ongoing reasoning and adaptively selects whether and how strongly to apply steering, enabling per-example and per-step adjustment with minimal overhead. To our knowledge, ATLAS is the first method to integrate learned latent verification into test-time steering for enhancing LLMs reasoning. Experiments on multiple mathematical reasoning benchmarks show that ATLAS consistently outperforms both vanilla decoding and fixed steering baselines, achieving higher accuracy while substantially reducing test-time token usage. These results demonstrate that verifier-guided latent adaptation provides an effective and scalable mechanism for controlling reasoning efficiency without sacrificing solution quality. All source code will be publicly available.

