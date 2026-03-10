---
layout: default
title: DARC: Disagreement-Aware Alignment via Risk-Constrained Decoding
---

# DARC: Disagreement-Aware Alignment via Risk-Constrained Decoding
**arXiv**：[2603.08145v1](https://arxiv.org/abs/2603.08145) · [PDF](https://arxiv.org/pdf/2603.08145.pdf)  
**作者**：Mingxi Zou, Jiaxiang Chen, Junfan Li, Langzhang Liang, Qifan Wang, Xu Yinghui, Zenglin Xu  

**一句话要点**：提出DARC方法，通过风险约束解码解决偏好对齐中的异质分歧问题。

**关键词**：偏好对齐, 风险约束解码, KL鲁棒性, 异质偏好, 推理时优化

## 3 点简述
- 核心问题：偏好对齐方法在异质人类偏好下，平均奖励最大化易受分歧和代理过优化影响。
- 方法要点：DARC作为免重训练推理时方法，通过KL鲁棒性目标重排序候选响应，并控制熵风险溢价。
- 实验或效果：在基准测试中减少分歧和尾部风险，同时保持平均质量。

## 摘要（原文）

> Preference-based alignment methods (e.g., RLHF, DPO) typically optimize a single scalar objective, implicitly averaging over heterogeneous human preferences. In practice, systematic annotator and user-group disagreement makes mean-reward maximization brittle and susceptible to proxy over-optimization. We propose **Disagreement-Aware Alignment via Risk-Constrained Decoding (DARC)**, a retraining-free inference-time method that frames response selection as distributionally robust, risk-sensitive decision making. Given multiple preference samples or scalable disagreement proxies, DARC reranks candidates by maximizing a *KL-robust (entropic)* satisfaction objective, and provides simple deployment controls that cap or penalize the corresponding entropic risk premium relative to the mean, enabling explicit risk budgets without retraining. We provide theoretical characterization linking this decoding rule to principled pessimism and KL-based distributionally robust optimization. Experiments on alignment benchmarks show that DARC reduces disagreement and tail risk while maintaining competitive average quality under noisy, heterogeneous feedback.

