---
layout: default
title: System 1&2 Synergy via Dynamic Model Interpolation
---

# System 1&2 Synergy via Dynamic Model Interpolation
**arXiv**：[2601.21414v1](https://arxiv.org/abs/2601.21414) · [PDF](https://arxiv.org/pdf/2601.21414.pdf)  
**作者**：Chenxu Yang, Qingyi Si, Chong Tian, Xiyu Liu, Dingyu Yao, Chuanyu Qin, Zheng Lin, Weiping Wang, Jiaqi Wang  

**一句话要点**：提出动态模型插值框架DAMI，通过能力控制结合直觉与深思认知模式以提升推理效率与精度。

**关键词**：动态模型插值, 能力控制, 认知模式协同, 参数插值, 数学推理, 零样本部署

## 3 点简述
- 核心问题：统一语言模型中直觉与深思认知模式存在干扰，现有方法聚焦输出控制而非能力控制。
- 方法要点：利用动态参数插值，基于查询估计推理强度，无需额外训练即可调制模型认知深度。
- 实验或效果：在五个数学推理基准上，DAMI比深思模型更准确且保持高效，实现系统1效率与系统2推理深度的结合。

## 摘要（原文）

> Training a unified language model that adapts between intuitive System 1 and deliberative System 2 remains challenging due to interference between their cognitive modes. Recent studies have thus pursued making System 2 models more efficient. However, these approaches focused on output control, limiting what models produce. We argue that this paradigm is misaligned: output length is merely a symptom of the model's cognitive configuration, not the root cause. In this work, we shift the focus to capability control, which modulates \textit{how models think} rather than \textit{what they produce}. To realize this, we leverage existing Instruct and Thinking checkpoints through dynamic parameter interpolation, without additional training. Our pilot study establishes that linear interpolation yields a convex, monotonic Pareto frontier, underpinned by representation continuity and structural connectivity. Building on this, we propose \textbf{DAMI} (\textbf{D}yn\textbf{A}mic \textbf{M}odel \textbf{I}nterpolation), a framework that estimates a query-specific Reasoning Intensity $λ(q)$ to configure cognitive depth. For training-based estimation, we develop a preference learning method encoding accuracy and efficiency criteria. For zero-shot deployment, we introduce a confidence-based method leveraging inter-model cognitive discrepancy. Experiments on five mathematical reasoning benchmarks demonstrate that DAMI achieves higher accuracy than the Thinking model while remaining efficient, effectively combining the efficiency of System 1 with the reasoning depth of System 2.

