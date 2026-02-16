---
layout: default
title: VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction
---

# VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction
**arXiv**：[2602.12579v1](https://arxiv.org/abs/2602.12579) · [PDF](https://arxiv.org/pdf/2602.12579.pdf)  
**作者**：Xin-Qiang Cai, Masashi Sugiyama  

**一句话要点**：提出VI-CuRL框架，通过置信度引导的方差减少稳定无验证器强化学习推理

**关键词**：强化学习, 无验证器推理, 方差减少, 课程学习, 置信度引导, 大语言模型

## 3 点简述
- 核心问题：无验证器强化学习中梯度方差大导致训练崩溃
- 方法要点：利用模型内在置信度构建课程，优先高置信样本减少方差
- 实验或效果：在六个基准测试中稳定且优于无验证器基线

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a dominant paradigm for enhancing Large Language Models (LLMs) reasoning, yet its reliance on external verifiers limits its scalability. Recent findings suggest that RLVR primarily functions by eliciting latent capabilities, motivating the development of verifier-free algorithms. However, in such settings, standard methods like Group Relative Policy Optimization face a critical challenge: destructive gradient variance that often leads to training collapse. To address this issue, we introduceVerifier-Independent Curriculum Reinforcement Learning (VI-CuRL), a framework that leverages the model's intrinsic confidence to construct a curriculum independent from external verifiers. By prioritizing high-confidence samples, VI-CuRL effectively manages the bias-variance trade-off, specifically targeting the reduction of action and problem variance. We provide a rigorous theoretical analysis, proving that our estimator guarantees asymptotic unbiasedness. Empirically, VI-CuRL promotes stability and consistently outperforms verifier-independent baselines across six challenging benchmarks with/without verifiers.

