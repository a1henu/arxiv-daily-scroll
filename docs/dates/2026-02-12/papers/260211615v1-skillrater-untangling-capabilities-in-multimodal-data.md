---
layout: default
title: SkillRater: Untangling Capabilities in Multimodal Data
---

# SkillRater: Untangling Capabilities in Multimodal Data
**arXiv**：[2602.11615v1](https://arxiv.org/abs/2602.11615) · [PDF](https://arxiv.org/pdf/2602.11615.pdf)  
**作者**：Naveen Sahi, Jeremy Dohmann, Armen Aghajanyan, Akshat Shrivastava  

**一句话要点**：提出SkillRater框架，通过多维评分解决多模态数据过滤中单一质量分数的局限性

**关键词**：多模态数据筛选, 能力分解, 元学习, 视觉语言模型, 质量评分

## 3 点简述
- 核心问题：传统数据筛选使用单一质量分数，无法同时优化模型所需的多项能力
- 方法要点：引入SkillRater，分解质量评分至多个能力维度，采用元学习训练专用评分器
- 实验或效果：在视觉语言模型中验证，提升视觉理解、OCR和STEM推理能力，评分信号近正交

## 摘要（原文）

> Data curation methods typically assign samples a single quality score. We argue this scalar framing is fundamentally limited: when training requires multiple distinct capabilities, a monolithic scorer cannot maximize useful signals for all of them simultaneously. Quality is better understood as multidimensional, with each dimension corresponding to a capability the model must acquire. We introduce SkillRater, a framework that decomposes data filtering into specialized raters - one per capability, each trained via meta-learning on a disjoint validation objective - and composes their scores through a progressive selection rule: at each training stage, a sample is retained if any rater ranks it above a threshold that tightens over time, preserving diversity early while concentrating on high-value samples late. We validate this approach on vision language models, decomposing quality into three capability dimensions: visual understanding, OCR, and STEM reasoning. At 2B parameters, SkillRater improves over unfiltered baselines by 5.63% on visual understanding, 2.00% on OCR, and 3.53% on STEM on held out benchmarks. The learned rater signals are near orthogonal, confirming that the decomposition captures genuinely independent quality dimensions and explaining why it outperforms both unfiltered training and monolithic learned filtering.

