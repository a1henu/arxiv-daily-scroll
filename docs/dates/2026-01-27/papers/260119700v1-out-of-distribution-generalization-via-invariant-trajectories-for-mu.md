---
layout: default
title: Out-of-Distribution Generalization via Invariant Trajectories for Multimodal Large Language Model Editing
---

# Out-of-Distribution Generalization via Invariant Trajectories for Multimodal Large Language Model Editing
**arXiv**：[2601.19700v1](https://arxiv.org/abs/2601.19700) · [PDF](https://arxiv.org/pdf/2601.19700.pdf)  
**作者**：Jiajie Su, Haoyuan Wang, Xiaohua Feng, Yunshan Ma, Xiaobo Xia, Yuyuan Li, Xiaolin Zheng, Jianmao Xiao, Chaochao Chen  

**一句话要点**：提出ODEdit框架，通过不变轨迹学习解决多模态大语言模型编辑中的分布外泛化问题。

**关键词**：多模态大语言模型编辑, 分布外泛化, 不变轨迹学习, 因果推理, 知识编辑, 跨模态提示

## 3 点简述
- 核心问题：现有单模态LLM编辑方法在MLLM中导致因果欠拟合和过拟合，难以处理跨模态提示的语义偏移。
- 方法要点：将MLLM编辑重构为OOD泛化问题，引入不变轨迹学习，优化三方风险目标以增强编辑可靠性、局部性和泛化性。
- 实验或效果：理论分析和广泛实验验证了ODEdit在提升编辑鲁棒性和泛化能力方面的有效性。

## 摘要（原文）

> Knowledge editing emerges as a crucial technique for efficiently correcting incorrect or outdated knowledge in large language models (LLM). Existing editing methods for unimodal LLM rely on a rigid parameter-to-output mapping, which causes causal-underfit and causal-overfit in cascaded reasoning for Multimodal LLM (MLLM). In this paper, we reformulate MLLM editing as an out-of-distribution (OOD) generalization problem, where the goal is to discern semantic shift with factual shift and thus achieve robust editing among diverse cross-modal prompting. The key challenge of this OOD problem lies in identifying invariant causal trajectories that generalize accurately while suppressing spurious correlations. To address it, we propose ODEdit, a plug-and-play invariant learning based framework that optimizes the tripartite OOD risk objective to simultaneously enhance editing reliability, locality, and generality.We further introduce an edit trajectory invariant learning method, which integrates a total variation penalty into the risk minimization objective to stabilize edit trajectories against environmental variations. Theoretical analysis and extensive experiments demonstrate the effectiveness of ODEdit.

