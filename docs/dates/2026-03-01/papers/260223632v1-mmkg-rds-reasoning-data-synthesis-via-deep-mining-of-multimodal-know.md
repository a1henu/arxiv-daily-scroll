---
layout: default
title: MMKG-RDS: Reasoning Data Synthesis via Deep Mining of Multimodal Knowledge Graphs
---

# MMKG-RDS: Reasoning Data Synthesis via Deep Mining of Multimodal Knowledge Graphs
**arXiv**：[2602.23632v1](https://arxiv.org/abs/2602.23632) · [PDF](https://arxiv.org/pdf/2602.23632.pdf)  
**作者**：Lun Zhan, Feng Xiong, Huanyong Liu, Feng Zhang, Yuhui Yin  

**一句话要点**：提出MMKG-RDS框架，通过多模态知识图谱合成推理数据以提升领域模型能力。

**关键词**：多模态知识图谱, 推理数据合成, 细粒度知识提取, 数据质量评估, 模型微调, 基准数据集

## 3 点简述
- 现有方法在长尾知识覆盖、验证和可解释性方面存在不足，知识图谱方法在功能、粒度、可定制性和评估上仍有局限。
- MMKG-RDS支持细粒度知识提取、可定制路径采样和多维数据质量评分，基于MMKG-RDS-Bench数据集验证。
- 实验显示，在少量合成数据上微调Qwen3模型，推理准确率提升9.2%，并生成挑战性数据用于复杂基准构建。

## 摘要（原文）

> Synthesizing high-quality training data is crucial for enhancing domain models' reasoning abilities. Existing methods face limitations in long-tail knowledge coverage, effectiveness verification, and interpretability. Knowledge-graph-based approaches still fall short in functionality, granularity, customizability, and evaluation. To address these issues, we propose MMKG-RDS, a flexible framework for reasoning data synthesis that leverages multimodal knowledge graphs. It supports fine-grained knowledge extraction, customizable path sampling, and multidimensional data quality scoring. We validate MMKG-RDS with the MMKG-RDS-Bench dataset, covering five domains, 17 task types, and 14,950 samples. Experimental results show fine-tuning Qwen3 models (0.6B/8B/32B) on a small number of synthesized samples improves reasoning accuracy by 9.2%. The framework also generates distinct data, challenging existing models on tasks involving tables and formulas, useful for complex benchmark construction. The dataset and code are available at https://github.com/360AILAB-NLP/MMKG-RDS

