---
layout: default
title: More Images, More Problems? A Controlled Analysis of VLM Failure Modes
---

# More Images, More Problems? A Controlled Analysis of VLM Failure Modes
**arXiv**：[2601.07812v1](https://arxiv.org/abs/2601.07812) · [PDF](https://arxiv.org/pdf/2601.07812.pdf)  
**作者**：Anurag Das, Adrian Bulat, Alberto Baldrati, Ioannis Maniadis Metaxas, Bernt Schiele, Georgios Tzimiropoulos, Brais Martinez  

**一句话要点**：提出MIMIC基准与数据优化方法，以解决大视觉语言模型在多图像理解中的信息聚合问题。

**关键词**：多图像理解, 视觉语言模型, 基准评估, 数据生成, 注意力机制, 信息聚合

## 3 点简述
- 核心问题：大视觉语言模型在多图像场景下存在信息聚合和概念跟踪的普遍失败。
- 方法要点：通过MIMIC基准进行诊断，并引入数据生成策略和注意力掩码方案进行优化。
- 实验或效果：实验显著提升跨图像聚合能力，并在多图像基准上超越先前最佳性能。

## 摘要（原文）

> Large Vision Language Models (LVLMs) have demonstrated remarkable capabilities, yet their proficiency in understanding and reasoning over multiple images remains largely unexplored. While existing benchmarks have initiated the evaluation of multi-image models, a comprehensive analysis of their core weaknesses and their causes is still lacking. In this work, we introduce MIMIC (Multi-Image Model Insights and Challenges), a new benchmark designed to rigorously evaluate the multi-image capabilities of LVLMs. Using MIMIC, we conduct a series of diagnostic experiments that reveal pervasive issues: LVLMs often fail to aggregate information across images and struggle to track or attend to multiple concepts simultaneously. To address these failures, we propose two novel complementary remedies. On the data side, we present a procedural data-generation strategy that composes single-image annotations into rich, targeted multi-image training examples. On the optimization side, we analyze layer-wise attention patterns and derive an attention-masking scheme tailored for multi-image inputs. Experiments substantially improved cross-image aggregation, while also enhancing performance on existing multi-image benchmarks, outperforming prior state of the art across tasks. Data and code will be made available at https://github.com/anurag-198/MIMIC.

