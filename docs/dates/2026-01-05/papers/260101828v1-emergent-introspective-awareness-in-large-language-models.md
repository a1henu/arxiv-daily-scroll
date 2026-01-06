---
layout: default
title: Emergent Introspective Awareness in Large Language Models
---

# Emergent Introspective Awareness in Large Language Models
**arXiv**：[2601.01828v1](https://arxiv.org/abs/2601.01828) · [PDF](https://arxiv.org/pdf/2601.01828.pdf)  
**作者**：Jack Lindsey  

**一句话要点**：提出通过注入概念表征测量自报告状态的方法，以探究大语言模型的内省意识

**关键词**：内省意识, 概念注入, 自报告状态, 激活调制, 模型能力评估, 后训练策略

## 3 点简述
- 核心问题：大语言模型能否内省其内部状态，区分真实内省与虚构
- 方法要点：向模型激活中注入已知概念表征，测量其对自报告状态的影响
- 实验或效果：模型能识别注入概念，回忆先前意图，区分自身输出与人工预填充

## 摘要（原文）

> We investigate whether large language models can introspect on their internal states. It is difficult to answer this question through conversation alone, as genuine introspection cannot be distinguished from confabulations. Here, we address this challenge by injecting representations of known concepts into a model's activations, and measuring the influence of these manipulations on the model's self-reported states. We find that models can, in certain scenarios, notice the presence of injected concepts and accurately identify them. Models demonstrate some ability to recall prior internal representations and distinguish them from raw text inputs. Strikingly, we find that some models can use their ability to recall prior intentions in order to distinguish their own outputs from artificial prefills. In all these experiments, Claude Opus 4 and 4.1, the most capable models we tested, generally demonstrate the greatest introspective awareness; however, trends across models are complex and sensitive to post-training strategies. Finally, we explore whether models can explicitly control their internal representations, finding that models can modulate their activations when instructed or incentivized to "think about" a concept. Overall, our results indicate that current language models possess some functional introspective awareness of their own internal states. We stress that in today's models, this capacity is highly unreliable and context-dependent; however, it may continue to develop with further improvements to model capabilities.

