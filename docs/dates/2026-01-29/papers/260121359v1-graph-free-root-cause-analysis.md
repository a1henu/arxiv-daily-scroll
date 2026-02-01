---
layout: default
title: Graph-Free Root Cause Analysis
---

# Graph-Free Root Cause Analysis
**arXiv**：[2601.21359v1](https://arxiv.org/abs/2601.21359) · [PDF](https://arxiv.org/pdf/2601.21359.pdf)  
**作者**：Luan Pham  

**一句话要点**：提出PRISM框架，在无依赖图场景下实现高效根因分析，解决故障传播导致的误判问题。

**关键词**：根因分析, 无依赖图, 故障传播, 系统诊断, 高效算法, 理论保证

## 3 点简述
- 核心问题：现有无依赖图根因分析方法假设根因异常分数最高，但故障传播时下游异常可能更大，导致误判。
- 方法要点：PRISM为无依赖图系统设计，基于组件模型提供理论保证，通过简单高效算法识别根因。
- 实验或效果：在9个真实数据集735次故障上，Top-1准确率达68%，比最佳基线提升258%，每次诊断仅需8ms。

## 摘要（原文）

> Failures in complex systems demand rapid Root Cause Analysis (RCA) to prevent cascading damage. Existing RCA methods that operate without dependency graph typically assume that the root cause having the highest anomaly score. This assumption fails when faults propagate, as a small delay at the root cause can accumulate into a much larger anomaly downstream. In this paper, we propose PRISM, a simple and efficient framework for RCA when the dependency graph is absent. We formulate a class of component-based systems under which PRISM performs RCA with theoretical guarantees. On 735 failures across 9 real-world datasets, PRISM achieves 68% Top-1 accuracy, a 258% improvement over the best baseline, while requiring only 8ms per diagnosis.

