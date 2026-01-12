---
layout: default
title: Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR
---

# Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR
**arXiv**：[2601.05607v1](https://arxiv.org/abs/2601.05607) · [PDF](https://arxiv.org/pdf/2601.05607.pdf)  
**作者**：Zijun Min, Bingshuai Liu, Ante Wang, Long Zhang, Anxiang Zeng, Haibo Zhang, Jinsong Su  

**一句话要点**：提出动态混合策略优化以结合令牌级与序列级更新，提升RLVR在推理任务中的性能。

**关键词**：强化学习, 策略优化, 令牌级更新, 序列级更新, 数学推理, 混合机制

## 3 点简述
- 现有RLVR算法在令牌级与序列级更新间存在互补优势与局限性，导致训练不稳定或信用分配不精确。
- DHPO通过加权机制混合令牌级和序列级重要性比率，并采用分支特定裁剪策略稳定训练。
- 在七个数学推理基准测试中，DHPO在Qwen3系列模型上一致优于GRPO和GSPO。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising framework for optimizing large language models in reasoning tasks. However, existing RLVR algorithms focus on different granularities, and each has complementary strengths and limitations. Group Relative Policy Optimization (GRPO) updates the policy with token-level importance ratios, which preserves fine-grained credit assignment but often suffers from high variance and instability. In contrast, Group Sequence Policy Optimization (GSPO) applies single sequence-level importance ratios across all tokens in a response that better matches sequence-level rewards, but sacrifices token-wise credit assignment. In this paper, we propose Dynamic Hybrid Policy Optimization (DHPO) to bridge GRPO and GSPO within a single clipped surrogate objective. DHPO combines token-level and sequence-level importance ratios using weighting mechanisms. We explore two variants of the mixing mechanism, including an averaged mixing and an entropy-guided mixing. To further stabilize training, we employ a branch-specific clipping strategy that constrains token-level and sequence-level ratios within separate trust regions before mixing, preventing outliers in either branch from dominating the update. Across seven challenging mathematical reasoning benchmarks, experiments on both dense and MoE models from the Qwen3 series show that DHPO consistently outperforms GRPO and GSPO. We will release our code upon acceptance of this paper.

