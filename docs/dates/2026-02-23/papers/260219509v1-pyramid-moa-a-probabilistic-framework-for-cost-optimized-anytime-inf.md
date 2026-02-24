---
layout: default
title: Pyramid MoA: A Probabilistic Framework for Cost-Optimized Anytime Inference
---

# Pyramid MoA: A Probabilistic Framework for Cost-Optimized Anytime Inference
**arXiv**：[2602.19509v1](https://arxiv.org/abs/2602.19509) · [PDF](https://arxiv.org/pdf/2602.19509.pdf)  
**作者**：Arindam Khaled  

**一句话要点**：提出Pyramid MoA框架，通过分层代理混合架构优化大语言模型推理成本与性能平衡。

**关键词**：大语言模型, 推理优化, 分层架构, 成本效益, 动态路由, 置信度校准

## 3 点简述
- 核心问题：大语言模型在推理成本与能力间存在权衡，大模型昂贵，小模型处理复杂任务能力不足。
- 方法要点：使用轻量级路由器动态升级查询，基于小模型集合的语义一致性和置信度校准识别难题。
- 实验或效果：在GSM8K基准上达到93.0%准确率，接近Oracle基线，计算成本降低61%，延迟开销可忽略。

## 摘要（原文）

> Large Language Models (LLMs) face a persistent trade-off between inference cost and reasoning capability. While "Oracle" models (e.g., Llama-3-70B) achieve state-of-the-art accuracy, they are prohibitively expensive for high-volume deployment. Smaller models (e.g., 8B parameters) are cost-effective but struggle with complex tasks. In this work, we propose "Pyramid MoA", a hierarchical Mixture-of-Agents architecture that uses a lightweight Router to dynamically escalate queries only when necessary. By leveraging semantic agreement and confidence calibration among an ensemble of small models, our Router identifies "hard" problems with high precision. On the GSM8K benchmark, our system achieves 93.0% accuracy, effectively matching the Oracle baseline (98.0%) while reducing compute costs by 61%. We demonstrate that the system introduces negligible latency overhead (+0.82s) and allows for a tunable trade-off between performance and budget.

