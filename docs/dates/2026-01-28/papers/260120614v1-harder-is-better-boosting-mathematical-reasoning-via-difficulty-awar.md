---
layout: default
title: Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation
---

# Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation
**arXiv**：[2601.20614v1](https://arxiv.org/abs/2601.20614) · [PDF](https://arxiv.org/pdf/2601.20614.pdf)  
**作者**：Yanqi Dai, Yuxiang Ji, Xiao Zhang, Yong Wang, Xiangxiang Chu, Zhiwu Lu  

**一句话要点**：提出MathForge框架，通过难度感知GRPO和多方面问题重构提升数学推理能力

**关键词**：数学推理, 强化学习, 难度感知优化, 问题重构, 组策略优化

## 3 点简述
- 核心问题：现有方法在算法和数据上缺乏对难题的重视，影响模型能力提升
- 方法要点：结合难度感知组策略优化和多方面问题重构，协同增强难题处理
- 实验或效果：在多种数学推理任务上显著优于现有方法，代码和数据已开源

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) offers a robust mechanism for enhancing mathematical reasoning in large models. However, we identify a systematic lack of emphasis on more challenging questions in existing methods from both algorithmic and data perspectives, despite their importance for refining underdeveloped capabilities. Algorithmically, widely used Group Relative Policy Optimization (GRPO) suffers from an implicit imbalance where the magnitude of policy updates is lower for harder questions. Data-wise, augmentation approaches primarily rephrase questions to enhance diversity without systematically increasing intrinsic difficulty. To address these issues, we propose a two-dual MathForge framework to improve mathematical reasoning by targeting harder questions from both perspectives, which comprises a Difficulty-Aware Group Policy Optimization (DGPO) algorithm and a Multi-Aspect Question Reformulation (MQR) strategy. Specifically, DGPO first rectifies the implicit imbalance in GRPO via difficulty-balanced group advantage estimation, and further prioritizes harder questions by difficulty-aware question-level weighting. Meanwhile, MQR reformulates questions across multiple aspects to increase difficulty while maintaining the original gold answer. Overall, MathForge forms a synergistic loop: MQR expands the data frontier, and DGPO effectively learns from the augmented data. Extensive experiments show that MathForge significantly outperforms existing methods on various mathematical reasoning tasks. The code and augmented data are all available at https://github.com/AMAP-ML/MathForge.

