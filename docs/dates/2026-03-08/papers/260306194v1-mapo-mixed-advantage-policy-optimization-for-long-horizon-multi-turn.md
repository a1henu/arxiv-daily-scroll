---
layout: default
title: MAPO: Mixed Advantage Policy Optimization for Long-Horizon Multi-Turn Dialogue
---

# MAPO: Mixed Advantage Policy Optimization for Long-Horizon Multi-Turn Dialogue
**arXiv**：[2603.06194v1](https://arxiv.org/abs/2603.06194) · [PDF](https://arxiv.org/pdf/2603.06194.pdf)  
**作者**：Naifan Zhang, Ruihan Sun, Jinwei Su, Hengjie Yang, Zhengyuan Pan, Zhaohan Chen, Xiaofan Zhang  

**一句话要点**：提出MAPO算法，通过混合优势估计和密集过程反馈解决长程多轮主观对话的强化学习挑战。

**关键词**：多轮对话, 强化学习, 信用分配, 主观任务, 过程监督, 混合优势估计

## 3 点简述
- 核心问题：长程多轮主观对话中，仅基于结果的强化学习难以分配信用，且交互环境采样成本高。
- 方法要点：利用法官模型提供密集过程反馈，结合蒙特卡洛回报和混合优势估计器进行细粒度信用分配。
- 实验或效果：在多个主观对话基准上提升训练稳定性和性能，并在未见基准上展现良好泛化能力。

## 摘要（原文）

> Subjective multi-turn dialogue tasks, such as emotional support, require conversational policies that adapt to evolving user states and optimize long-horizon interaction quality. However, reinforcement learning (RL) for such settings remains challenging due to the absence of reliable process supervision. Outcome-only training collapses credit assignment across turns into a single trajectory-level reward, while naïve turn-level group sampling incurs prohibitive rollout costs in interactive environments. We propose a critic-free and efficient RL algorithm named MAPO that leverages dense process feedback from a judge model and propagates long-horizon effects through Monte Carlo returns. To stabilize optimization, we introduce a mixed advantage estimator that combines turn-level normalization with batch-level normalization, enabling fine-grained yet scalable credit assignment. Across multiple subjective dialogue benchmarks, including EMPA, EmoBench, and EQ-Bench, and model scales ranging from 7B to 32B, our method consistently improves both training stability and final performance over outcome-only GRPO and single-level normalization baselines. On EMPA, we improve rates by up to 9 points and increase dialogue scores by as much as +43.2 over the 7B base model. Despite training only on EMPA-style environments, our approach generalizes well, yielding consistent improvements on unseen emotional-intelligence benchmarks, including up to +4 points on EmoBench and +3.5 on EQ-Bench. Together, these results demonstrate that dense process supervision combined with mixed-level normalization enables effective and scalable RL for subjective, open-ended multi-turn dialogue.

