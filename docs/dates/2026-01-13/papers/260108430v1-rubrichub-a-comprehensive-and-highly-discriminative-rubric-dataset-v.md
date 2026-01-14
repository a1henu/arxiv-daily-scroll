---
layout: default
title: RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation
---

# RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation
**arXiv**：[2601.08430v1](https://arxiv.org/abs/2601.08430) · [PDF](https://arxiv.org/pdf/2601.08430.pdf)  
**作者**：Sunzhu Li, Jiale Zhao, Miteto Wei, Huimin Ren, Yang Zhou, Jingwen Yang, Shunyu Liu, Kaike Zhang, Wei Chen  

**一句话要点**：提出自动化粗到细准则生成框架以解决开放生成任务中监督瓶颈问题

**关键词**：准则生成, 开放生成评估, 强化学习, 后训练, 多域数据集, 自动化框架

## 3 点简述
- 开放生成任务因缺乏真实标签而难以优化，现有准则评估方法存在可扩展性瓶颈和标准粗糙问题
- 通过原则引导合成、多模型聚合和难度演化，生成全面且高区分度的准则数据集RubricHub
- 实验显示，基于RubricHub的后训练方法在HealthBench上实现SOTA性能，超越GPT-5等前沿模型

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has driven substantial progress in reasoning-intensive domains like mathematics. However, optimizing open-ended generation remains challenging due to the lack of ground truth. While rubric-based evaluation offers a structured proxy for verification, existing methods suffer from scalability bottlenecks and coarse criteria, resulting in a supervision ceiling effect. To address this, we propose an automated Coarse-to-Fine Rubric Generation framework. By synergizing principle-guided synthesis, multi-model aggregation, and difficulty evolution, our approach produces comprehensive and highly discriminative criteria capable of capturing the subtle nuances. Based on this framework, we introduce RubricHub, a large-scale ($\sim$110k) and multi-domain dataset. We validate its utility through a two-stage post-training pipeline comprising Rubric-based Rejection Sampling Fine-Tuning (RuFT) and Reinforcement Learning (RuRL). Experimental results demonstrate that RubricHub unlocks significant performance gains: our post-trained Qwen3-14B achieves state-of-the-art (SOTA) results on HealthBench (69.3), surpassing proprietary frontier models such as GPT-5. The code and data will be released soon.

