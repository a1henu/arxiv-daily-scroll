---
layout: default
title: Linear representations in language models can change dramatically over a conversation
---

# Linear representations in language models can change dramatically over a conversation
**arXiv**：[2601.20834v1](https://arxiv.org/abs/2601.20834) · [PDF](https://arxiv.org/pdf/2601.20834.pdf)  
**作者**：Andrew Kyle Lampinen, Yuxuan Li, Eghbal Hosseini, Sangnie Bhardwaj, Murray Shanahan  

**一句话要点**：揭示语言模型线性表示在对话中动态变化，挑战静态解释与操控

**关键词**：语言模型表示, 对话动态, 可解释性, 事实性表示, 模型适应, 线性探测

## 3 点简述
- 研究语言模型线性表示在对话中的动态演化，发现事实性等概念表示可剧烈变化
- 通过模拟对话实验，证明变化内容依赖且跨模型稳健，但非策略对话也能引发
- 表示变化影响可解释性与操控，需动态视角，为模型适应上下文研究提供新方向

## 摘要（原文）

> Language model representations often contain linear directions that correspond to high-level concepts. Here, we study the dynamics of these representations: how representations evolve along these dimensions within the context of (simulated) conversations. We find that linear representations can change dramatically over a conversation; for example, information that is represented as factual at the beginning of a conversation can be represented as non-factual at the end and vice versa. These changes are content-dependent; while representations of conversation-relevant information may change, generic information is generally preserved. These changes are robust even for dimensions that disentangle factuality from more superficial response patterns, and occur across different model families and layers of the model. These representation changes do not require on-policy conversations; even replaying a conversation script written by an entirely different model can produce similar changes. However, adaptation is much weaker from simply having a sci-fi story in context that is framed more explicitly as such. We also show that steering along a representational direction can have dramatically different effects at different points in a conversation. These results are consistent with the idea that representations may evolve in response to the model playing a particular role that is cued by a conversation. Our findings may pose challenges for interpretability and steering -- in particular, they imply that it may be misleading to use static interpretations of features or directions, or probes that assume a particular range of features consistently corresponds to a particular ground-truth value. However, these types of representational dynamics also point to exciting new research directions for understanding how models adapt to context.

