---
layout: default
title: $φ$-DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models
---

# $φ$-DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models
**arXiv**：[2602.22601v1](https://arxiv.org/abs/2602.22601) · [PDF](https://arxiv.org/pdf/2602.22601.pdf)  
**作者**：Thanh-Dat Truong, Huu-Thien Tran, Jackson Cothren, Bhiksha Raj, Khoa Luu  

**一句话要点**：提出φ-DPO框架以解决大型多模态模型持续学习中的公平性问题

**关键词**：持续学习, 大型多模态模型, 公平性优化, 直接偏好优化, 数据不平衡, 灾难性遗忘

## 3 点简述
- 核心问题：持续学习中数据分布不平衡导致模型更新偏差和跨任务性能下降。
- 方法要点：基于直接偏好优化提出φ-DPO损失，显式处理分布偏差以缓解灾难性遗忘。
- 实验或效果：在多个基准测试中实现最先进性能，优于现有持续学习方法。

## 摘要（原文）

> Fairness in Continual Learning for Large Multimodal Models (LMMs) is an emerging yet underexplored challenge, particularly in the presence of imbalanced data distributions that can lead to biased model updates and suboptimal performance across tasks. While recent continual learning studies have made progress in addressing catastrophic forgetting, the problem of fairness caused the imbalanced data remains largely underexplored. This paper presents a novel Fairness Direct Preference Optimization (FaiDPO or $φ$-DPO) framework for continual learning in LMMs. In particular, we first propose a new continual learning paradigm based on Direct Preference Optimization (DPO) to mitigate catastrophic forgetting by aligning learning with pairwise preference signals. Then, we identify the limitations of conventional DPO in imbalanced data and present a new $φ$-DPO loss that explicitly addresses distributional biases. We provide a comprehensive theoretical analysis demonstrating that our approach addresses both forgetting and data imbalance. Additionally, to enable $φ$-DPO-based continual learning, we construct pairwise preference annotations for existing benchmarks in the context of continual learning. Extensive experiments and ablation studies show the proposed $φ$-DPO achieves State-of-the-Art performance across multiple benchmarks, outperforming prior continual learning methods of LMMs.

