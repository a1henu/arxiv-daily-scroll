---
layout: default
title: Beyond Imitation: Reinforcement Learning for Active Latent Planning
---

# Beyond Imitation: Reinforcement Learning for Active Latent Planning
**arXiv**：[2601.21598v1](https://arxiv.org/abs/2601.21598) · [PDF](https://arxiv.org/pdf/2601.21598.pdf)  
**作者**：Zhi Zheng, Wee Sun Lee  

**一句话要点**：提出ATP-Latent方法，通过强化学习优化潜在推理策略以提升大语言模型的规划能力。

**关键词**：潜在推理, 强化学习, 变分自编码器, 大语言模型, 规划能力

## 3 点简述
- 核心问题：现有潜在推理方法被动模仿语言标签，导致潜在表示和推理策略不佳，影响规划能力。
- 方法要点：使用条件变分自编码器平滑潜在空间，并引入基于一致性的强化学习奖励优化推理策略。
- 实验或效果：在LLaMA-1B上，相比先进基线，在四个基准测试中准确率提升4.1%，令牌消耗减少3.3%。

## 摘要（原文）

> Aiming at efficient and dense chain-of-thought (CoT) reasoning, latent reasoning methods fine-tune Large Language Models (LLMs) to substitute discrete language tokens with continuous latent tokens. These methods consume fewer tokens compared to the conventional language CoT reasoning and have the potential to plan in a dense latent space. However, current latent tokens are generally supervised based on imitating language labels. Considering that there can be multiple equivalent but diverse CoT labels for a question, passively imitating an arbitrary one may lead to inferior latent token representations and latent reasoning policies, undermining the potential planning ability and resulting in clear gaps between training and testing. In this work, we emphasize the importance of active planning over the representation space of latent tokens in achieving the optimal latent reasoning policy. So, we propose the \underline{A}c\underline{t}ive Latent \underline{P}lanning method (ATP-Latent), which models the supervision process of latent tokens as a conditional variational auto-encoder (VAE) to obtain a smoother latent space. Moreover, to facilitate the most reasonable latent reasoning policy, ATP-Latent conducts reinforcement learning (RL) with an auxiliary coherence reward, which is calculated based on the consistency between VAE-decoded contents of latent tokens, enabling a guided RL process. In experiments on LLaMA-1B, ATP-Latent demonstrates +4.1\% accuracy and -3.3\% tokens on four benchmarks compared to advanced baselines. Codes are available on https://github.com/zz1358m/ATP-Latent-master.

