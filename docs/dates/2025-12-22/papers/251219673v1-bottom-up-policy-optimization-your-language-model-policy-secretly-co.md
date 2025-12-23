---
layout: default
title: Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies
---

# Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies
**arXiv**：[2512.19673v1](https://arxiv.org/abs/2512.19673) · [PDF](https://arxiv.org/pdf/2512.19673.pdf)  
**作者**：Yuqiao Tan, Minzheng Wang, Shizhu He, Huanxuan Liao, Chengfeng Zhao, Qiunan Lu, Tian Liang, Jun Zhao, Kang Liu  

**一句话要点**：提出自底向上策略优化以优化大语言模型内部策略，提升复杂推理性能

**关键词**：大语言模型, 强化学习, 策略分解, Transformer, 推理优化, 自底向上优化

## 3 点简述
- 现有强化学习将大语言模型视为单一策略，忽略内部机制演化
- 通过分解Transformer残差流揭示内部层策略和模块策略，分析熵变化模式
- 自底向上策略优化直接优化早期层策略，在复杂推理基准上表现优异

## 摘要（原文）

> Existing reinforcement learning (RL) approaches treat large language models (LLMs) as a single unified policy, overlooking their internal mechanisms. Understanding how policy evolves across layers and modules is therefore crucial for enabling more targeted optimization and raveling out complex reasoning mechanisms. In this paper, we decompose the language model policy by leveraging the intrinsic split of the Transformer residual stream and the equivalence between the composition of hidden states with the unembedding matrix and the resulting samplable policy. This decomposition reveals Internal Layer Policies, corresponding to contributions from individual layers, and Internal Modular Policies, which align with the self-attention and feed-forward network (FFN) components within each layer. By analyzing the entropy of internal policy, we find that: (a) Early layers keep high entropy for exploration, top layers converge to near-zero entropy for refinement, with convergence patterns varying across model series. (b) LLama's prediction space rapidly converges in the final layer, whereas Qwen-series models, especially Qwen3, exhibit a more human-like, progressively structured reasoning pattern. Motivated by these findings, we propose Bottom-up Policy Optimization (BuPO), a novel RL paradigm that directly optimizes the internal layer policy during early training. By aligning training objective at lower layer, BuPO reconstructs foundational reasoning capabilities and achieves superior performance. Extensive experiments on complex reasoning benchmarks demonstrates the effectiveness of our method. Our code is available at https://github.com/Trae1ounG/BuPO.

