---
layout: default
title: SpatialBench: Can Agents Analyze Real-World Spatial Biology Data?
---

# SpatialBench: Can Agents Analyze Real-World Spatial Biology Data?
**arXiv**：[2512.21907v1](https://arxiv.org/abs/2512.21907) · [PDF](https://arxiv.org/pdf/2512.21907.pdf)  
**作者**：Kenny Workman, Zhen Yang, Harihara Muralidharan, Hannah Le  

**一句话要点**：提出SpatialBench基准以评估AI代理分析真实世界空间生物学数据的能力

**关键词**：空间转录组学, AI代理评估, 基准测试, 生物学数据分析, 模型性能诊断

## 3 点简述
- 核心问题：AI代理能否从复杂真实空间数据中提取生物学见解尚不明确
- 方法要点：构建包含146个可验证问题的基准，覆盖五种空间技术和七类任务
- 实验或效果：前沿模型准确率低（20-38%），性能受模型-任务和模型-平台交互影响

## 摘要（原文）

> Spatial transcriptomics assays are rapidly increasing in scale and complexity, making computational analysis a major bottleneck in biological discovery. Although frontier AI agents have improved dramatically at software engineering and general data analysis, it remains unclear whether they can extract biological insight from messy, real-world spatial datasets. We introduce SpatialBench, a benchmark of 146 verifiable problems derived from practical spatial analysis workflows spanning five spatial technologies and seven task categories. Each problem provides a snapshot of experimental data immediately prior to an analysis step and a deterministic grader that evaluates recovery of a key biological result. Benchmark data on frontier models shows that base model accuracy remains low (20-38% across model families), with strong model-task and model-platform interactions. Harness design has a large empirical effect on performance, indicating that tools, prompts, control flow, and execution environment should be evaluated and improved as first-class objects. SpatialBench serves both as a measurement tool and a diagnostic lens for developing agents that can interact with real spatial datasets faithfully, transparently, and reproducibly.

