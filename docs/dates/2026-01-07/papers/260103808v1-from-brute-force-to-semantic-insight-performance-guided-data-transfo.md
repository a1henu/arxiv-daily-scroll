---
layout: default
title: From Brute Force to Semantic Insight: Performance-Guided Data Transformation Design with LLMs
---

# From Brute Force to Semantic Insight: Performance-Guided Data Transformation Design with LLMs
**arXiv**：[2601.03808v1](https://arxiv.org/abs/2601.03808) · [PDF](https://arxiv.org/pdf/2601.03808.pdf)  
**作者**：Usha Shrestha, Dmitry Ignatov, Radu Timofte  

**一句话要点**：提出基于性能反馈的闭环方法，使LLM自主设计数据增强变换以替代暴力搜索。

**关键词**：数据增强设计, 性能反馈学习, LLM微调, 闭环优化, 代码合成

## 3 点简述
- 核心问题：数据增强依赖启发式或暴力方法，缺乏性能导向的自动化设计。
- 方法要点：使用6000多个带准确率标注的PyTorch函数微调LLM，通过成对性能排序对齐反馈。
- 实验或效果：候选评估减少高达600倍，保持竞争性峰值准确率，模型内化语义性能线索。

## 摘要（原文）

> Large language models (LLMs) have achieved notable performance in code synthesis; however, data-aware augmentation remains a limiting factor, handled via heuristic design or brute-force approaches. We introduce a performance-aware, closed-loop solution in the NNGPT ecosystem of projects that enables LLMs to autonomously engineer optimal transformations by internalizing empirical performance cues. We fine-tune LLMs with Low-Rank Adaptation on a novel repository of more than 6,000 empirically evaluated PyTorch augmentation functions, each annotated solely by downstream model accuracy. Training uses pairwise performance ordering (better-worse transformations), enabling alignment through empirical feedback without reinforcement learning, reward models, or symbolic objectives. This reduces the need for exhaustive search, achieving up to 600x times fewer evaluated candidates than brute-force discovery while maintaining competitive peak accuracy and shifting generation from random synthesis to task-aligned design. Ablation studies show that structured Chain-of-Thought prompting introduces syntactic noise and degrades performance, whereas direct prompting ensures stable optimization in performance-critical code tasks. Qualitative and quantitative analyses demonstrate that the model internalizes semantic performance cues rather than memorizing syntax. These results show that LLMs can exhibit task-level reasoning through non-textual feedback loops, bypassing explicit symbolic rewards.

