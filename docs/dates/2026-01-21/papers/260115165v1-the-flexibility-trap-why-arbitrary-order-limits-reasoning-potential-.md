---
layout: default
title: The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models
---

# The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models
**arXiv**：[2601.15165v1](https://arxiv.org/abs/2601.15165) · [PDF](https://arxiv.org/pdf/2601.15165.pdf)  
**作者**：Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang  

**一句话要点**：揭示扩散语言模型中任意顺序生成限制推理潜力，提出JustGRPO方法提升性能

**关键词**：扩散语言模型, 推理能力, 强化学习, 并行解码, 顺序生成

## 3 点简述
- 核心问题：任意顺序生成导致模型绕过高不确定性关键token，缩小推理边界
- 方法要点：放弃任意顺序，应用标准Group Relative Policy Optimization（GRPO）
- 实验或效果：在GSM8K上达到89.1%准确率，保留并行解码能力

## 摘要（原文）

> Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential for general tasks like mathematics and coding. Consequently, numerous works have leveraged reinforcement learning (RL) to elicit the reasoning capability of dLLMs. In this paper, we reveal a counter-intuitive reality: arbitrary order generation, in its current form, narrows rather than expands the reasoning boundary of dLLMs. We find that dLLMs tend to exploit this order flexibility to bypass high-uncertainty tokens that are crucial for exploration, leading to a premature collapse of the solution space. This observation challenges the premise of existing RL approaches for dLLMs, where considerable complexities, such as handling combinatorial trajectories and intractable likelihoods, are often devoted to preserving this flexibility. We demonstrate that effective reasoning is better elicited by intentionally forgoing arbitrary order and applying standard Group Relative Policy Optimization (GRPO) instead. Our approach, JustGRPO, is minimalist yet surprisingly effective (e.g., 89.1% accuracy on GSM8K) while fully retaining the parallel decoding ability of dLLMs. Project page: https://nzl-thu.github.io/the-flexibility-trap

