---
layout: default
title: Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing
---

# Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing
**arXiv**：[2601.15686v1](https://arxiv.org/abs/2601.15686) · [PDF](https://arxiv.org/pdf/2601.15686.pdf)  
**作者**：Xinyu Wang, Sicheng Lyu, Yu Gu, Jerry Huang, Peng Lu, Yufei Cui, Xiao-Wen Chang  

**一句话要点**：提出RLSEdit，一种基于软约束递归最小二乘的LLM终身编辑方法，以解决长序列编辑中的可塑性-稳定性困境。

**关键词**：大语言模型编辑, 终身学习, 递归最小二乘, 在线优化, 可塑性-稳定性权衡, 软约束

## 3 点简述
- 核心问题：现有LLM编辑方法在长流编辑中面临可塑性-稳定性困境，硬写入易累积干扰，硬保护易覆盖过去编辑或导致未约束行为偏离。
- 方法要点：将编辑建模为带软约束的在线二次优化，最小化累积键值拟合目标，通过Woodbury恒等式实现高效在线递归更新。
- 实验或效果：在多个模型家族上实验，稳定扩展至10K编辑，在编辑成功率和整体稳定性上优于基线，保留早期编辑并保持通用能力。

## 摘要（原文）

> Model editing updates a pre-trained LLM with new facts or rules without re-training, while preserving unrelated behavior. In real deployment, edits arrive as long streams, and existing editors often face a plasticity-stability dilemma: locate-then-edit "hard writes" can accumulate interference over time, while null-space-style "hard preservation" preserves only what is explicitly constrained, so past edits can be overwritten and unconstrained behaviors may deviate, degrading general capabilities in the many-edits regime. We propose RLSEdit, a recursive least-squares editor for long sequential editing. RLSEdit formulates editing as an online quadratic optimization with soft constraints, minimizing a cumulative key-value fitting objective with two regularizers that control for both deviation from the pre-trained weights and from a designated anchor mapping. The resulting update admits an efficient online recursion via the Woodbury identity, with per-edit cost independent of history length and scaling only with the current edit size. We further provide deviation bounds and an asymptotic characterization of the adherence-preservation trade-off in the many-edits regime. Experiments on multiple model families demonstrate stable scaling to 10K edits, outperforming strong baselines in both edit success and holistic stability -- crucially retaining early edits, and preserving general capabilities on GLUE and held-out reasoning/code benchmarks.

