---
layout: default
title: CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning
---

# CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning
**arXiv**：[2601.22803v1](https://arxiv.org/abs/2601.22803) · [PDF](https://arxiv.org/pdf/2601.22803.pdf)  
**作者**：Ji Shi, Peiming Guo, Meishan Zhang, Miao Zhang, Xuebo Liu, Min Zhang, Weili Guan  

**一句话要点**：提出CVeDRL，通过难度感知强化学习提升代码验证器的效率和可靠性

**关键词**：代码验证, 强化学习, 难度感知, 单元测试, 推理效率

## 3 点简述
- 核心问题：现有代码验证器面临数据稀缺、高失败率和推理效率低的问题
- 方法要点：结合语法和功能奖励，引入分支和样本难度感知的强化学习优化
- 实验或效果：仅0.6B参数，在通过率和分支覆盖率上优于GPT-3.5，推理速度提升20倍以上

## 摘要（原文）

> Code verifiers play a critical role in post-verification for LLM-based code generation, yet existing supervised fine-tuning methods suffer from data scarcity, high failure rates, and poor inference efficiency. While reinforcement learning (RL) offers a promising alternative by optimizing models through execution-driven rewards without labeled supervision, our preliminary results show that naive RL with only functionality rewards fails to generate effective unit tests for difficult branches and samples. We first theoretically analyze showing that branch coverage, sample difficulty, syntactic and functional correctness can be jointly modeled as RL rewards, where optimizing these signals can improve the reliability of unit-test-based verification. Guided by this analysis, we design syntax- and functionality-aware rewards and further propose branch- and sample-difficulty--aware RL using exponential reward shaping and static analysis metrics. With this formulation, CVeDRL achieves state-of-the-art performance with only 0.6B parameters, yielding up to 28.97% higher pass rate and 15.08% higher branch coverage than GPT-3.5, while delivering over $20\times$ faster inference than competitive baselines. Code is available at https://github.com/LIGHTCHASER1/CVeDRL.git

