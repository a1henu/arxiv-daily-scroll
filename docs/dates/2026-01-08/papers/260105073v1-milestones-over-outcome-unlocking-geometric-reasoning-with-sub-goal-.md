---
layout: default
title: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward
---

# Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward
**arXiv**：[2601.05073v1](https://arxiv.org/abs/2601.05073) · [PDF](https://arxiv.org/pdf/2601.05073.pdf)  
**作者**：Jianlong Chen, Daocheng Fu, Shengze Xu, Jiawei Chen, Yuan Feng, Yue Yang, Junchi Yan, Hongyuan Zha, Renqiu Xia  

**一句话要点**：提出子目标可验证奖励框架以解决多模态大语言模型几何推理难题

**关键词**：几何推理, 子目标验证, 多模态大语言模型, 密集奖励, 形式验证, 泛化能力

## 3 点简述
- 核心问题：基于结果的监督无法区分几何推理中的猜测与严谨推导，导致模型性能受限。
- 方法要点：构建GeoGoal基准，通过形式验证数据引擎将抽象证明转换为可验证数值子目标，并基于骨架率设计密集奖励。
- 实验或效果：SGVR提升几何性能9.7%，并泛化至一般数学和其他推理任务，分别提升8.0%和2.8%。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) struggle with complex geometric reasoning, largely because "black box" outcome-based supervision fails to distinguish between lucky guesses and rigorous deduction. To address this, we introduce a paradigm shift towards subgoal-level evaluation and learning. We first construct GeoGoal, a benchmark synthesized via a rigorous formal verification data engine, which converts abstract proofs into verifiable numeric subgoals. This structure reveals a critical divergence between reasoning quality and outcome accuracy. Leveraging this, we propose the Sub-Goal Verifiable Reward (SGVR) framework, which replaces sparse signals with dense rewards based on the Skeleton Rate. Experiments demonstrate that SGVR not only enhances geometric performance (+9.7%) but also exhibits strong generalization, transferring gains to general math (+8.0%) and other general reasoning tasks (+2.8%), demonstrating broad applicability across diverse domains.

