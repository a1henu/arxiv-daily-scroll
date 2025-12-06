---
layout: default
title: LLMs Know More Than Words: A Genre Study with Syntax, Metaphor & Phonetics
---

# LLMs Know More Than Words: A Genre Study with Syntax, Metaphor & Phonetics
**arXiv**：[2512.04957v1](https://arxiv.org/abs/2512.04957) · [PDF](https://arxiv.org/pdf/2512.04957.pdf)  
**作者**：Weiye Shi, Zhaowei Zhang, Shaoheng Yan, Yaodong Yang  

**一句话要点**：提出基于多语言文学体裁分类数据集，评估大语言模型对句法、隐喻和语音特征的捕获能力。

**关键词**：大语言模型, 体裁分类, 句法分析, 隐喻检测, 语音特征, 多语言评估

## 3 点简述
- 核心问题：大语言模型是否能从原始文本中有效学习深层语言属性，如句法结构和语音模式。
- 方法要点：构建多语言体裁分类数据集，并显式添加句法树、隐喻计数和语音指标特征集。
- 实验或效果：实验表明，不同特征对分类任务贡献不均，强调训练中融入复杂语言信号的重要性。

## 摘要（原文）

> Large language models (LLMs) demonstrate remarkable potential across diverse language related tasks, yet whether they capture deeper linguistic properties, such as syntactic structure, phonetic cues, and metrical patterns from raw text remains unclear. To analysis whether LLMs can learn these features effectively and apply them to important nature language related tasks, we introduce a novel multilingual genre classification dataset derived from Project Gutenberg, a large-scale digital library offering free access to thousands of public domain literary works, comprising thousands of sentences per binary task (poetry vs. novel;drama vs. poetry;drama vs. novel) in six languages (English, French, German, Italian, Spanish, and Portuguese). We augment each with three explicit linguistic feature sets (syntactic tree structures, metaphor counts, and phonetic metrics) to evaluate their impact on classification performance. Experiments demonstrate that although LLM classifiers can learn latent linguistic structures either from raw text or from explicitly provided features, different features contribute unevenly across tasks, which underscores the importance of incorporating more complex linguistic signals during model training.

