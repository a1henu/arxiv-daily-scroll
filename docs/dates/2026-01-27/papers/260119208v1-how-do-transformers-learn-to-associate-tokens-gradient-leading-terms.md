---
layout: default
title: How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
---

# How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
**arXiv**：[2601.19208v1](https://arxiv.org/abs/2601.19208) · [PDF](https://arxiv.org/pdf/2601.19208.pdf)  
**作者**：Shawn Im, Changdae Oh, Zhen Fang, Sharon Li  

**一句话要点**：提出梯度主导项近似方法，以闭式表达解释Transformer早期训练中语义关联的形成机制。

**关键词**：Transformer机制解释, 梯度主导项近似, 语义关联学习, 训练动态分析, 闭式权重表达

## 3 点简述
- 核心问题：Transformer模型如何从自然语言数据中学习语义关联，如'鸟'与'飞'的联系。
- 方法要点：利用梯度主导项近似，推导训练早期权重的闭式表达式，揭示基于三种基础函数的组合机制。
- 实验或效果：在真实LLMs上验证理论权重与学习权重匹配，并通过定性分析解释Transformer的语义关联学习。

## 摘要（原文）

> Semantic associations such as the link between "bird" and "flew" are foundational for language modeling as they enable models to go beyond memorization and instead generalize and generate coherent text. Understanding how these associations are learned and represented in language models is essential for connecting deep learning with linguistic theory and developing a mechanistic foundation for large language models. In this work, we analyze how these associations emerge from natural language data in attention-based language models through the lens of training dynamics. By leveraging a leading-term approximation of the gradients, we develop closed-form expressions for the weights at early stages of training that explain how semantic associations first take shape. Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions (bigram, token-interchangeability, and context mappings), reflecting the statistics of the text corpus and uncovering how each component of the transformer captures semantic associations based on these compositions. Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further show how our theorem shines light on interpreting the learned associations in transformers.

