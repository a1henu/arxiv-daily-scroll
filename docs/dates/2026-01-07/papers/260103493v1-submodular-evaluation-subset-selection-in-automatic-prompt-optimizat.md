---
layout: default
title: Submodular Evaluation Subset Selection in Automatic Prompt Optimization
---

# Submodular Evaluation Subset Selection in Automatic Prompt Optimization
**arXiv**：[2601.03493v1](https://arxiv.org/abs/2601.03493) · [PDF](https://arxiv.org/pdf/2601.03493.pdf)  
**作者**：Jinming Nian, Zhiyuan Peng, Hongwei Shang, Dae Hoon Park, Yi Fang  

**一句话要点**：提出SESS方法，基于子模性选择评估子集以优化自动提示优化效果

**关键词**：自动提示优化, 评估子集选择, 子模优化, 贪心算法, 大语言模型

## 3 点简述
- 核心问题：自动提示优化依赖小规模评估子集，其选择常被忽视，影响优化效果
- 方法要点：将评估子集选择建模为最大化目标集函数，证明其子模性，采用贪心算法
- 实验或效果：在GSM8K、MATH和GPQA-Diamond数据集上，SESS优于随机或启发式基线

## 摘要（原文）

> Automatic prompt optimization reduces manual prompt engineering, but relies on task performance measured on a small, often randomly sampled evaluation subset as its main source of feedback signal. Despite this, how to select that evaluation subset is usually treated as an implementation detail. We study evaluation subset selection for prompt optimization from a principled perspective and propose SESS, a submodular evaluation subset selection method. We frame selection as maximizing an objective set function and show that, under mild conditions, it is monotone and submodular, enabling greedy selection with theoretical guarantees. Across GSM8K, MATH, and GPQA-Diamond, submodularly selected evaluation subsets can yield better optimized prompts than random or heuristic baselines.

