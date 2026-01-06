---
layout: default
title: ELLA: Efficient Lifelong Learning for Adapters in Large Language Models
---

# ELLA: Efficient Lifelong Learning for Adapters in Large Language Models
**arXiv**：[2601.02232v1](https://arxiv.org/abs/2601.02232) · [PDF](https://arxiv.org/pdf/2601.02232.pdf)  
**作者**：Shristi Das Biswas, Yue Zhang, Anwesan Pal, Radhika Bhargava, Kaushik Roy  

**一句话要点**：提出ELLA框架，通过选择性子空间去相关解决大语言模型持续学习中的灾难性遗忘问题。

**关键词**：持续学习, 灾难性遗忘, 大语言模型适配, 选择性子空间去相关, 轻量级正则化, 零样本泛化

## 3 点简述
- 核心问题：大语言模型在持续学习场景下顺序适应新任务时，面临严重的灾难性遗忘，现有方法如重放或严格正交性存在局限性。
- 方法要点：基于选择性子空间去相关原则，通过轻量级正则化惩罚高能量任务特定方向的对齐，保留低能量子空间自由度以促进迁移。
- 实验或效果：在三个流行基准上实现最先进的持续学习性能，相对准确率提升达9.6%，内存占用减少35倍，且无需数据重放或架构扩展。

## 摘要（原文）

> Large Language Models (LLMs) suffer severe catastrophic forgetting when adapted sequentially to new tasks in a continual learning (CL) setting. Existing approaches are fundamentally limited: replay-based methods are impractical and privacy-violating, while strict orthogonality-based methods collapse under scale: each new task is projected onto an orthogonal complement, progressively reducing the residual degrees of freedom and eliminating forward transfer by forbidding overlap in shared representations. In this work, we introduce ELLA, a training framework built on the principle of selective subspace de-correlation. Rather than forbidding all overlap, ELLA explicitly characterizes the structure of past updates and penalizes alignments along their high-energy, task-specific directions, while preserving freedom in the low-energy residual subspaces to enable transfer. Formally, this is realized via a lightweight regularizer on a single aggregated update matrix. We prove this mechanism corresponds to an anisotropic shrinkage operator that bounds interference, yielding a penalty that is both memory- and compute-constant regardless of task sequence length. ELLA requires no data replay, no architectural expansion, and negligible storage. Empirically, it achieves state-of-the-art CL performance on three popular benchmarks, with relative accuracy gains of up to $9.6\%$ and a $35\times$ smaller memory footprint. Further, ELLA scales robustly across architectures and actively enhances the model's zero-shot generalization performance on unseen tasks, establishing a principled and scalable solution for constructive lifelong LLM adaptation.

