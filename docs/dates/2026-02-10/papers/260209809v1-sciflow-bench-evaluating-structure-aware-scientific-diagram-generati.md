---
layout: default
title: SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing
---

# SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing
**arXiv**：[2602.09809v1](https://arxiv.org/abs/2602.09809) · [PDF](https://arxiv.org/pdf/2602.09809.pdf)  
**作者**：Tong Zhang, Honglin Lin, Zhou Liu, Chong Chen, Wentao Zhang  

**一句话要点**：提出SciFlow-Bench基准，通过逆解析评估结构感知的科学图表生成

**关键词**：科学图表生成, 结构感知评估, 逆解析基准, 像素级生成, 多智能体系统

## 3 点简述
- 核心问题：现有基准对科学图表的结构正确性评估不足，模型常生成视觉合理但结构错误的图表
- 方法要点：基于真实PDF构建基准，采用闭环逆解析协议，将生成图像解析为结构化图进行对比
- 实验或效果：实验表明复杂拓扑图表的生成仍具挑战，突显结构感知评估的必要性

## 摘要（原文）

> Scientific diagrams convey explicit structural information, yet modern text-to-image models often produce visually plausible but structurally incorrect results. Existing benchmarks either rely on image-centric or subjective metrics insensitive to structure, or evaluate intermediate symbolic representations rather than final rendered images, leaving pixel-based diagram generation underexplored. We introduce SciFlow-Bench, a structure-first benchmark for evaluating scientific diagram generation directly from pixel-level outputs. Built from real scientific PDFs, SciFlow-Bench pairs each source framework figure with a canonical ground-truth graph and evaluates models as black-box image generators under a closed-loop, round-trip protocol that inverse-parses generated diagram images back into structured graphs for comparison. This design enforces evaluation by structural recoverability rather than visual similarity alone, and is enabled by a hierarchical multi-agent system that coordinates planning, perception, and structural reasoning. Experiments show that preserving structural correctness remains a fundamental challenge, particularly for diagrams with complex topology, underscoring the need for structure-aware evaluation.

