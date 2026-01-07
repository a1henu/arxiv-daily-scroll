---
layout: default
title: Image, Word and Thought: A More Challenging Language Task for the Iterated Learning Model
---

# Image, Word and Thought: A More Challenging Language Task for the Iterated Learning Model
**arXiv**：[2601.02911v1](https://arxiv.org/abs/2601.02911) · [PDF](https://arxiv.org/pdf/2601.02911.pdf)  
**作者**：Hyoyeon Lee, Seth Bullock, Conor Houghton  

**一句话要点**：提出半监督迭代学习模型，应用于七段显示图像任务，实现表达性、组合性和稳定性语言传输。

**关键词**：迭代学习模型, 语言传输, 半监督学习, 自编码器, 七段显示图像, 语言涌现

## 3 点简述
- 核心问题：迭代学习模型如何模拟复杂含义（如图像）的语言传输，以探索语言结构的涌现。
- 方法要点：结合监督与无监督学习的半监督迭代学习模型，使用自编码器架构处理大规模含义-信号空间。
- 实验或效果：模型成功应用于七段显示图像任务，代理学习并传输表达性、组合性和稳定的语言。

## 摘要（原文）

> The iterated learning model simulates the transmission of language from generation to generation in order to explore how the constraints imposed by language transmission facilitate the emergence of language structure. Despite each modelled language learner starting from a blank slate, the presence of a bottleneck limiting the number of utterances to which the learner is exposed can lead to the emergence of language that lacks ambiguity, is governed by grammatical rules, and is consistent over successive generations, that is, one that is expressive, compositional and stable. The recent introduction of a more computationally tractable and ecologically valid semi supervised iterated learning model, combining supervised and unsupervised learning within an autoencoder architecture, has enabled exploration of language transmission dynamics for much larger meaning-signal spaces. Here, for the first time, the model has been successfully applied to a language learning task involving the communication of much more complex meanings: seven-segment display images. Agents in this model are able to learn and transmit a language that is expressive: distinct codes are employed for all 128 glyphs; compositional: signal components consistently map to meaning components, and stable: the language does not change from generation to generation.

