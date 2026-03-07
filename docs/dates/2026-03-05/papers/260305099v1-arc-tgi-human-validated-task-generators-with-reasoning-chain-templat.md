---
layout: default
title: ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI
---

# ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI
**arXiv**：[2603.05099v1](https://arxiv.org/abs/2603.05099) · [PDF](https://arxiv.org/pdf/2603.05099.pdf)  
**作者**：Jens Lehmann, Syeda Khushbakht, Nikoo Salehfard, Nur A Zarin Nishat, Dhananjay Bhandiwad, Andrei Aioanei, Sahar Vahdati  

**一句话要点**：提出ARC-TGI框架，通过任务生成器解决ARC-AGI基准测试中的过拟合和数据集泄露问题。

**关键词**：任务生成器, 抽象推理, 基准测试, 数据集采样, 人类验证, 规则归纳

## 3 点简述
- 核心问题：ARC-AGI基准测试因静态谜题集导致过拟合、数据集泄露和记忆化，难以衡量进展。
- 方法要点：开发开源任务生成器框架，生成多样任务并保持潜在规则，支持任务级约束和人类验证。
- 实验或效果：发布461个生成器覆盖多个任务集，支持可扩展数据集采样和受控基准测试。

## 摘要（原文）

> The Abstraction and Reasoning Corpus (ARC-AGI) probes few-shot abstraction and rule induction on small visual grids, but progress is difficult to measure on static collections of hand-authored puzzles due to overfitting, dataset leakage, and memorisation. We introduce ARC-TGI (ARC Task Generators Inventory), an open-source framework for task-family generators: compact Python programs that sample diverse ARC-AGI tasks while preserving a latent rule. ARC-TGI is built around a solver-facing representation: each generated task is paired with natural-language input and transformation reasoning chains and partially evaluated Python code implementing sampling, transformation, and episode construction. Crucially, ARC-TGI supports task-level constraints so that training examples collectively expose the variations needed to infer the underlying rule, a requirement for human-solvable ARC tasks that independent per-example sampling often fails to guarantee. All generators undergo human refinement and local verification to keep both grids and reasoning traces natural and consistent under variation. We release 461 generators covering 180 ARC-Mini tasks, 215 ARC-AGI-1 tasks (200 train, 15 test), and 66 ARC-AGI-2 tasks (55 train, 11 test), enabling scalable dataset sampling and controlled benchmarking.

