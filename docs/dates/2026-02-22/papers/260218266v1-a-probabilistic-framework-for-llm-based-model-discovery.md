---
layout: default
title: A Probabilistic Framework for LLM-Based Model Discovery
---

# A Probabilistic Framework for LLM-Based Model Discovery
**arXiv**：[2602.18266v1](https://arxiv.org/abs/2602.18266) · [PDF](https://arxiv.org/pdf/2602.18266.pdf)  
**作者**：Stefan Wahl, Raphaela Schenk, Ali Farnoud, Jakob H. Macke, Daniel Gedon  

**一句话要点**：提出基于概率推理的LLM模型发现框架ModelSMC，以提升科学模型发现的系统性和解释性。

**关键词**：模型发现, 概率推理, 序贯蒙特卡洛, LLM应用, 科学模拟

## 3 点简述
- 核心问题：现有LLM模型发现方法依赖启发式流程，缺乏统一概率框架。
- 方法要点：将模型发现重构为概率推理，引入基于序贯蒙特卡洛采样的ModelSMC算法。
- 实验或效果：在真实科学系统上验证，发现模型机制更可解释，后验预测检查改善。

## 摘要（原文）

> Automated methods for discovering mechanistic simulator models from observational data offer a promising path toward accelerating scientific progress. Such methods often take the form of agentic-style iterative workflows that repeatedly propose and revise candidate models by imitating human discovery processes. However, existing LLM-based approaches typically implement such workflows via hand-crafted heuristic procedures, without an explicit probabilistic formulation. We recast model discovery as probabilistic inference, i.e., as sampling from an unknown distribution over mechanistic models capable of explaining the data. This perspective provides a unified way to reason about model proposal, refinement, and selection within a single inference framework. As a concrete instantiation of this view, we introduce ModelSMC, an algorithm based on Sequential Monte Carlo sampling. ModelSMC represents candidate models as particles which are iteratively proposed and refined by an LLM, and weighted using likelihood-based criteria. Experiments on real-world scientific systems illustrate that this formulation discovers models with interpretable mechanisms and improves posterior predictive checks. More broadly, this perspective provides a probabilistic lens for understanding and developing LLM-based approaches to model discovery.

