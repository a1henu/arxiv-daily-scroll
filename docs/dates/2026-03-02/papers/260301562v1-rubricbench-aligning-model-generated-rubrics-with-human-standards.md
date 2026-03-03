---
layout: default
title: RubricBench: Aligning Model-Generated Rubrics with Human Standards
---

# RubricBench: Aligning Model-Generated Rubrics with Human Standards
**arXiv**：[2603.01562v1](https://arxiv.org/abs/2603.01562) · [PDF](https://arxiv.org/pdf/2603.01562.pdf)  
**作者**：Qiyuan Zhang, Junyi Zhou, Yufei Wang, Fuyuan Lyu, Yidong Ming, Can Xu, Qingfeng Sun, Kai Zheng, Peng Kang, Xue Liu, Chen Ma  

**一句话要点**：提出RubricBench基准以评估基于评分标准的模型评估可靠性

**关键词**：大语言模型对齐, 评分标准评估, 基准构建, 专家标注, 模型评估可靠性, 表面偏差缓解

## 3 点简述
- 核心问题：缺乏统一基准评估基于评分标准的LLM对齐，现有基准缺乏判别复杂性和真实评分标准标注
- 方法要点：构建包含1147对比较的基准，通过多维过滤针对复杂输入和表面偏差的困难样本，并添加专家标注的原子评分标准
- 实验或效果：实验显示模型生成评分标准与人类标注存在显著能力差距，先进模型难以自主指定有效评估标准

## 摘要（原文）

> As Large Language Model (LLM) alignment evolves from simple completions to complex, highly sophisticated generation, Reward Models are increasingly shifting toward rubric-guided evaluation to mitigate surface-level biases. However, the community lacks a unified benchmark to assess this evaluation paradigm, as existing benchmarks lack both the discriminative complexity and the ground-truth rubric annotations required for rigorous analysis. To bridge this gap, we introduce RubricBench, a curated benchmark with 1,147 pairwise comparisons specifically designed to assess the reliability of rubric-based evaluation. Our construction employs a multi-dimensional filtration pipeline to target hard samples featuring nuanced input complexity and misleading surface bias, augmenting each with expert-annotated, atomic rubrics derived strictly from instructions. Comprehensive experiments reveal a substantial capability gap between human-annotated and model-generated rubrics, indicating that even state-of-the-art models struggle to autonomously specify valid evaluation criteria, lagging considerably behind human-guided performance.

