---
layout: default
title: HarmonyCell: Automating Single-Cell Perturbation Modeling under Semantic and Distribution Shifts
---

# HarmonyCell: Automating Single-Cell Perturbation Modeling under Semantic and Distribution Shifts
**arXiv**：[2603.01396v1](https://arxiv.org/abs/2603.01396) · [PDF](https://arxiv.org/pdf/2603.01396.pdf)  
**作者**：Wenxuan Huang, Mingyu Tsoi, Yanhao Huang, Xinjie Mao, Xue Xia, Hao Wu, Jiaqi Wei, Yuejin Yang, Lang Yu, Cheng Tan, Xiang Zhang, Zhangyang Gao, Siqi Sun  

**一句话要点**：提出HarmonyCell框架以解决单细胞扰动建模中的语义和分布异质性瓶颈

**关键词**：单细胞扰动建模, 语义异质性, 分布偏移, LLM驱动, 蒙特卡洛树搜索, 自动虚拟细胞建模

## 3 点简述
- 核心问题：单细胞扰动研究面临语义异质性（元数据模式不兼容）和统计异质性（分布偏移）的双重挑战
- 方法要点：采用LLM驱动的语义统一器自动映射元数据，结合自适应蒙特卡洛树搜索引擎优化架构以应对分布偏移
- 实验或效果：在语义和分布偏移任务中，实现95%有效执行率，并在分布外评估中匹配或超越专家基线

## 摘要（原文）

> Single-cell perturbation studies face dual heterogeneity bottlenecks: (i) semantic heterogeneity--identical biological concepts encoded under incompatible metadata schemas across datasets; and (ii) statistical heterogeneity--distribution shifts from biological variation demanding dataset-specific inductive biases. We propose HarmonyCell, an end-to-end agent framework resolving each challenge through a dedicated mechanism: an LLM-driven Semantic Unifier autonomously maps disparate metadata into a canonical interface without manual intervention; and an adaptive Monte Carlo Tree Search engine operates over a hierarchical action space to synthesize architectures with optimal statistical inductive biases for distribution shifts. Evaluated across diverse perturbation tasks under both semantic and distribution shifts, HarmonyCell achieves a 95% valid execution rate on heterogeneous input datasets (versus 0% for general agents) while matching or even exceeding expert-designed baselines in rigorous out-of-distribution evaluations. This dual-track orchestration enables scalable automatic virtual cell modeling without dataset-specific engineering.

