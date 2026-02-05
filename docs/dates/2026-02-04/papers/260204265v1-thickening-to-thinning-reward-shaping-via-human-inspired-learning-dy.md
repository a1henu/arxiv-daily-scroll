---
layout: default
title: Thickening-to-Thinning: Reward Shaping via Human-Inspired Learning Dynamics for LLM Reasoning
---

# Thickening-to-Thinning: Reward Shaping via Human-Inspired Learning Dynamics for LLM Reasoning
**arXiv**：[2602.04265v1](https://arxiv.org/abs/2602.04265) · [PDF](https://arxiv.org/pdf/2602.04265.pdf)  
**作者**：Wenze Lin, Zhen Yang, Xitai Jiang, Pony Ma, Gao Huang  

**一句话要点**：提出T2T动态奖励框架以解决LLM推理中奖励设计不足的问题

**关键词**：强化学习, 大语言模型推理, 动态奖励框架, 人类学习启发, 数学问题求解, 奖励塑造

## 3 点简述
- 核心问题：现有奖励方案无法区分问题求解中的广泛搜索需求与已掌握知识的高效性要求
- 方法要点：基于人类学习过程，设计双阶段机制，错误时激励加厚搜索，正确时惩罚冗余以促进精简
- 实验或效果：在数学基准测试中显著优于标准GRPO和近期基线，实现更优性能

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for enhancing reasoning in Large Language Models (LLMs). However, it frequently encounters challenges such as entropy collapse, excessive verbosity, and insufficient exploration for hard problems. Crucially, existing reward schemes fail to distinguish between the need for extensive search during problem-solving and the efficiency required for mastered knowledge. In this work, we introduce T2T(Thickening-to-Thinning), a dynamic reward framework inspired by human learning processes. Specifically, it implements a dual-phase mechanism: (1) On incorrect attempts, T2T incentivizes "thickening" (longer trajectories) to broaden the search space and explore novel solution paths; (2) Upon achieving correctness, it shifts to "thinning", imposing length penalties to discourage redundancy, thereby fostering model confidence and crystallizing reasoning capabilities. Extensive experiments on mathematical benchmarks (MATH-500, AIME, AMC) across Qwen-series and Deepseek models demonstrate that T2T significantly outperforms standard GRPO and recent baselines, achieving superior performance.

