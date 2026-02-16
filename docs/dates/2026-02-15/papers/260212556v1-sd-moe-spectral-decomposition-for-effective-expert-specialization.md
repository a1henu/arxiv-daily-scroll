---
layout: default
title: SD-MoE: Spectral Decomposition for Effective Expert Specialization
---

# SD-MoE: Spectral Decomposition for Effective Expert Specialization
**arXiv**：[2602.12556v1](https://arxiv.org/abs/2602.12556) · [PDF](https://arxiv.org/pdf/2602.12556.pdf)  
**作者**：Ruijun Huang, Fang Dong, Xin Zhang, Hengjie Cao, Zhendong Huang, Anrui Chen, Jixian Zhou, Mengyi Chen, Yifeng Yang, Mingzhi Dong, Yujiang Wang, Jinlong Hou, Qin Lv, Robert P. Dick, Yuan Cheng, Fan Yang, Tun Lu, Chun Zhang, Li Shang  

**一句话要点**：提出SD-MoE以解决MoE架构中专家专业化不足的问题

**关键词**：混合专家模型, 谱分解, 专家专业化, 条件计算, 梯度对齐, 低秩结构

## 3 点简述
- 核心问题：MoE中专家参数和梯度谱重叠，导致功能相似和共享专家现象
- 方法要点：在谱空间分解参数和梯度，促进专家专业化，计算开销小
- 实验或效果：提升下游任务性能，可集成到Qwen和DeepSeek等现有MoE架构

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures scale Large Language Models via expert specialization induced by conditional computation. In practice, however, expert specialization often fails: some experts become functionally similar, while others functioning as de facto shared experts, limiting the effective capacity and model performance. In this work, we analysis from a spectral perspective on parameter and gradient spaces, uncover that (1) experts share highly overlapping dominant spectral components in their parameters, (2) dominant gradient subspaces are strongly aligned across experts, driven by ubiquitous low-rank structure in human corpus, and (3) gating mechanisms preferentially route inputs along these dominant directions, further limiting specialization. To address this, we propose Spectral-Decoupled MoE (SD-MoE), which decomposes both parameter and gradient in the spectral space. SD-MoE improves performance across downstream tasks, enables effective expert specialization, incurring minimal additional computation, and can be seamlessly integrated into a wide range of existing MoE architectures, including Qwen and DeepSeek.

