---
layout: default
title: Leaderboard Incentives: Model Rankings under Strategic Post-Training
---

# Leaderboard Incentives: Model Rankings under Strategic Post-Training
**arXiv**：[2603.08371v1](https://arxiv.org/abs/2603.08371) · [PDF](https://arxiv.org/pdf/2603.08371.pdf)  
**作者**：Yatong Chen, Guanhua Zhang, Moritz Hardt  

**一句话要点**：提出tune-before-test协议以解决基准测试中模型开发者策略性优化导致的排名失真问题

**关键词**：基准测试, 博弈论, 模型排名, 后训练优化, 激励结构, 评估协议

## 3 点简述
- 核心问题：基准测试激励模型开发者策略性分配后训练资源，导致排名无法反映真实质量
- 方法要点：将基准测试建模为Stackelberg博弈，分析不同评估协议的激励结构
- 实验或效果：证明当前基准无纳什均衡，而tune-before-test协议能诱导唯一均衡并实现真实质量排名

## 摘要（原文）

> Influential benchmarks incentivize competing model developers to strategically allocate post-training resources toward improvements on the leaderboard, a phenomenon dubbed benchmaxxing or training on the test task. In this work, we initiate a principled study of the incentive structure that benchmarks induce. We model benchmarking as a Stackelberg game between a benchmark designer who chooses an evaluation protocol and multiple model developers who compete simultaneously in a subgame given by the designer's choice. Each competitor has a model of unknown latent quality and can inflate its observed score by allocating resources to benchmark-specific improvements. First, we prove that current benchmarks induce games for which no Nash equilibrium between model developers exists. This result suggests one explanation for why current practice leads to misaligned incentives, prompting model developers to strategize in opaque ways. However, we prove that under mild conditions, a recently proposed evaluation protocol, called tune-before-test, induces a benchmark with a unique Nash equilibrium that ranks models by latent quality. This positive result demonstrates that benchmarks need not set bad incentives, even if current evaluations do.

