---
layout: default
title: Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning
---

# Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning
**arXiv**：[2602.22751v1](https://arxiv.org/abs/2602.22751) · [PDF](https://arxiv.org/pdf/2602.22751.pdf)  
**作者**：Qiannian Zhao, Chen Yang, Jinhao Jing, Yunke Zhang, Xuhui Ren, Lu Yu, Shijie Zhang, Hongzhi Yin  

**一句话要点**：提出EGPO框架，通过元认知熵校准解决强化学习中不确定性-奖励不匹配问题，提升大型推理模型性能。

**关键词**：大型推理模型, 强化学习, 不确定性校准, 元认知熵, 推理性能优化, RLVR框架

## 3 点简述
- 核心问题：现有RLVR方法依赖二元正确性信号，忽略模型内在不确定性，导致不确定性-奖励不匹配，阻碍推理路径优化。
- 方法要点：EGPO利用零开销熵代理估计样本不确定性，通过非对称校准机制对齐内在不确定性与外在正确性，稳定优化策略。
- 实验或效果：在多个基准测试中，EGPO显著且一致地提升推理性能，为大型推理模型提供原则性改进路径。

## 摘要（原文）

> Large reasoning models (LRMs) have emerged as a powerful paradigm for solving complex real-world tasks. In practice, these models are predominantly trained via Reinforcement Learning with Verifiable Rewards (RLVR), yet most existing outcome-only RLVR pipelines rely almost exclusively on a binary correctness signal and largely ignore the model's intrinsic uncertainty. We term this discrepancy the uncertainty-reward mismatch, under which high- and low-uncertainty solutions are treated equivalently, preventing the policy from "Know What You Know" and impeding the shift from optimizing for correct answers to optimizing effective reasoning paths. This limitation is especially critical in reasoning-centric tasks such as mathematics and question answering, where performance hinges on the quality of the model's internal reasoning process rather than mere memorization of final answers. To address this, we propose EGPO, a metacognitive entropy calibration framework that explicitly integrates intrinsic uncertainty into RLVR for enhancing LRMs. EGPO estimates per-sample uncertainty using a zero-overhead entropy proxy derived from token-level likelihoods and aligns it with extrinsic correctness through an asymmetric calibration mechanism that preserves correct reasoning while selectively regulating overconfident failures, thereby enabling stable and uncertainty-aware policy optimization. Moreover, EGPO recovers informative learning signals from otherwise degenerate group-based rollouts without modifying the verifier or reward definition. Extensive experiments across multiple benchmarks demonstrate that the proposed EGPO leads to substantial and consistent improvements in reasoning performance, establishing a principled path for advancing LRMs through metacognitive entropy calibration.

