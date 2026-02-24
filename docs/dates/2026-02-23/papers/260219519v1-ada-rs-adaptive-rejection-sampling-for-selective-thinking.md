---
layout: default
title: Ada-RS: Adaptive Rejection Sampling for Selective Thinking
---

# Ada-RS: Adaptive Rejection Sampling for Selective Thinking
**arXiv**：[2602.19519v1](https://arxiv.org/abs/2602.19519) · [PDF](https://arxiv.org/pdf/2602.19519.pdf)  
**作者**：Yirou Ge, Yixi Li, Alec Chiu, Shivani Shekhar, Zijie Pan, Avinash Thangali, Yun-Shiuan Chuang, Chaitanya Kulkarni, Uma Kona, Linsey Pang, Prakhar Mehrotra  

**一句话要点**：提出自适应拒绝采样框架以优化工具调用大语言模型的选择性推理效率

**关键词**：选择性推理, 自适应拒绝采样, 工具调用大语言模型, 效率优化, 偏好学习, 延迟敏感部署

## 3 点简述
- 核心问题：链式思维在简单请求中浪费计算资源，影响成本与延迟敏感部署
- 方法要点：通过自适应长度惩罚奖励评分，结合随机拒绝采样筛选高质量推理样本
- 实验或效果：在合成电商基准上，减少输出令牌达80%，降低思考率95%，保持或提升工具调用准确率

## 摘要（原文）

> Large language models (LLMs) are increasingly being deployed in cost and latency-sensitive settings. While chain-of-thought improves reasoning, it can waste tokens on simple requests. We study selective thinking for tool-using LLMs and introduce Adaptive Rejection Sampling (Ada-RS), an algorithm-agnostic sample filtering framework for learning selective and efficient reasoning. For each given context, Ada-RS scores multiple sampled completions with an adaptive length-penalized reward then applies stochastic rejection sampling to retain only high-reward candidates (or preference pairs) for downstream optimization. We demonstrate how Ada-RS plugs into both preference pair (e.g. DPO) or grouped policy optimization strategies (e.g. DAPO). Using Qwen3-8B with LoRA on a synthetic tool call-oriented e-commerce benchmark, Ada-RS improves the accuracy-efficiency frontier over standard algorithms by reducing average output tokens by up to 80% and reducing thinking rate by up to 95% while maintaining or improving tool call accuracy. These results highlight that training-signal selection is a powerful lever for efficient reasoning in latency-sensitive deployments.

