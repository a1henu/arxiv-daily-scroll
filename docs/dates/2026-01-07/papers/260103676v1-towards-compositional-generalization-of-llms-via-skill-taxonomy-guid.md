---
layout: default
title: Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis
---

# Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis
**arXiv**：[2601.03676v1](https://arxiv.org/abs/2601.03676) · [PDF](https://arxiv.org/pdf/2601.03676.pdf)  
**作者**：Yifan Wei, Li Du, Xiaoyan Yu, Yang Feng, Angsheng Li  

**一句话要点**：提出STEPS框架以解决LLMs组合泛化中的数据瓶颈问题

**关键词**：组合泛化, 数据合成, 技能分类学, 结构信息理论, 指令跟随, 代理系统

## 3 点简述
- 核心问题：LLMs因复杂技能组合的长尾分布导致组合泛化能力受限
- 方法要点：基于技能分类学，通过最大化结构信息合成组合挑战性数据
- 实验或效果：在指令跟随基准测试中优于现有基线，提升下游代理任务泛化

## 摘要（原文）

> Large Language Models (LLMs) and agent-based systems often struggle with compositional generalization due to a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution, limiting both instruction-following performance and generalization in agent-centric tasks. To address this challenge, we propose STEPS, a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data. STEPS explicitly targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. Building on this taxonomy, we formulate data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence. Experiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.

