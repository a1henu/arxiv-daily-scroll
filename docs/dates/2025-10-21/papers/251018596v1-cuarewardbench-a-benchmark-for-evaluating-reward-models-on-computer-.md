---
layout: default
title: CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent
---

# CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent
**arXiv**：[2510.18596v1](https://arxiv.org/abs/2510.18596) · [PDF](https://arxiv.org/pdf/2510.18596.pdf)  
**作者**：Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun  

**一句话要点**：提出CUARewardBench基准以评估计算机使用代理的奖励模型

**关键词**：计算机使用代理, 奖励模型评估, 轨迹数据集, 视觉语言模型, 一致提示集成, 软件交互任务

## 3 点简述
- 核心问题：现有基于脚本的评估方法可扩展性差，无法提供逐步评估。
- 方法要点：构建首个综合基准，支持结果和过程奖励模型的轨迹级与步骤级评估。
- 实验或效果：通过广泛实验揭示当前模型局限，并提出UPE方法显著提升可靠性。

## 摘要（原文）

> Computer-using agents (CUAs) enable task completion through natural
> interaction with operating systems and software interfaces. While script-based
> verifiers are widely adopted for evaluation, they suffer from limited
> scalability and inability to provide step-wise assessment. Reward models offer
> promising alternatives, but their effectiveness on CUA evaluation remains
> largely underexplored. To address this gap, we present CUARewardBench,
> comprising four key contributions: (1) First-ever Comprehensive CUA Reward
> Benchmark: We introduce the first benchmark for evaluating both outcome reward
> models (ORM) and process reward models (PRM) on CUA tasks, enabling systematic
> assessment across trajectory-level and step-level evaluation. (2) Diverse,
> Practical and Reliable Dataset: CUARewardBench encompasses trajectories from 10
> software categories and 7 agent architectures with varying performance levels
> (25.9%-50.8% success rates). All trajectories are expertly annotated through
> carefully designed protocols, with rigorous quality control to ensure
> reliability and practical applicability. (3) Comprehensive Analysis and
> Insights: Through extensive experiments across 7 vision-language models and 3
> prompt templates, we reveal critical limitations of current CUA RMs, including
> insufficient visual reasoning capabilities, knowledge deficiencies, and the
> superiority of general VLMs over specialized CUA models for reward evaluation.
> (4) Unanimous Prompt Ensemble (UPE): Based on the insights from our
> comprehensive analysis, we propose UPE, a novel ensemble method that
> significantly enhances reward model reliability through strict unanimous voting
> and strategic prompt-template configurations. UPE achieves 89.8% precision and
> 93.3% NPV for ORM, and 81.7% precision and 85.1% NPV for PRM, substantially
> outperforming single VLMs and traditional ensemble approaches.

