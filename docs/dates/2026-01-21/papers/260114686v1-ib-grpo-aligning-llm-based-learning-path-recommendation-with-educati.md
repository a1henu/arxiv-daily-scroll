---
layout: default
title: IB-GRPO: Aligning LLM-based Learning Path Recommendation with Educational Objectives via Indicator-Based Group Relative Policy Optimization
---

# IB-GRPO: Aligning LLM-based Learning Path Recommendation with Educational Objectives via Indicator-Based Group Relative Policy Optimization
**arXiv**：[2601.14686v1](https://arxiv.org/abs/2601.14686) · [PDF](https://arxiv.org/pdf/2601.14686.pdf)  
**作者**：Shuai Wang, Yaoming Yang, Bingdong Li, Hao Hao, Aimin Zhou  

**一句话要点**：提出IB-GRPO方法，通过指标引导优化，解决LLM在学习路径推荐中与教育目标对齐的挑战。

**关键词**：学习路径推荐, 大语言模型对齐, 多目标强化学习, 最近发展区, 遗传算法, 指标优化

## 3 点简述
- 核心问题：LLM在长时学习路径推荐中，难以对齐最近发展区等教育目标，且面临数据稀缺和多目标交互问题。
- 方法要点：结合遗传算法和教师RL构建混合专家演示，设计ZPD对齐分数，使用Iε+优势指标进行多目标优化。
- 实验或效果：在ASSIST09和Junyi数据集上，基于Qwen2.5-7B模型，相比基线方法取得一致改进。

## 摘要（原文）

> Learning Path Recommendation (LPR) aims to generate personalized sequences of learning items that maximize long-term learning effect while respecting pedagogical principles and operational constraints. Although large language models (LLMs) offer rich semantic understanding for free-form recommendation, applying them to long-horizon LPR is challenging due to (i) misalignment with pedagogical objectives such as the Zone of Proximal Development (ZPD) under sparse, delayed feedback, (ii) scarce and costly expert demonstrations, and (iii) multi-objective interactions among learning effect, difficulty scheduling, length controllability, and trajectory diversity. To address these issues, we propose IB-GRPO (Indicator-Based Group Relative Policy Optimization), an indicator-guided alignment approach for LLM-based LPR. To mitigate data scarcity, we construct hybrid expert demonstrations via Genetic Algorithm search and teacher RL agents and warm-start the LLM with supervised fine-tuning. Building on this warm-start, we design a within-session ZPD alignment score for difficulty scheduling. IB-GRPO then uses the $I_{ε+}$ dominance indicator to compute group-relative advantages over multiple objectives, avoiding manual scalarization and improving Pareto trade-offs. Experiments on ASSIST09 and Junyi using the KES simulator with a Qwen2.5-7B backbone show consistent improvements over representative RL and LLM baselines.

