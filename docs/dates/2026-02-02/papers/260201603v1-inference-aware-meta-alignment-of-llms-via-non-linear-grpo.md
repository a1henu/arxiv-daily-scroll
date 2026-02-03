---
layout: default
title: Inference-Aware Meta-Alignment of LLMs via Non-Linear GRPO
---

# Inference-Aware Meta-Alignment of LLMs via Non-Linear GRPO
**arXiv**：[2602.01603v1](https://arxiv.org/abs/2602.01603) · [PDF](https://arxiv.org/pdf/2602.01603.pdf)  
**作者**：Shokichi Takakura, Akifumi Wachi, Rei Higuchi, Kohei Miyaguchi, Taiji Suzuki  

**一句话要点**：提出推理感知元对齐方法，以有限计算预算实现大语言模型的多准则对齐。

**关键词**：大语言模型对齐, 推理时对齐, 元学习, 非线性优化, 概率测度

## 3 点简述
- 核心问题：大语言模型对齐多准则时计算成本高，推理时对齐需多次前向传播。
- 方法要点：通过推理感知元对齐训练基础模型，使其能通过不同推理时对齐算法有效对齐多任务。
- 实验或效果：提出非线性GRPO解决优化问题，理论上在概率测度空间收敛至最优解。

## 摘要（原文）

> Aligning large language models (LLMs) to diverse human preferences is fundamentally challenging since criteria can often conflict with each other. Inference-time alignment methods have recently gained popularity as they allow LLMs to be aligned to multiple criteria via different alignment algorithms at inference time. However, inference-time alignment is computationally expensive since it often requires multiple forward passes of the base model. In this work, we propose inference-aware meta-alignment (IAMA), a novel approach that enables LLMs to be aligned to multiple criteria with limited computational budget at inference time. IAMA trains a base model such that it can be effectively aligned to multiple tasks via different inference-time alignment algorithms. To solve the non-linear optimization problems involved in IAMA, we propose non-linear GRPO, which provably converges to the optimal solution in the space of probability measures.

