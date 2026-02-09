---
layout: default
title: FloorplanVLM: A Vision-Language Model for Floorplan Vectorization
---

# FloorplanVLM: A Vision-Language Model for Floorplan Vectorization
**arXiv**：[2602.06507v1](https://arxiv.org/abs/2602.06507) · [PDF](https://arxiv.org/pdf/2602.06507.pdf)  
**作者**：Yuanqing Liu, Ziming Yang, Yulong Li, Yue Yang  

**一句话要点**：提出FloorplanVLM，通过图像到序列建模解决栅格平面图向量化难题

**关键词**：平面图向量化, 视觉语言模型, 序列建模, 几何约束, 数据集构建, 基准测试

## 3 点简述
- 核心问题：栅格平面图向量化因复杂拓扑和几何约束而困难，传统方法易产生碎片化结果
- 方法要点：采用统一框架，将向量化重构为图像条件序列建模，直接输出结构化JSON序列
- 实验或效果：在FPBench-2K基准上，外部墙IoU达92.52%，展现优异结构有效性和泛化能力

## 摘要（原文）

> Converting raster floorplans into engineering-grade vector graphics is challenging due to complex topology and strict geometric constraints. To address this, we present FloorplanVLM, a unified framework that reformulates floorplan vectorization as an image-conditioned sequence modeling task. Unlike pixel-based methods that rely on fragile heuristics or query-based transformers that generate fragmented rooms, our model directly outputs structured JSON sequences representing the global topology. This 'pixels-to-sequence' paradigm enables the precise and holistic constraint satisfaction of complex geometries, such as slanted walls and curved arcs. To support this data-hungry approach, we introduce a scalable data engine: we construct a large-scale dataset (Floorplan-2M) and a high-fidelity subset (Floorplan-HQ-300K) to balance geometric diversity and pixel-level precision. We then employ a progressive training strategy, using Supervised Fine-Tuning (SFT) for structural grounding and quality annealing, followed by Group Relative Policy Optimization (GRPO) for strict geometric alignment. To standardize evaluation on complex layouts, we establish and open-source FPBench-2K. Evaluated on this rigorous benchmark, FloorplanVLM demonstrates exceptional structural validity, achieving $\textbf{92.52%}$ external-wall IoU and robust generalization across non-Manhattan architectures.

