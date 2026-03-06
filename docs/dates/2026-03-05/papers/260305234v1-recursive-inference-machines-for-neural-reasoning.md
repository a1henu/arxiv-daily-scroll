---
layout: default
title: Recursive Inference Machines for Neural Reasoning
---

# Recursive Inference Machines for Neural Reasoning
**arXiv**：[2603.05234v1](https://arxiv.org/abs/2603.05234) · [PDF](https://arxiv.org/pdf/2603.05234.pdf)  
**作者**：Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, Sriraam Natarajan, Kristian Kersting  

**一句话要点**：提出递归推理机以结合神经推理与经典推理机制，提升复杂问题解决性能。

**关键词**：神经推理, 递归推理, 推理机框架, 复杂问题解决, 表格数据分类

## 3 点简述
- 核心问题：神经推理系统如TRMs需结合推理机制以处理复杂查询，但现有方法可能未充分整合经典推理引擎。
- 方法要点：引入递归推理机框架，通过递归推理机制和重加权组件扩展TRMs，增强推理能力。
- 实验或效果：在ARC-AGI和Sudoku Extreme等基准上表现更优，并在表格数据分类任务中超越TabPFNs。

## 摘要（原文）

> Neural reasoners such as Tiny Recursive Models (TRMs) solve complex problems by combining neural backbones with specialized inference schemes. Such inference schemes have been a central component of stochastic reasoning systems, where inference rules are applied to a stochastic model to derive answers to complex queries. In this work, we bridge these two paradigms by introducing Recursive Inference Machines (RIMs), a neural reasoning framework that explicitly incorporates recursive inference mechanisms inspired by classical inference engines. We show that TRMs can be expressed as an instance of RIMs, allowing us to extend them through a reweighting component, yielding better performance on challenging reasoning benchmarks, including ARC-AGI-1, ARC-AGI-2, and Sudoku Extreme. Furthermore, we show that RIMs can be used to improve reasoning on other tasks, such as the classification of tabular data, outperforming TabPFNs.

