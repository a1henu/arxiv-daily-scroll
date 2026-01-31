---
layout: default
title: Meta Context Engineering via Agentic Skill Evolution
---

# Meta Context Engineering via Agentic Skill Evolution
**arXiv**：[2601.21557v1](https://arxiv.org/abs/2601.21557) · [PDF](https://arxiv.org/pdf/2601.21557.pdf)  
**作者**：Haoran Ye, Xuning He, Vincent Arak, Haonan Dong, Guojie Song  

**一句话要点**：提出元上下文工程框架，通过智能体技能协同进化优化大语言模型推理上下文。

**关键词**：元上下文工程, 智能体技能进化, 上下文优化, 大语言模型推理, 双层框架

## 3 点简述
- 核心问题：现有上下文工程方法依赖人工设计，存在结构偏见和设计空间受限。
- 方法要点：引入双层框架，元级智能体进化工程技能，基础级智能体执行技能优化上下文。
- 实验或效果：在五个领域评估，性能相对提升5.6-53.8%，上下文适应性、可迁移性和效率更优。

## 摘要（原文）

> The operational efficacy of large language models relies heavily on their inference-time context. This has established Context Engineering (CE) as a formal discipline for optimizing these inputs. Current CE methods rely on manually crafted harnesses, such as rigid generation-reflection workflows and predefined context schemas. They impose structural biases and restrict context optimization to a narrow, intuition-bound design space. To address this, we introduce Meta Context Engineering (MCE), a bi-level framework that supersedes static CE heuristics by co-evolving CE skills and context artifacts. In MCE iterations, a meta-level agent refines engineering skills via agentic crossover, a deliberative search over the history of skills, their executions, and evaluations. A base-level agent executes these skills, learns from training rollouts, and optimizes context as flexible files and code. We evaluate MCE across five disparate domains under offline and online settings. MCE demonstrates consistent performance gains, achieving 5.6--53.8% relative improvement over state-of-the-art agentic CE methods (mean of 16.9%), while maintaining superior context adaptability, transferability, and efficiency in both context usage and training.

