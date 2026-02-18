---
layout: default
title: Hybrid Federated and Split Learning for Privacy Preserving Clinical Prediction and Treatment Optimization
---

# Hybrid Federated and Split Learning for Privacy Preserving Clinical Prediction and Treatment Optimization
**arXiv**：[2602.15304v1](https://arxiv.org/abs/2602.15304) · [PDF](https://arxiv.org/pdf/2602.15304.pdf)  
**作者**：Farzana Akter, Rakib Hossain, Deb Kanna Roy Toushi, Mahmood Menon Khan, Sultana Amin, Lisan Al Amin  

**一句话要点**：提出结合联邦学习与分割学习的混合框架，以在隐私保护下支持临床预测与治疗优化。

**关键词**：隐私保护学习, 联邦学习, 分割学习, 临床决策支持, 非独立同分布数据, 成员推理攻击

## 3 点简述
- 核心问题：临床协作决策受隐私规则限制，无法跨机构共享患者原始数据。
- 方法要点：在客户端保留特征提取主干，服务器端托管预测头，实现共享表示学习并应用隐私控制。
- 实验或效果：在非独立同分布数据集上评估，混合框架在预测性能、隐私泄漏和通信开销间提供可调权衡。

## 摘要（原文）

> Collaborative clinical decision support is often constrained by governance and privacy rules that prevent pooling patient-level records across institutions. We present a hybrid privacy-preserving framework that combines Federated Learning (FL) and Split Learning (SL) to support decision-oriented healthcare modeling without raw-data sharing. The approach keeps feature-extraction trunks on clients while hosting prediction heads on a coordinating server, enabling shared representation learning and exposing an explicit collaboration boundary where privacy controls can be applied. Rather than assuming distributed training is inherently private, we audit leakage empirically using membership inference on cut-layer representations and study lightweight defenses based on activation clipping and additive Gaussian noise. We evaluate across three public clinical datasets under non-IID client partitions using a unified pipeline and assess performance jointly along four deployment-relevant axes: factual predictive utility, uplift-based ranking under capacity constraints, audited privacy leakage, and communication overhead. Results show that hybrid FL-SL variants achieve competitive predictive performance and decision-facing prioritization behavior relative to standalone FL or SL, while providing a tunable privacy-utility trade-off that can reduce audited leakage without requiring raw-data sharing. Overall, the work positions hybrid FL-SL as a practical design space for privacy-preserving healthcare decision support where utility, leakage risk, and deployment cost must be balanced explicitly.

