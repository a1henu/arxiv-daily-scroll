---
layout: default
title: Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
---

# Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
**arXiv**：[2512.15674v1](https://arxiv.org/abs/2512.15674) · [PDF](https://arxiv.org/pdf/2512.15674.pdf)  
**作者**：Adam Karvonen, James Chua, Clément Dumas, Kit Fraser-Taliente, Subhash Kantamneni, Julian Minder, Euan Ong, Arnab Sen Sharma, Daniel Wen, Owain Evans, Samuel Marks  

**一句话要点**：提出激活预言机，通过多样化训练使LLM能通用解释激活信息

**关键词**：激活解释, 自然语言查询, 多样化训练, 分布外泛化, 白盒基线比较

## 3 点简述
- 核心问题：LLM激活难以理解，现有方法复杂且局限于特定任务
- 方法要点：训练LLM直接以激活为输入，用自然语言回答任意问题，并探索训练数据多样性的影响
- 实验或效果：在分布外任务中评估，发现模型能泛化并匹配或超越白盒基线，多样化训练提升性能

## 摘要（原文）

> Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. Our main evaluations are four downstream tasks where we can compare to prior white- and black-box techniques. We find that even narrowly-trained LatentQA models can generalize well, and that adding additional training datasets (such as classification tasks and a self-supervised context prediction task) yields consistent further improvements. Overall, our best AOs match or exceed prior white-box baselines on all four tasks and are the best method on 3 out of 4. These results suggest that diversified training to answer natural-language queries imparts a general capability to verbalize information about LLM activations.

