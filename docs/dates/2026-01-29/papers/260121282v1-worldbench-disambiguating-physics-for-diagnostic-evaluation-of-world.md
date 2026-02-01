---
layout: default
title: WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models
---

# WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models
**arXiv**：[2601.21282v1](https://arxiv.org/abs/2601.21282) · [PDF](https://arxiv.org/pdf/2601.21282.pdf)  
**作者**：Rishi Upadhyay, Howard Zhang, Jim Solomon, Ayush Agrawal, Pranay Boreddy, Shruti Satya Narayana, Yunhao Ba, Alex Wong, Celso M de Melo, Achuta Kadambi  

**一句话要点**：提出WorldBench以解决世界模型物理评估中的概念纠缠问题

**关键词**：世界模型评估, 物理推理基准, 视频生成, 概念解耦, 物理一致性

## 3 点简述
- 现有视频基准在物理评估中存在概念纠缠，限制诊断能力
- WorldBench通过概念解耦设计，支持单物理概念或定律的隔离评估
- 实验显示当前世界模型在特定物理概念上存在一致性不足

## 摘要（原文）

> Recent advances in generative foundational models, often termed "world models," have propelled interest in applying them to critical tasks like robotic planning and autonomous system training. For reliable deployment, these models must exhibit high physical fidelity, accurately simulating real-world dynamics. Existing physics-based video benchmarks, however, suffer from entanglement, where a single test simultaneously evaluates multiple physical laws and concepts, fundamentally limiting their diagnostic capability. We introduce WorldBench, a novel video-based benchmark specifically designed for concept-specific, disentangled evaluation, allowing us to rigorously isolate and assess understanding of a single physical concept or law at a time. To make WorldBench comprehensive, we design benchmarks at two different levels: 1) an evaluation of intuitive physical understanding with concepts such as object permanence or scale/perspective, and 2) an evaluation of low-level physical constants and material properties such as friction coefficients or fluid viscosity. When SOTA video-based world models are evaluated on WorldBench, we find specific patterns of failure in particular physics concepts, with all tested models lacking the physical consistency required to generate reliable real-world interactions. Through its concept-specific evaluation, WorldBench offers a more nuanced and scalable framework for rigorously evaluating the physical reasoning capabilities of video generation and world models, paving the way for more robust and generalizable world-model-driven learning.

