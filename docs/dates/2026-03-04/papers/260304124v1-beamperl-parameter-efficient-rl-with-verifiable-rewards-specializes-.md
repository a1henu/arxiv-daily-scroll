---
layout: default
title: BeamPERL: Parameter-Efficient RL with Verifiable Rewards Specializes Compact LLMs for Structured Beam Mechanics Reasoning
---

# BeamPERL: Parameter-Efficient RL with Verifiable Rewards Specializes Compact LLMs for Structured Beam Mechanics Reasoning
**arXiv**：[2603.04124v1](https://arxiv.org/abs/2603.04124) · [PDF](https://arxiv.org/pdf/2603.04124.pdf)  
**作者**：Tarjei Paule Hage, Markus J. Buehler  

**一句话要点**：提出BeamPERL方法，通过参数高效强化学习与可验证奖励，训练紧凑大语言模型进行梁结构力学推理。

**关键词**：参数高效强化学习, 可验证奖励, 紧凑大语言模型, 梁结构力学推理, 物理推理泛化

## 3 点简述
- 研究问题：强化学习能否基于可验证奖励教会紧凑模型物理推理，而非仅模式匹配。
- 方法要点：使用1.5B参数模型，基于符号求解器的二元正确性奖励进行参数高效RLVR训练。
- 实验效果：最佳检查点Pass@1提升66.7%，但推理能力各向异性，泛化有限。

## 摘要（原文）

> Can reinforcement learning with hard, verifiable rewards teach a compact language model to reason about physics, or does it primarily learn to pattern-match toward correct answers? We study this question by training a 1.5B-parameter reasoning model on beam statics, a classic engineering problem, using parameter-efficient RLVR with binary correctness rewards from symbolic solvers, without teacher-generated reasoning traces. The best BeamPERL checkpoint achieves a 66.7% improvement in Pass@1 over the base model. However, the learned competence is anisotropic: the model generalizes compositionally (more loads) but fails under topological shifts (moved supports) that require the same equilibrium equations. Intermediate checkpoints yield the strongest reasoning, while continued optimization degrades robustness while maintaining reward. These findings reveal a key limitation of outcome-level alignment: reinforcement learning with exact physics rewards induces procedural solution templates rather than internalization of governing equations. The precision of the reward signal - even when analytically exact - does not by itself guarantee transferable physical reasoning. Our results suggest that verifiable rewards may need to be paired with structured reasoning scaffolding to move beyond template matching toward robust scientific reasoning.

