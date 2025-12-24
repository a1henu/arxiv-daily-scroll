---
layout: default
title: Schoenfeld's Anatomy of Mathematical Reasoning by Language Models
---

# Schoenfeld's Anatomy of Mathematical Reasoning by Language Models
**arXiv**：[2512.19995v1](https://arxiv.org/abs/2512.19995) · [PDF](https://arxiv.org/pdf/2512.19995.pdf)  
**作者**：Ming Li, Chenrui Fan, Yize Cheng, Soheil Feizi, Tianyi Zhou  

**一句话要点**：提出ThinkARM框架，基于Schoenfeld理论分析语言模型在数学推理中的认知结构

**关键词**：语言模型推理分析, 数学问题解决, 认知结构抽象, ThinkARM框架, Schoenfeld理论

## 3 点简述
- 核心问题：语言模型推理痕迹难以识别，认知步骤不明确
- 方法要点：引入ThinkARM框架，将推理痕迹抽象为功能步骤如分析、探索、实施、验证
- 实验或效果：应用于数学问题解决，揭示推理动态和结构差异，探索步骤与正确性相关

## 摘要（原文）

> Large language models increasingly expose reasoning traces, yet their underlying cognitive structure and steps remain difficult to identify and analyze beyond surface-level statistics. We adopt Schoenfeld's Episode Theory as an inductive, intermediate-scale lens and introduce ThinkARM (Anatomy of Reasoning in Models), a scalable framework that explicitly abstracts reasoning traces into functional reasoning steps such as Analysis, Explore, Implement, Verify, etc. When applied to mathematical problem solving by diverse models, this abstraction reveals reproducible thinking dynamics and structural differences between reasoning and non-reasoning models, which are not apparent from token-level views. We further present two diagnostic case studies showing that exploration functions as a critical branching step associated with correctness, and that efficiency-oriented methods selectively suppress evaluative feedback steps rather than uniformly shortening responses. Together, our results demonstrate that episode-level representations make reasoning steps explicit, enabling systematic analysis of how reasoning is structured, stabilized, and altered in modern language models.

