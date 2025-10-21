---
layout: default
title: High-Level Multi-Robot Trajectory Planning And Spurious Behavior Detection
---

# High-Level Multi-Robot Trajectory Planning And Spurious Behavior Detection
**arXiv**：[2510.17261v1](https://arxiv.org/abs/2510.17261) · [PDF](https://arxiv.org/pdf/2510.17261.pdf)  
**作者**：Fernando Salanova, Jesús Roche, Cristian Mahuela, Eduardo Montijano  

**一句话要点**：提出基于NWN和Transformer的框架以检测多机器人系统中的虚假行为

**关键词**：多机器人系统, 轨迹规划, 虚假行为检测, 线性时序逻辑, Transformer模型, 异常检测

## 3 点简述
- 核心问题：多机器人系统中LTL计划执行时的虚假行为检测，如任务序列错误和约束违反。
- 方法要点：使用Nets-within-Nets框架协调机器人动作，并采用Transformer进行异常分类。
- 实验或效果：实验显示高准确率，虚假行为检测达91.3%，核心任务违反检测为88.3%。

## 摘要（原文）

> The reliable execution of high-level missions in multi-robot systems with
> heterogeneous agents, requires robust methods for detecting spurious behaviors.
> In this paper, we address the challenge of identifying spurious executions of
> plans specified as a Linear Temporal Logic (LTL) formula, as incorrect task
> sequences, violations of spatial constraints, timing inconsis- tencies, or
> deviations from intended mission semantics. To tackle this, we introduce a
> structured data generation framework based on the Nets-within-Nets (NWN)
> paradigm, which coordinates robot actions with LTL-derived global mission
> specifications. We further propose a Transformer-based anomaly detection
> pipeline that classifies robot trajectories as normal or anomalous. Experi-
> mental evaluations show that our method achieves high accuracy (91.3%) in
> identifying execution inefficiencies, and demonstrates robust detection
> capabilities for core mission violations (88.3%) and constraint-based adaptive
> anomalies (66.8%). An ablation experiment of the embedding and architecture was
> carried out, obtaining successful results where our novel proposition performs
> better than simpler representations.

