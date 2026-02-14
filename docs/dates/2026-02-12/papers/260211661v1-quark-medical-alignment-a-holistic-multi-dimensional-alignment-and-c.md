---
layout: default
title: Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm
---

# Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm
**arXiv**：[2602.11661v1](https://arxiv.org/abs/2602.11661) · [PDF](https://arxiv.org/pdf/2602.11661.pdf)  
**作者**：Tianxiang Xu, Jiayi Liu, Yixuan Tong, Jialu Xu, Yunqing Wei, Kaiwen Feng, PanPan Hou, Kangping Yin, Jiyuan Hu, Hao Zhou, Zhenxin Ma, Jian Xu, Guanjun Jiang  

**一句话要点**：提出Quark Medical Alignment范式，以解决医疗问答中多目标对齐的挑战

**关键词**：医疗问答对齐, 多目标优化, 强化学习, 参考冻结归一化, 自适应动态加权, 垂直领域对齐

## 3 点简述
- 核心问题：现有强化学习对齐方法在医疗领域存在成本高、验证难和多目标冲突问题
- 方法要点：构建多维度对齐矩阵，结合参考冻结归一化和三因子自适应动态加权进行协同优化
- 实验或效果：在真实医疗场景评估中验证了有效性，为垂直领域复杂对齐提供新范式

## 摘要（原文）

> While reinforcement learning for large language model alignment has progressed rapidly in recent years, transferring these paradigms to high-stakes medical question answering reveals a fundamental paradigm mismatch. Reinforcement Learning from Human Feedback relies on preference annotations that are prohibitively expensive and often fail to reflect the absolute correctness of medical facts. Reinforcement Learning from Verifiable Rewards lacks effective automatic verifiers and struggles to handle complex clinical contexts. Meanwhile, medical alignment requires the simultaneous optimization of correctness, safety, and compliance, yet multi-objective heterogeneous reward signals are prone to scale mismatch and optimization conflicts.To address these challenges, we propose a robust medical alignment paradigm. We first construct a holistic multi-dimensional medical alignment matrix that decomposes alignment objectives into four categories: fundamental capabilities, expert knowledge, online feedback, and format specifications. Within each category, we establish a closed loop of where observable metrics inform attributable diagnosis, which in turn drives optimizable rewards, thereby providing fine-grained, high-resolution supervision signals for subsequent iterative optimization. To resolve gradient domination and optimization instability problem caused by heterogeneous signals, we further propose a unified optimization mechanism. This mechanism employs Reference-Frozen Normalization to align reward scales and implements a Tri-Factor Adaptive Dynamic Weighting strategy to achieve collaborative optimization that is weakness-oriented, risk-prioritized, and redundancy-reducing. Experimental results demonstrate the effectiveness of our proposed paradigm in real-world medical scenario evaluations, establishing a new paradigm for complex alignment in vertical domains.

