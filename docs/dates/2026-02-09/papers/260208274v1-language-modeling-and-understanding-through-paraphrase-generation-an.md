---
layout: default
title: Language Modeling and Understanding Through Paraphrase Generation and Detection
---

# Language Modeling and Understanding Through Paraphrase Generation and Detection
**arXiv**：[2602.08274v1](https://arxiv.org/abs/2602.08274) · [PDF](https://arxiv.org/pdf/2602.08274.pdf)  
**作者**：Jan Philip Wahle  

**一句话要点**：提出基于释义类型分解的方法以提升语言模型在语义理解与下游任务中的性能

**关键词**：释义生成, 语义理解, 语言模型, 剽窃检测, 下游任务

## 3 点简述
- 核心问题：现有方法将释义简化为二元决策或单一改写，难以细粒度分析语义等价性。
- 方法要点：将释义分解为构成性语言方面（释义类型），提供更细粒度和认知基础的语义等价视图。
- 实验或效果：在剽窃检测和重复问题识别等任务中，基于释义类型训练的模型超越人类基线或改进现有模型性能。

## 摘要（原文）

> Language enables humans to share knowledge, reason about the world, and pass on strategies for survival and innovation across generations. At the heart of this process is not just the ability to communicate but also the remarkable flexibility in how we can express ourselves. We can express the same thoughts in virtually infinite ways using different words and structures - this ability to rephrase and reformulate expressions is known as paraphrase. Modeling paraphrases is a keystone to meaning in computational language models; being able to construct different variations of texts that convey the same meaning or not shows strong abilities of semantic understanding. If computational language models are to represent meaning, they must understand and control the different aspects that construct the same meaning as opposed to different meanings at a fine granularity. Yet most existing approaches reduce paraphrasing to a binary decision between two texts or to producing a single rewrite of a source, obscuring which linguistic factors are responsible for meaning preservation. In this thesis, I propose that decomposing paraphrases into their constituent linguistic aspects (paraphrase types) offers a more fine-grained and cognitively grounded view of semantic equivalence. I show that even advanced machine learning models struggle with this task. Yet, when explicitly trained on paraphrase types, models achieve stronger performance on related paraphrase tasks and downstream applications. For example, in plagiarism detection, language models trained on paraphrase types surpass human baselines: 89.6% accuracy compared to 78.4% for plagiarism cases from Wikipedia, and 66.5% compared to 55.7% for plagiarism of scientific papers from arXiv. In identifying duplicate questions on Quora, models trained with paraphrase types improve over models trained on binary pairs. Furthermore, I demonstrate that...

