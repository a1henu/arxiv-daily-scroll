---
layout: default
title: Causality Elicitation from Large Language Models
---

# Causality Elicitation from Large Language Models
**arXiv**：[2603.04276v1](https://arxiv.org/abs/2603.04276) · [PDF](https://arxiv.org/pdf/2603.04276.pdf)  
**作者**：Takashi Kameyama, Masahiro Kato, Yasuko Hio, Yasushi Takano, Naoto Minakawa  

**一句话要点**：提出从大型语言模型中提取因果关系的流程，以生成可检查的因果假设集。

**关键词**：大型语言模型, 因果关系提取, 因果发现, 事件分组, 文档采样, 假设生成

## 3 点简述
- 核心问题：如何从大型语言模型中提取因果知识，而不保证真实世界因果关系。
- 方法要点：通过采样文档、提取事件、分组为规范事件、构建指示向量，并应用因果发现方法。
- 实验或效果：提供框架以呈现大型语言模型可能假设的因果假设集，作为可检查的变量和候选图。

## 摘要（原文）

> Large language models (LLMs) are trained on enormous amounts of data and encode knowledge in their parameters. We propose a pipeline to elicit causal relationships from LLMs. Specifically, (i) we sample many documents from LLMs on a given topic, (ii) we extract an event list from from each document, (iii) we group events that appear across documents into canonical events, (iv) we construct a binary indicator vector for each document over canonical events, and (v) we estimate candidate causal graphs using causal discovery methods. Our approach does not guarantee real-world causality. Rather, it provides a framework for presenting the set of causal hypotheses that LLMs can plausibly assume, as an inspectable set of variables and candidate graphs.

