---
layout: default
title: MIST-RL: Mutation-based Incremental Suite Testing via Reinforcement Learning
---

# MIST-RL: Mutation-based Incremental Suite Testing via Reinforcement Learning
**arXiv**：[2603.01409v1](https://arxiv.org/abs/2603.01409) · [PDF](https://arxiv.org/pdf/2603.01409.pdf)  
**作者**：Sicheng Zhu, Jiajun Wang, Jiawei Ai, Xin Li  

**一句话要点**：提出MIST-RL框架，通过强化学习优化测试生成，解决大语言模型代码验证中的测试冗余问题。

**关键词**：代码测试生成, 强化学习, 突变测试, 大语言模型验证, 测试冗余优化

## 3 点简述
- 核心问题：现有基于大语言模型的代码验证方法依赖大量测试，导致测试冗余和故障检测收益递减。
- 方法要点：将测试生成建模为序列决策过程，使用GRPO优化，结合增量突变奖励和动态惩罚来抑制冗余断言。
- 实验效果：在HumanEval+和MBPP+上，MIST-RL提升突变分数28.5%，减少测试用例19.3%，并提高下游代码重排准确率3.05%。

## 摘要（原文）

> Large Language Models (LLMs) often fail to generate correct code on the first attempt, which requires using generated unit tests as verifiers to validate the solutions. Despite the success of recent verification methods, they remain constrained by a "scaling-by-quantity" paradigm. This brute-force approach suffers from a critical limitation: it yields diminishing returns in fault detection while causing severe test redundancy. To address this, we propose MIST-RL (Mutation-based Incremental Suite Testing via Reinforcement Learning), a framework that shifts the focus to "scaling-by-utility". We formulate test generation as a sequential decision process optimized via Group Relative Policy Optimization (GRPO). Specifically, we introduce a novel incremental mutation reward combined with dynamic penalties, which incentivizes the model to discover new faults while it suppresses functionally equivalent assertions. Experiments on HumanEval+ and MBPP+ demonstrate that MIST-RL outperforms state-of-the-art baselines. It achieves a +28.5% higher mutation score while reducing the number of test cases by 19.3%. Furthermore, we show that these compact, high-utility tests serve as superior verifiers, which improves downstream code reranking accuracy on HumanEval+ by 3.05% over the SOTA baseline with 10 candidate samples. The source code and data are provided in the supplementary material.

