---
layout: default
title: GeoLoom: High-quality Geometric Diagram Generation from Textual Input
---

# GeoLoom: High-quality Geometric Diagram Generation from Textual Input
**arXiv**：[2512.08180v1](https://arxiv.org/abs/2512.08180) · [PDF](https://arxiv.org/pdf/2512.08180.pdf)  
**作者**：Xiaojing Wei, Ting Zhang, Wei He, Jingdong Wang, Hua Huang  

**一句话要点**：提出GeoLoom框架，通过形式化语言和坐标求解实现文本到高质量几何图生成。

**关键词**：几何图生成, 文本到图生成, 形式化语言, 坐标求解, 蒙特卡洛优化, 结构保真度

## 3 点简述
- 核心问题：几何图生成需高空间精度，现有方法难以保证结构保真度。
- 方法要点：结合自动形式化模块和蒙特卡洛优化求解器，将自然语言转换为形式约束并映射为坐标。
- 实验或效果：在GeoNF数据集上评估，结构保真度显著优于基线，支持可解释和可扩展生成。

## 摘要（原文）

> High-quality geometric diagram generation presents both a challenge and an opportunity: it demands strict spatial accuracy while offering well-defined constraints to guide generation. Inspired by recent advances in geometry problem solving that employ formal languages and symbolic solvers for enhanced correctness and interpretability, we propose GeoLoom, a novel framework for text-to-diagram generation in geometric domains. GeoLoom comprises two core components: an autoformalization module that translates natural language into a specifically designed generation-oriented formal language GeoLingua, and a coordinate solver that maps formal constraints to precise coordinates using the efficient Monte Carlo optimization. To support this framework, we introduce GeoNF, a dataset aligning natural language geometric descriptions with formal GeoLingua descriptions. We further propose a constraint-based evaluation metric that quantifies structural deviation, offering mathematically grounded supervision for iterative refinement. Empirical results demonstrate that GeoLoom significantly outperforms state-of-the-art baselines in structural fidelity, providing a principled foundation for interpretable and scalable diagram generation.

