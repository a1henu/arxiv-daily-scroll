---
layout: default
title: Token-Level LLM Collaboration via FusionRoute
---

# Token-Level LLM Collaboration via FusionRoute
**arXiv**：[2601.05106v1](https://arxiv.org/abs/2601.05106) · [PDF](https://arxiv.org/pdf/2601.05106.pdf)  
**作者**：Nuoya Xiong, Yuhang Zhou, Hanqing Zeng, Zhaorun Chen, Furong Huang, Shuchao Bi, Lizhu Zhang, Zhuokai Zhao  

**一句话要点**：提出FusionRoute框架，通过令牌级多LLM协作解决通用性与效率的权衡问题。

**关键词**：令牌级协作, 多LLM路由, logit融合, 解码优化, 模型泛化

## 3 点简述
- 核心问题：单一通用LLM需大规模扩展成本高，而小型领域专家模型泛化能力有限。
- 方法要点：轻量级路由器在解码时选择专家并贡献互补logit，优化令牌分布。
- 实验或效果：在Llama-3和Gemma-2模型及多基准测试中优于现有协作方法，保持领域专家竞争力。

## 摘要（原文）

> Large language models (LLMs) exhibit strengths across diverse domains. However, achieving strong performance across these domains with a single general-purpose model typically requires scaling to sizes that are prohibitively expensive to train and deploy. On the other hand, while smaller domain-specialized models are much more efficient, they struggle to generalize beyond their training distributions. To address this dilemma, we propose FusionRoute, a robust and effective token-level multi-LLM collaboration framework in which a lightweight router simultaneously (i) selects the most suitable expert at each decoding step and (ii) contributes a complementary logit that refines or corrects the selected expert's next-token distribution via logit addition. Unlike existing token-level collaboration methods that rely solely on fixed expert outputs, we provide a theoretical analysis showing that pure expert-only routing is fundamentally limited: unless strong global coverage assumptions hold, it cannot in general realize the optimal decoding policy. By augmenting expert selection with a trainable complementary generator, FusionRoute expands the effective policy class and enables recovery of optimal value functions under mild conditions. Empirically, across both Llama-3 and Gemma-2 families and diverse benchmarks spanning mathematical reasoning, code generation, and instruction following, FusionRoute outperforms both sequence- and token-level collaboration, model merging, and direct fine-tuning, while remaining competitive with domain experts on their respective tasks.

