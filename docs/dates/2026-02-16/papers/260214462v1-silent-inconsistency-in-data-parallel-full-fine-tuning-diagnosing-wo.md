---
layout: default
title: Silent Inconsistency in Data-Parallel Full Fine-Tuning: Diagnosing Worker-Level Optimization Misalignment
---

# Silent Inconsistency in Data-Parallel Full Fine-Tuning: Diagnosing Worker-Level Optimization Misalignment
**arXiv**：[2602.14462v1](https://arxiv.org/abs/2602.14462) · [PDF](https://arxiv.org/pdf/2602.14462.pdf)  
**作者**：Hong Li, Zhen Zhou, Honggang Zhang, Yuping Luo, Xinyue Wang, Han Gong, Zhiyuan Liu  

**一句话要点**：提出轻量级诊断框架以检测数据并行全微调中的工作节点优化不一致问题

**关键词**：数据并行训练, 全参数微调, 优化不一致, 梯度诊断, 大语言模型

## 3 点简述
- 核心问题：数据并行训练中工作节点间损失和梯度存在隐藏不一致，称为静默不一致
- 方法要点：引入损失分散、梯度范数分散和梯度方向一致性三个互补指标进行量化诊断
- 实验或效果：在8-NPU设置下验证指标能揭示隐藏不稳定性，尽管全局平均损失曲线平滑

## 摘要（原文）

> Data-parallel (DP) training with synchronous all-reduce is a dominant paradigm for full-parameter fine-tuning of large language models (LLMs). While parameter synchronization guarantees numerical equivalence of model weights after each iteration, it does not necessarily imply alignment of worker-level optimization dynamics before gradient aggregation. This paper identifies and studies this latent mismatch, termed \emph{silent inconsistency}, where cross-worker divergence in losses and gradients can remain invisible under conventional aggregated monitoring signals. We propose a lightweight, model-agnostic diagnostic framework that quantifies worker-level consistency using training signals readily available in standard pipelines. Specifically, we introduce three complementary metrics: loss dispersion, gradient-norm dispersion, and gradient-direction consistency measured by inter-worker cosine similarity. The proposed metrics incur negligible overhead and require no modification to model architecture, synchronization mechanisms, or optimization algorithms. We validate the framework by fully fine-tuning the 1B-parameter \texttt{openPangu-Embedded-1B-V1.1} model on the \texttt{tatsu-lab/alpaca} dataset using an 8-NPU DP setup, under controlled perturbations of cross-rank stochasticity. Experimental results show that progressively desynchronized data shuffling and random seeds lead to substantial increases in loss/gradient dispersion and reduced directional alignment, despite smooth globally averaged loss curves. These findings demonstrate that the proposed indicators provide actionable visibility into hidden instability modes in large-scale DP fine-tuning, enabling more reliable diagnosis and configuration assessment.

