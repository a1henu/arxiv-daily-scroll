---
layout: default
title: YuriiFormer: A Suite of Nesterov-Accelerated Transformers
---

# YuriiFormer: A Suite of Nesterov-Accelerated Transformers
**arXiv**：[2601.23236v1](https://arxiv.org/abs/2601.23236) · [PDF](https://arxiv.org/pdf/2601.23236.pdf)  
**作者**：Aleksandr Zimin, Yury Polyanskiy, Philippe Rigollet  

**一句话要点**：提出基于Nesterov加速的Transformer架构，通过优化理论视角提升语言模型性能。

**关键词**：Transformer架构, 优化理论, Nesterov加速, 语言模型, 变分框架

## 3 点简述
- 将Transformer层解释为优化算法迭代，自注意力对应交互能量梯度步，MLP对应势能梯度步。
- 引入Nesterov加速Transformer，保持注意力与MLP结构，基于优化原理设计架构。
- 在TinyStories和OpenWebText上优于nanoGPT基线，验证优化理论指导的实践增益。

## 摘要（原文）

> We propose a variational framework that interprets transformer layers as iterations of an optimization algorithm acting on token embeddings. In this view, self-attention implements a gradient step of an interaction energy, while MLP layers correspond to gradient updates of a potential energy. Standard GPT-style transformers emerge as vanilla gradient descent on the resulting composite objective, implemented via Lie--Trotter splitting between these two energy functionals. This perspective enables principled architectural design using classical optimization ideas. As a proof of concept, we introduce a Nesterov-style accelerated transformer that preserves the same attention and MLP oracles. The resulting architecture consistently outperforms a nanoGPT baseline on TinyStories and OpenWebText, demonstrating that optimization-theoretic insights can translate into practical gains.

