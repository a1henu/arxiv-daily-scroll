---
layout: default
title: Retrieval-augmented Prompt Learning for Pre-trained Foundation Models
---

# Retrieval-augmented Prompt Learning for Pre-trained Foundation Models
**arXiv**：[2512.20145v1](https://arxiv.org/abs/2512.20145) · [PDF](https://arxiv.org/pdf/2512.20145.pdf)  
**作者**：Xiang Chen, Yixin Ou, Quan Feng, Lei Li, Piji Li, Haibo Ye, Sheng-Jun Huang, Shuofei Qiao, Shumin Deng, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出RetroPrompt以解决预训练基础模型提示学习中记忆与泛化的平衡问题

**关键词**：预训练基础模型, 提示学习, 检索增强, 零样本学习, 少样本学习, 泛化能力

## 3 点简述
- 核心问题：传统提示学习依赖参数化学习，可能导致记忆不稳定和泛化不足，难以充分利用非典型实例。
- 方法要点：RetroPrompt通过检索机制从训练数据知识库中动态获取上下文信息，解耦知识记忆，增强提示线索。
- 实验或效果：在NLP和CV任务的多数据集上验证，RetroPrompt在零样本和少样本场景中表现优越，减少死记硬背依赖。

## 摘要（原文）

> The pre-trained foundation models (PFMs) have become essential for facilitating large-scale multimodal learning. Researchers have effectively employed the ``pre-train, prompt, and predict'' paradigm through prompt learning to induce improved few-shot performance. However, prompt learning approaches for PFMs still follow a parametric learning paradigm. As such, the stability of generalization in memorization and rote learning can be compromised. More specifically, conventional prompt learning might face difficulties in fully utilizing atypical instances and avoiding overfitting to shallow patterns with limited data during the process of fully-supervised training. To overcome these constraints, we present our approach, named RetroPrompt, which aims to achieve a balance between memorization and generalization by decoupling knowledge from mere memorization. Unlike traditional prompting methods, RetroPrompt leverages a publicly accessible knowledge base generated from the training data and incorporates a retrieval mechanism throughout the input, training, and inference stages. This enables the model to actively retrieve relevant contextual information from the corpus, thereby enhancing the available cues. We conduct comprehensive experiments on a variety of datasets across natural language processing and computer vision tasks to demonstrate the superior performance of our proposed approach, RetroPrompt, in both zero-shot and few-shot scenarios. Through detailed analysis of memorization patterns, we observe that RetroPrompt effectively reduces the reliance on rote memorization, leading to enhanced generalization.

