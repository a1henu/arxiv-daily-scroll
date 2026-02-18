---
layout: default
title: Improving LLM Reliability through Hybrid Abstention and Adaptive Detection
---

# Improving LLM Reliability through Hybrid Abstention and Adaptive Detection
**arXiv**：[2602.15391v1](https://arxiv.org/abs/2602.15391) · [PDF](https://arxiv.org/pdf/2602.15391.pdf)  
**作者**：Ankit Sharma, Nachiket Tapas, Jyotiprakash Patra  

**一句话要点**：提出自适应弃权系统以解决LLM部署中的安全与效用权衡问题

**关键词**：LLM安全, 自适应弃权, 上下文感知检测, 级联机制, 延迟优化, 误报减少

## 3 点简述
- 核心问题：LLM部署面临安全过滤与用户效用间的权衡，传统静态规则或固定阈值方法存在上下文不敏感和高延迟问题。
- 方法要点：引入基于实时上下文信号（如领域和用户历史）动态调整安全阈值的自适应弃权系统，集成五并行检测器的多维检测架构，通过分层级联机制优化速度与精度。
- 实验或效果：在混合和特定领域工作负载上评估，显著减少误报，尤其在医疗建议和创意写作等敏感领域，保持高安全精度和近乎完美的召回率，同时降低延迟。

## 摘要（原文）

> Large Language Models (LLMs) deployed in production environments face a fundamental safety-utility trade-off either a strict filtering mechanisms prevent harmful outputs but often block benign queries or a relaxed controls risk unsafe content generation. Conventional guardrails based on static rules or fixed confidence thresholds are typically context-insensitive and computationally expensive, resulting in high latency and degraded user experience. To address these limitations, we introduce an adaptive abstention system that dynamically adjusts safety thresholds based on real-time contextual signals such as domain and user history. The proposed framework integrates a multi-dimensional detection architecture composed of five parallel detectors, combined through a hierarchical cascade mechanism to optimize both speed and precision. The cascade design reduces unnecessary computation by progressively filtering queries, achieving substantial latency improvements compared to non-cascaded models and external guardrail systems. Extensive evaluation on mixed and domain-specific workloads demonstrates significant reductions in false positives, particularly in sensitive domains such as medical advice and creative writing. The system maintains high safety precision and near-perfect recall under strict operating modes. Overall, our context-aware abstention framework effectively balances safety and utility while preserving performance, offering a scalable solution for reliable LLM deployment.

