---
layout: default
title: Prototype Transformer: Towards Language Model Architectures Interpretable by Design
---

# Prototype Transformer: Towards Language Model Architectures Interpretable by Design
**arXiv**：[2602.11852v1](https://arxiv.org/abs/2602.11852) · [PDF](https://arxiv.org/pdf/2602.11852.pdf)  
**作者**：Yordan Yordanov, Matteo Forasassi, Bayar Menzat, Ruizhi Wang, Chang Qi, Markus Kaltenberger, Amine M'Charrak, Tommaso Salvatori, Thomas Lukasiewicz  

**一句话要点**：提出原型Transformer以构建可解释的自回归语言模型架构

**关键词**：可解释语言模型, 原型学习, 自回归模型, 线性复杂度, 模型编辑, 概念捕获

## 3 点简述
- 核心问题：当前语言模型推理不透明，影响信任并带来风险如幻觉。
- 方法要点：基于原型向量实现输入序列与原型的双向通信，自动捕获可命名概念。
- 实验或效果：在文本生成和GLUE任务上表现良好，计算复杂度线性于序列长度。

## 摘要（原文）

> While state-of-the-art language models (LMs) surpass the vast majority of humans in certain domains, their reasoning remains largely opaque, undermining trust in their output. Furthermore, while autoregressive LMs can output explicit reasoning, their true reasoning process is opaque, which introduces risks like deception and hallucination. In this work, we introduce the Prototype Transformer (ProtoT) -- an autoregressive LM architecture based on prototypes (parameter vectors), posed as an alternative to the standard self-attention-based transformers. ProtoT works by means of two-way communication between the input sequence and the prototypes, and we show that this leads to the prototypes automatically capturing nameable concepts (e.g. "woman") during training. They provide the potential to interpret the model's reasoning and allow for targeted edits of its behavior. Furthermore, by design, the prototypes create communication channels that aggregate contextual information at different time scales, aiding interpretability. In terms of computation scalability, ProtoT scales linearly with sequence length vs the quadratic scalability of SOTA self-attention transformers. Compared to baselines, ProtoT scales well with model and data size, and performs well on text generation and downstream tasks (GLUE). ProtoT exhibits robustness to input perturbations on par or better than some baselines, but differs from them by providing interpretable pathways showing how robustness and sensitivity arises. Reaching close to the performance of state-of-the-art architectures, ProtoT paves the way to creating well-performing autoregressive LMs interpretable by design.

