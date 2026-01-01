---
layout: default
title: Modeling Language as a Sequence of Thoughts
---

# Modeling Language as a Sequence of Thoughts
**arXiv**：[2512.25026v1](https://arxiv.org/abs/2512.25026) · [PDF](https://arxiv.org/pdf/2512.25026.pdf)  
**作者**：Nasim Borazjanizadeh, James McClelland  

**一句话要点**：提出Thought Gestalt模型，通过双层次抽象建模语言以提升Transformer的全局一致性和效率

**关键词**：语言建模, Transformer模型, 思想表示, 循环神经网络, 关系方向泛化, 数据效率

## 3 点简述
- 核心问题：Transformer语言模型依赖表层共现统计，缺乏全局一致的实体和事件表示，导致关系方向泛化错误和上下文错误
- 方法要点：引入循环Transformer，在token和句子级'思想'状态两个抽象层次建模语言，通过跨注意力记忆先前句子表示
- 实验或效果：在扩展实验中，TG相比GPT-2基线提高效率，减少关系方向泛化错误，拟合显示GPT-2需更多数据和参数匹配TG损失

## 摘要（原文）

> Transformer language models can generate strikingly natural text by modeling language as a sequence of tokens. Yet, by relying primarily on surface-level co-occurrence statistics, they fail to form globally consistent latent representations of entities and events, lack of which contributes to brittleness in relational direction (e.g., reversal curse), contextualization errors, and data inefficiency. On the other hand, cognitive science shows that human comprehension involves converting the input linguistic stream into compact, event-like representations that persist in memory while verbatim form is short-lived. Motivated by this view, we introduce Thought Gestalt (TG) model, a recurrent Transformer that models language at two levels of abstraction - tokens and sentence-level "thought" states. TG generates the tokens of one sentence at a time while cross-attending to a memory of prior sentence representations. In TG, token and sentence representations are generated using the same set of model parameters and trained with a single objective, the next-token cross-entropy: by retaining the computation graph of sentence representations written to memory, gradients from future token losses flow backward through cross-attention to optimize the parameters generating earlier sentence vectors. In scaling experiments, TG consistently improves efficiency over matched GPT-2 runs, among other baselines, with scaling fits indicating GPT-2 requires ~5-8% more data and ~33-42% more parameters to match TG's loss. TG also reduces errors on relational direction generalization on a father-son reversal curse probe.

