---
layout: default
title: Unlabeled Data Can Provably Enhance In-Context Learning of Transformers
---

# Unlabeled Data Can Provably Enhance In-Context Learning of Transformers
**arXiv**：[2601.10058v1](https://arxiv.org/abs/2601.10058) · [PDF](https://arxiv.org/pdf/2601.10058.pdf)  
**作者**：Renpu Liu, Jing Yang  

**一句话要点**：提出增强上下文学习框架，利用未标记数据提升Transformer性能

**关键词**：上下文学习, 未标记数据, Transformer, 期望最大化, 理论分析, 线性分类

## 3 点简述
- 研究未标记数据如何理论增强Transformer上下文学习性能
- 结合标签示例与未标记输入，通过思维链提示模拟期望最大化算法
- 实验显示框架优于传统少样本学习，支持理论发现

## 摘要（原文）

> Large language models (LLMs) exhibit impressive in-context learning (ICL) capabilities, yet the quality of their predictions is fundamentally limited by the few costly labeled demonstrations that can fit into a prompt. Meanwhile, there exist vast and continuously growing amounts of unlabeled data that may be closely related to the ICL task. How to utilize such unlabeled data to provably enhance the performance of ICL thus becomes an emerging fundamental question. In this work, we propose a novel augmented ICL framework, in which the prompt includes a small set of labeled examples alongside a block of unlabeled inputs. We focus on the multi-class linear classification setting and demonstrate that, with chain-of-thought (CoT) prompting, a multi-layer transformer can effectively emulate an expectation-maximization (EM) algorithm. This enables the transformer to implicitly extract useful information from both labeled and unlabeled data, leading to provable improvements in ICL accuracy. Moreover, we show that such a transformer can be trained via teacher forcing, with its parameters converging to the desired solution at a linear rate. Experiments demonstrate that the augmented ICL framework consistently outperforms conventional few-shot ICL, providing empirical support for our theoretical findings. To the best of our knowledge, this is the first theoretical study on the impact of unlabeled data on the ICL performance of transformers.

