---
layout: default
title: Mixture-of-Models: Unifying Heterogeneous Agents via N-Way Self-Evaluating Deliberation
---

# Mixture-of-Models: Unifying Heterogeneous Agents via N-Way Self-Evaluating Deliberation
**arXiv**：[2601.16863v1](https://arxiv.org/abs/2601.16863) · [PDF](https://arxiv.org/pdf/2601.16863.pdf)  
**作者**：Tims Pecerskis, Aivars Smirnovs  

**一句话要点**：提出N向自评估审议协议，通过运行时模型混合架构统一异构智能体以提升效率与安全性

**关键词**：模型混合架构, 动态专家选择, 运行时优化, 异构智能体集成, 安全对齐, 资源效率优化

## 3 点简述
- 核心问题：传统专家混合模型依赖静态门控网络，难以动态优化异构模型组合与资源约束
- 方法要点：引入动态专家代理器，将模型选择建模为背包问题变体，并采用宏观循环神经网络实现迭代精化
- 实验效果：在多个基准测试中，小规模模型组合可媲美或超越百亿参数模型，且安全评估显示对齐属性提升

## 摘要（原文）

> This paper introduces the N-Way Self-Evaluating Deliberation (NSED) protocol, a Runtime Mixture-of-Models (MoM) architecture that constructs emergent composite models from a plurality of distinct expert agents. Unlike traditional Mixture-of-Experts (MoE) which rely on static gating networks, NSED employs a Dynamic Expertise Broker - a runtime optimization engine that treats model selection as a variation of the Knapsack Problem, binding heterogeneous checkpoints to functional roles based on live telemetry and cost constraints. At the execution layer, we formalize deliberation as a Macro-Scale Recurrent Neural Network (RNN), where the consensus state loops back through a semantic forget gate to enable iterative refinement without proportional VRAM scaling. Key components include an orchestration fabric for trustless N-to-N peer review, a Quadratic Voting activation function for non-linear consensus, and a feedback-driven state update. Empirical validation on challenging benchmarks (AIME 2025, LiveCodeBench) demonstrates that this topology allows ensembles of small (less than 20B) consumer-grade models to match or exceed the performance of state-of-the-art 100B+ parameter models, establishing a new hardware arbitrage efficiency frontier. Furthermore, testing on the DarkBench safety suite reveals intrinsic alignment properties, with peer-mediated correction reducing sycophancy scores below that of any individual agent.

