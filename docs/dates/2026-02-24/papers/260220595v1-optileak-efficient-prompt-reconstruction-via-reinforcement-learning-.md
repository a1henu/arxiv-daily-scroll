---
layout: default
title: OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
---

# OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
**arXiv**：[2602.20595v1](https://arxiv.org/abs/2602.20595) · [PDF](https://arxiv.org/pdf/2602.20595.pdf)  
**作者**：Longxiang Wang, Xiang Zheng, Xuhao Zhang, Yao Zhang, Ye Wu, Cong Wang  

**一句话要点**：提出OptiLeak框架，通过强化学习优化多租户LLM服务中的提示词重构效率。

**关键词**：多租户LLM服务, 提示词泄漏攻击, 强化学习优化, 缓存侧信道, 直接偏好优化, 隐私风险评估

## 3 点简述
- 核心问题：多租户LLM共享缓存导致侧信道漏洞，现有攻击方法成本高，低估隐私风险。
- 方法要点：基于强化学习的两阶段微调，自动识别硬令牌并用于直接偏好优化，避免手动标注。
- 实验或效果：在医疗和金融基准测试中，平均每令牌请求数减少高达12.48倍，模型规模从3B到14B均有效。

## 摘要（原文）

> Multi-tenant LLM serving frameworks widely adopt shared Key-Value caches to enhance efficiency. However, this creates side-channel vulnerabilities enabling prompt leakage attacks. Prior studies identified these attack surfaces yet focused on expanding attack vectors rather than optimizing attack performance, reporting impractically high attack costs that underestimate the true privacy risk. We propose OptiLeak, a reinforcement learning-enhanced framework that maximizes prompt reconstruction efficiency through two-stage fine-tuning. Our key insight is that domain-specific ``hard tokens'' -- terms difficult to predict yet carrying sensitive information -- can be automatically identified via likelihood ranking and used to construct preference pairs for Direct Preference Optimization, eliminating manual annotation. This enables effective preference alignment while avoiding the overfitting issues of extended supervised fine-tuning. Evaluated on three benchmarks spanning medical and financial domains, OptiLeak achieves up to $12.48\times$ reduction in average requests per token compared to baseline approaches, with consistent improvements across model scales from 3B to 14B parameters. Our findings demonstrate that cache-based prompt leakage poses a more severe threat than previously reported, underscoring the need for robust cache isolation in production deployments.

