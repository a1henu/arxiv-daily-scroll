---
layout: default
title: NRGPT: An Energy-based Alternative for GPT
---

# NRGPT: An Energy-based Alternative for GPT
**arXiv**：[2512.16762v1](https://arxiv.org/abs/2512.16762) · [PDF](https://arxiv.org/pdf/2512.16762.pdf)  
**作者**：Nima Dehmamy, Benjamin Hoover, Bishwajit Saha, Leo Kozachkov, Jean-Jacques Slotine, Dmitry Krotov  

**一句话要点**：提出NRGPT模型，将GPT与能量基模型统一，用于语言建模任务。

**关键词**：能量基模型, 语言建模, GPT架构, 推理探索, 抗过拟合

## 3 点简述
- 核心问题：GPT架构流行，但能量基建模作为不同范式未被整合。
- 方法要点：通过最小修改GPT，将推理视为能量景观上的探索过程。
- 实验或效果：在Shakespeare、ListOPS和OpenWebText数据集上表现良好，可能更抗过拟合。

## 摘要（原文）

> Generative Pre-trained Transformer (GPT) architectures are the most popular design for language modeling. Energy-based modeling is a different paradigm that views inference as a dynamical process operating on an energy landscape. We propose a minimal modification of the GPT setting to unify it with the EBM framework. The inference step of our model, which we call eNeRgy-GPT (NRGPT), is conceptualized as an exploration of the tokens on the energy landscape. We prove, and verify empirically, that under certain circumstances this exploration becomes gradient descent, although they don't necessarily lead to the best performing models. We demonstrate that our model performs well for simple language (Shakespeare dataset), algebraic ListOPS tasks, and richer settings such as OpenWebText language modeling. We also observe that our models may be more resistant to overfitting, doing so only during very long training.

