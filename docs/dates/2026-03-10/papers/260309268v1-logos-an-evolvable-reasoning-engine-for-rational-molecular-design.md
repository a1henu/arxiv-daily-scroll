---
layout: default
title: Logos: An evolvable reasoning engine for rational molecular design
---

# Logos: An evolvable reasoning engine for rational molecular design
**arXiv**：[2603.09268v1](https://arxiv.org/abs/2603.09268) · [PDF](https://arxiv.org/pdf/2603.09268.pdf)  
**作者**：Haibin Wen, Zhe Zhao, Fanfu Wang, Tianyi Xu, Hao Zhang, Chao Yang, Ye Wei  

**一句话要点**：提出Logos紧凑分子推理模型，整合多步逻辑推理与严格化学一致性，以解决分子设计中可靠性与可解释性问题。

**关键词**：分子推理模型, 逻辑推理整合, 化学一致性, 分阶段训练, 可解释AI, 分子设计优化

## 3 点简述
- 核心问题：现有AI模型在分子设计中常缺乏透明推理或化学有效性保证，限制科学工作流可靠性。
- 方法要点：采用分阶段训练策略，先学习推理示例，再对齐推理模式与分子表示，最后融入化学规则优化。
- 实验或效果：在基准数据集上表现优异，结构准确性与化学有效性均强，支持多约束优化和人类可检查推理步骤。

## 摘要（原文）

> The discovery and design of functional molecules remain central challenges across chemistry,biology, and materials science. While recent advances in machine learning have accelerated molecular property prediction and candidate generation, existing models tend to excel either in physical fidelity without transparent reasoning, or in flexible reasoning without guarantees of chemical validity. This imbalance limits the reliability of artificial intelligence systems in real scientific design workflows.Here we present Logos, a compact molecular reasoning model that integrates multi-step logical reasoning with strict chemical consistency. Logos is trained using a staged strategy that first exposes the model to explicit reasoning examples linking molecular descriptions to structural decisions, and then progressively aligns these reasoning patterns with molecular representations. In a final training phase, chemical rules and invariants are incorporated directly into the optimization objective, guiding the model toward chemically valid outputs. Across multiple benchmark datasets, Logos achieves strong performance in both structural accuracy and chemical validity, matching or surpassing substantially larger general-purpose language models while operating with a fraction of their parameters. Beyond benchmark evaluation, the model exhibits stable behaviour in molecular optimization tasks involving multiple, potentially conflicting constraints. By explicitly exposing intermediate reasoning steps, Logos enables human inspection and assessment of the design logic underlying each generated structure. These results indicate that jointly optimizing for reasoning structure and physical consistency offers a practical pathway toward reliable and interpretable AI systems for molecular science, supporting closer integration of artificial intelligence into scientific discovery processes.

