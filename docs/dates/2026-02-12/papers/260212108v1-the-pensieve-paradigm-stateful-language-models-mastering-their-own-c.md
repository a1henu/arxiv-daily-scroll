---
layout: default
title: The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context
---

# The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context
**arXiv**：[2602.12108v1](https://arxiv.org/abs/2602.12108) · [PDF](https://arxiv.org/pdf/2602.12108.pdf)  
**作者**：Xiaoyuan Liu, Tian Liang, Dongyang Ma, Deyu Zhou, Haitao Mi, Pinjia He, Yan Wang  

**一句话要点**：提出StateLM以解决大语言模型被动依赖固定上下文的问题，使其能主动管理状态。

**关键词**：状态感知模型, 上下文管理, 长文档问答, 记忆工具, 推理循环

## 3 点简述
- 核心问题：大语言模型缺乏主动管理上下文的能力，受限于固定窗口架构。
- 方法要点：引入内部推理循环和记忆工具，训练模型动态优化自身上下文。
- 实验或效果：在长文档QA、聊天记忆和深度研究任务中，性能显著超越标准大语言模型。

## 摘要（原文）

> In the world of Harry Potter, when Dumbledore's mind is overburdened, he extracts memories into a Pensieve to be revisited later. In the world of AI, while we possess the Pensieve-mature databases and retrieval systems, our models inexplicably lack the "wand" to operate it. They remain like a Dumbledore without agency, passively accepting a manually engineered context as their entire memory. This work finally places the wand in the model's hand. We introduce StateLM, a new class of foundation models endowed with an internal reasoning loop to manage their own state. We equip our model with a suite of memory tools, such as context pruning, document indexing, and note-taking, and train it to actively manage these tools. By learning to dynamically engineering its own context, our model breaks free from the architectural prison of a fixed window. Experiments across various model sizes demonstrate StateLM's effectiveness across diverse scenarios. On long-document QA tasks, StateLMs consistently outperform standard LLMs across all model scales; on the chat memory task, they achieve absolute accuracy improvements of 10% to 20% over standard LLMs. On the deep research task BrowseComp-Plus, the performance gap becomes even more pronounced: StateLM achieves up to 52% accuracy, whereas standard LLM counterparts struggle around 5%. Ultimately, our approach shifts LLMs from passive predictors to state-aware agents where reasoning becomes a stateful and manageable process.

