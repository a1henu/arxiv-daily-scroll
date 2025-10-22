---
layout: default
title: From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation
---

# From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation
**arXiv**：[2510.18263v1](https://arxiv.org/abs/2510.18263) · [PDF](https://arxiv.org/pdf/2510.18263.pdf)  
**作者**：Ziwei Huang, Ying Shu, Hao Fang, Quanyu Long, Wenya Wang, Qiushi Guo, Tiezheng Ge, Leilei Gan  

**一句话要点**：提出Customized-GRPO框架以解决主题驱动图像生成中的竞争退化问题

**关键词**：主题驱动图像生成, 强化学习, 奖励塑形, 扩散模型, 竞争退化

## 3 点简述
- 核心问题：在线强化学习在主题驱动图像生成中导致竞争退化，身份保真与提示遵循冲突
- 方法要点：引入Synergy-Aware Reward Shaping和Time-Aware Dynamic Weighting，优化奖励信号
- 实验或效果：方法显著优于基线，实现身份特征保留与复杂提示遵循的平衡

## 摘要（原文）

> Subject-driven image generation models face a fundamental trade-off between
> identity preservation (fidelity) and prompt adherence (editability). While
> online reinforcement learning (RL), specifically GPRO, offers a promising
> solution, we find that a naive application of GRPO leads to competitive
> degradation, as the simple linear aggregation of rewards with static weights
> causes conflicting gradient signals and a misalignment with the temporal
> dynamics of the diffusion process. To overcome these limitations, we propose
> Customized-GRPO, a novel framework featuring two key innovations: (i)
> Synergy-Aware Reward Shaping (SARS), a non-linear mechanism that explicitly
> penalizes conflicted reward signals and amplifies synergistic ones, providing a
> sharper and more decisive gradient. (ii) Time-Aware Dynamic Weighting (TDW),
> which aligns the optimization pressure with the model's temporal dynamics by
> prioritizing prompt-following in the early, identity preservation in the later.
> Extensive experiments demonstrate that our method significantly outperforms
> naive GRPO baselines, successfully mitigating competitive degradation. Our
> model achieves a superior balance, generating images that both preserve key
> identity features and accurately adhere to complex textual prompts.

