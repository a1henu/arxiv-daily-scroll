---
layout: default
title: CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal
---

# CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal
**arXiv**：[2512.19554v1](https://arxiv.org/abs/2512.19554) · [PDF](https://arxiv.org/pdf/2512.19554.pdf)  
**作者**：Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang  

**一句话要点**：提出CARE框架，通过对比锚定与反思重采样，将多模态推理中的失败案例转化为监督信号。

**关键词**：多模态推理, 失败学习, 对比学习, 可验证奖励, 视觉推理, 后训练框架

## 3 点简述
- 核心问题：可验证多模态推理中，失败数据常被浪费，导致梯度停滞或信用分配错误。
- 方法要点：结合锚定对比目标与反思引导重采样，从错误中提取学习信号，提升训练稳定性。
- 实验或效果：在Qwen模型上，CARE显著提升多个视觉推理基准的准确率，达到竞争性或最优结果。

## 摘要（原文）

> Group-relative reinforcement learning with verifiable rewards (RLVR) often wastes the most informative data it already has the failures. When all rollouts are wrong, gradients stall; when one happens to be correct, the update usually ignores why the others are close-but-wrong, and credit can be misassigned to spurious chains. We present CARE (Contrastive Anchored REflection), a failure-centric post-training framework for multimodal reasoning that turns errors into supervision. CARE combines: (i) an anchored-contrastive objective that forms a compact subgroup around the best rollout and a set of semantically proximate hard negatives, performs within-subgroup z-score normalization with negative-only scaling, and includes an all-negative rescue to prevent zero-signal batches; and (ii) Reflection-Guided Resampling (RGR), a one-shot structured self-repair that rewrites a representative failure and re-scores it with the same verifier, converting near-misses into usable positives without any test-time reflection. CARE improves accuracy and training smoothness while explicitly increasing the share of learning signal that comes from failures. On Qwen2.5-VL-7B, CARE lifts macro-averaged accuracy by 4.6 points over GRPO across six verifiable visual-reasoning benchmarks; with Qwen3-VL-8B it reaches competitive or state-of-the-art results on MathVista and MMMU-Pro under an identical evaluation protocol.

