---
layout: default
title: Neural-Inspired Posterior Approximation (NIPA)
---

# Neural-Inspired Posterior Approximation (NIPA)
**arXiv**：[2601.22539v1](https://arxiv.org/abs/2601.22539) · [PDF](https://arxiv.org/pdf/2601.22539.pdf)  
**作者**：Babak Shahbaba, Zahra Moslemi  

**一句话要点**：提出NIPA算法，结合模型化、无模型和记忆模块，实现可扩展贝叶斯推断。

**关键词**：贝叶斯推断, 采样算法, 深度学习, 不确定性量化, 神经启发

## 3 点简述
- 核心问题：生物高效学习机制如何转化为可扩展贝叶斯推断算法。
- 方法要点：集成模型化模块进行引导采样、无模型模块快速采样、记忆模块回忆采样。
- 实验或效果：应用于贝叶斯深度学习，提升不确定性量化能力。

## 摘要（原文）

> Humans learn efficiently from their environment by engaging multiple interacting neural systems that support distinct yet complementary forms of control, including model-based (goal-directed) planning, model-free (habitual) responding, and episodic memory-based learning. Model-based mechanisms compute prospective action values using an internal model of the environment, supporting flexible but computationally costly planning; model-free mechanisms cache value estimates and build heuristics that enable fast, efficient habitual responding; and memory-based mechanisms allow rapid adaptation from individual experience. In this work, we aim to elucidate the computational principles underlying this biological efficiency and translate them into a sampling algorithm for scalable Bayesian inference through effective exploration of the posterior distribution. More specifically, our proposed algorithm comprises three components: a model-based module that uses the target distribution for guided but computationally slow sampling; a model-free module that uses previous samples to learn patterns in the parameter space, enabling fast, reflexive sampling without directly evaluating the expensive target distribution; and an episodic-control module that supports rapid sampling by recalling specific past events (i.e., samples). We show that this approach advances Bayesian methods and facilitates their application to large-scale statistical machine learning problems. In particular, we apply our proposed framework to Bayesian deep learning, with an emphasis on proper and principled uncertainty quantification.

