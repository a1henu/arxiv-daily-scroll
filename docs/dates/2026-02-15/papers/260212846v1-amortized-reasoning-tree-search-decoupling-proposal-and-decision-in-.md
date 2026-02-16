---
layout: default
title: Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models
---

# Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models
**arXiv**：[2602.12846v1](https://arxiv.org/abs/2602.12846) · [PDF](https://arxiv.org/pdf/2602.12846.pdf)  
**作者**：Zesheng Hong, Jiadong Yu, Hui Pan  

**一句话要点**：提出摊销推理树搜索以解决大语言模型在强化学习中对稀有推理路径的抑制问题

**关键词**：大语言模型, 推理路径抑制, 摊销推理树搜索, 流匹配目标, 概率流守恒, 长尾性能恢复

## 3 点简述
- 核心问题：强化学习与可验证奖励范式会系统性地抑制有效但稀有的推理路径，导致长尾性能崩溃
- 方法要点：通过解耦生成与验证，引入流匹配目标来估计概率流守恒，实现稀疏高熵搜索空间的稳健导航
- 实验或效果：在MATH-500基准上达到74.6%性能，匹配全微调策略，并在长尾子集上恢复显著性能

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has established itself as the dominant paradigm for instilling rigorous reasoning capabilities in Large Language Models. While effective at amplifying dominant behaviors, we identify a critical pathology in this alignment process: the systematic suppression of valid but rare (low-likelihood under the base model distribution) reasoning paths. We theoretically characterize this phenomenon as a "Normalization Squeeze," where the interplay between mode-seeking policy gradients and finite sampling acts as a high-pass likelihood filter, driving the probability of rare correct traces to statistical extinction. To counteract this collapse without discarding the base model's latent diversity, we propose Amortized Reasoning Tree Search (ARTS). Unlike standard approaches that force internalization via parameter updates, ARTS prioritizes deliberation by decoupling generation from verification. We introduce a Flow Matching objective that repurposes the verifier to estimate the conservation of probability flow, enabling robust navigation through sparse, high-entropy search spaces where traditional discriminative objectives fail. Extensive experiments on the MATH-500 benchmark demonstrate that ARTS achieves a performance of 74.6% (BoN@16), effectively matching fully fine-tuned policies (74.7%) without modifying the generative backbone. Crucially, on the long-tail subset where coupled RL optimization collapses to 0% pass@k, ARTS uniquely recovers significant performance, suggesting that disentangling verification from generation offers a more robust pathway for solving complex reasoning tasks.

