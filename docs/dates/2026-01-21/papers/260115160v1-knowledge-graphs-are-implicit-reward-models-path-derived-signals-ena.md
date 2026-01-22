---
layout: default
title: Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning
---

# Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning
**arXiv**：[2601.15160v1](https://arxiv.org/abs/2601.15160) · [PDF](https://arxiv.org/pdf/2601.15160.pdf)  
**作者**：Yuval Kansal, Niraj K. Jha  

**一句话要点**：提出基于知识图谱路径的隐式奖励模型，以提升大语言模型在科学领域的组合推理能力。

**关键词**：知识图谱, 组合推理, 强化学习, 后训练, 医学领域, 隐式奖励模型

## 3 点简述
- 大语言模型在科学领域组合推理能力有限，需解决多跳推理问题。
- 通过知识图谱路径生成奖励信号，结合监督微调和强化学习进行后训练。
- 在医学领域验证，模型在复杂任务上超越更大模型和前沿系统。

## 摘要（原文）

> Large language models have achieved near-expert performance in structured reasoning domains like mathematics and programming, yet their ability to perform compositional multi-hop reasoning in specialized scientific fields remains limited. We propose a bottom-up learning paradigm in which models are grounded in axiomatic domain facts and compose them to solve complex, unseen tasks. To this end, we present a post-training pipeline, based on a combination of supervised fine-tuning and reinforcement learning (RL), in which knowledge graphs act as implicit reward models. By deriving novel reward signals from knowledge graph paths, we provide verifiable, scalable, and grounded supervision that encourages models to compose intermediate axioms rather than optimize only final answers during RL. We validate this approach in the medical domain, training a 14B model on short-hop reasoning paths (1-3 hops) and evaluating its zero-shot generalization to complex multi-hop queries (4-5 hops). Our experiments show that path-derived rewards act as a "compositional bridge", enabling our model to significantly outperform much larger models and frontier systems like GPT-5.2 and Gemini 3 Pro, on the most difficult reasoning tasks. Furthermore, we demonstrate the robustness of our approach to adversarial perturbations against option-shuffling stress tests. This work suggests that grounding the reasoning process in structured knowledge is a scalable and efficient path toward intelligent reasoning.

