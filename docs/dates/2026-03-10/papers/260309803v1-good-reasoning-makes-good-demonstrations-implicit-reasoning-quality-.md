---
layout: default
title: Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning
---

# Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning
**arXiv**：[2603.09803v1](https://arxiv.org/abs/2603.09803) · [PDF](https://arxiv.org/pdf/2603.09803.pdf)  
**作者**：Tiehua Mei, Minxuan Lv, Leiyu Pan, Zhenpeng Su, Hongru Hou, Hengrui Chen, Ao Xu, Deqing Yang  

**一句话要点**：提出In-Context RLVR方法，通过隐式推理质量监督提升大语言模型的推理能力。

**关键词**：推理质量监督, 上下文强化学习, 大语言模型, 贝叶斯分析, 演示效用

## 3 点简述
- 核心问题：RLVR方法可能强化偶然正确的低质量推理轨迹，忽略推理质量差异。
- 方法要点：利用模型自身上下文学习能力测量演示效用，通过贝叶斯分析隐式重加权奖励。
- 实验或效果：在数学基准测试中，相比标准RLVR，提高了准确性和推理质量。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) improves reasoning in large language models but treats all correct solutions equally, potentially reinforcing flawed traces that get correct answers by chance. We observe that better reasoning are better teachers: high-quality solutions serve as more effective demonstrations than low-quality ones. We term this teaching ability Demonstration Utility, and show that the policy model's own in-context learning ability provides an efficient way to measure it, yielding a quality signal termed Evidence Gain. To employ this signal during training, we introduce In-Context RLVR. By Bayesian analysis, we show that this objective implicitly reweights rewards by Evidence Gain, assigning higher weights to high-quality traces and lower weights to low-quality ones, without requiring costly computation or external evaluators. Experiments on mathematical benchmarks show improvements in both accuracy and reasoning quality over standard RLVR.

