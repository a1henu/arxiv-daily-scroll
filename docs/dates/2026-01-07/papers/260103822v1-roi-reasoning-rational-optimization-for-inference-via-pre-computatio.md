---
layout: default
title: ROI-Reasoning: Rational Optimization for Inference via Pre-Computation Meta-Cognition
---

# ROI-Reasoning: Rational Optimization for Inference via Pre-Computation Meta-Cognition
**arXiv**：[2601.03822v1](https://arxiv.org/abs/2601.03822) · [PDF](https://arxiv.org/pdf/2601.03822.pdf)  
**作者**：Muyang Zhao, Qi Qi, Hao Sun  

**一句话要点**：提出ROI-Reasoning框架，通过元认知微调和强化学习优化大语言模型在严格计算预算下的推理决策。

**关键词**：预算推理, 元认知微调, 强化学习, 计算分配, 大语言模型优化

## 3 点简述
- 核心问题：大语言模型在推理时无法预知任务所需计算量，导致在严格全局令牌约束下效率低下。
- 方法要点：采用两阶段框架，先预测推理成本和预期效用，再通过强化学习优化序列决策。
- 实验或效果：在预算数学推理基准测试中，显著提升整体分数并减少计算不足的遗憾。

## 摘要（原文）

> Large language models (LLMs) can achieve strong reasoning performance with sufficient computation, but they do not inherently know how much computation a task requires. We study budgeted inference-time reasoning for multiple tasks under a strict global token constraint and formalize it as a Ordered Stochastic Multiple-Choice Knapsack Problem(OS-MCKP). This perspective highlights a meta-cognitive requirement -- anticipating task difficulty, estimating return over investment (ROI), and allocating computation strategically. We propose ROI-Reasoning, a two-stage framework that endows LLMs with intrinsic, budget-aware rationality. In the first stage, Meta-Cognitive Fine-Tuning teaches models to predict reasoning cost and expected utility before generation, enabling explicit solve-or-skip decisions. Next, Rationality-Aware Reinforcement Learning optimizes sequential decision making under a hard token budget, allowing models to learn long-horizon allocation strategies. Across budgeted mathematical reasoning benchmarks, ROI-Reasoning consistently improves overall score while substantially reducing regret under tight computation budgets.

