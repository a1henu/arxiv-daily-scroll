---
layout: default
title: Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning
---

# Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning
**arXiv**：[2602.06475v1](https://arxiv.org/abs/2602.06475) · [PDF](https://arxiv.org/pdf/2602.06475.pdf)  
**作者**：Jingyao Wang, Peizheng Guo, Wenwen Qiang, Jiahuan Zhou, Huijie Guo, Changwen Zheng, Hui Xiong  

**一句话要点**：提出群组因果反事实策略优化，以提升大语言模型推理的泛化能力。

**关键词**：大语言模型推理, 因果反事实学习, 策略优化, 泛化能力, 奖励机制设计

## 3 点简述
- 核心问题：现有奖励机制过度依赖最终答案正确性，忽略推理过程质量，影响泛化。
- 方法要点：基于因果视角设计反事实奖励，联合评估推理步骤的鲁棒性和有效性。
- 实验或效果：在多样化基准测试中验证了方法在提升推理泛化方面的优势。

## 摘要（原文）

> Large language models (LLMs) excel at complex tasks with advances in reasoning capabilities. However, existing reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization. From a causal perspective, we interpret multi-candidate reasoning for a fixed question as a family of counterfactual experiments with theoretical supports. Building on this, we propose Group Causal Counterfactual Policy Optimization to explicitly train LLMs to learn generalizable reasoning patterns. It proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions. We then construct token-level advantages from this reward and optimize the policy, encouraging LLMs to favor reasoning patterns that are process-valid and counterfactually robust. Extensive experiments on diverse benchmarks demonstrate its advantages.

