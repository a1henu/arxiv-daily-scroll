---
layout: default
title: VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation
---

# VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation
**arXiv**：[2601.03525v1](https://arxiv.org/abs/2601.03525) · [PDF](https://arxiv.org/pdf/2601.03525.pdf)  
**作者**：Longwen Wang, Xuan'er Wu, Xiaohui Hu, Yirui Liu, Yuankai Fan, Kaidong Yu, Qizhen Weng, Wei Xi, Xuelong Li  

**一句话要点**：提出VeRPO框架，通过可验证执行反馈合成稠密奖励以优化代码生成强化学习。

**关键词**：代码生成, 强化学习, 稠密奖励, 可验证执行, 单元测试, 奖励设计

## 3 点简述
- 核心问题：代码生成强化学习中，传统通过/失败奖励稀疏，外部奖励模型存在对齐偏差和高计算成本。
- 方法要点：基于训练中单元测试执行统计动态估计难度权重，从部分成功合成稠密奖励，并与全局执行结果结合。
- 实验或效果：在多个基准测试中优于基线，最高提升8.83% pass@1，时间成本可忽略且无GPU内存开销。

## 摘要（原文）

> Effective reward design is a central challenge in Reinforcement Learning (RL) for code generation. Mainstream pass/fail outcome rewards enforce functional correctness via executing unit tests, but the resulting sparsity limits potential performance gains. While recent work has explored external Reward Models (RM) to generate richer, continuous rewards, the learned RMs suffer from reward misalignment and prohibitive computational cost. In this paper, we introduce \textbf{VeRPO} (\textbf{V}erifiable D\textbf{e}nse \textbf{R}eward \textbf{P}olicy \textbf{O}ptimization), a novel RL framework for code generation that synthesizes \textit{robust and dense rewards fully grounded in verifiable execution feedback}. The core idea of VeRPO is constructing dense rewards from weighted partial success: by dynamically estimating the difficulty weight of each unit test based on the execution statistics during training, a dense reward is derived from the sum of weights of the passed unit tests. To solidify the consistency between partial success and end-to-end functional correctness, VeRPO further integrates the dense signal with global execution outcomes, establishing a robust and dense reward paradigm relying solely on verifiable execution feedback. Extensive experiments across diverse benchmarks and settings demonstrate that VeRPO consistently outperforms outcome-driven and RM-based baselines, achieving up to +8.83\% gain in pass@1 with negligible time cost (< 0.02\%) and zero GPU memory overhead.

