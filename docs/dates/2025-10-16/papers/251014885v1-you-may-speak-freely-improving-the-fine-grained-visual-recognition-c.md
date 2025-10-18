---
layout: default
title: You May Speak Freely: Improving the Fine-Grained Visual Recognition Capabilities of Multimodal Large Language Models with Answer Extraction
---

# You May Speak Freely: Improving the Fine-Grained Visual Recognition Capabilities of Multimodal Large Language Models with Answer Extraction
**arXiv**：[2510.14885v1](https://arxiv.org/abs/2510.14885) · [PDF](https://arxiv.org/pdf/2510.14885.pdf)  
**作者**：Logan Lawrence, Oindrila Saha, Megan Wei, Chen Sun, Subhransu Maji, Grant Van Horn  

**一句话要点**：提出nlg2choice方法以提升多模态大语言模型在细粒度视觉识别中的性能

**关键词**：多模态大语言模型, 细粒度视觉分类, 答案提取, 约束解码, 零样本学习

## 3 点简述
- 核心问题：多模态大语言模型在细粒度视觉分类中，处理自由形式响应和多选项问题存在挑战
- 方法要点：采用两阶段方法，先开放问答，后文本约束解码提取最可能选项
- 实验或效果：在七个细粒度视觉数据集上，分类和检索性能均得到提升

## 摘要（原文）

> Despite the renewed interest in zero-shot visual classification due to the
> rise of Multimodal Large Language Models (MLLMs), the problem of evaluating
> free-form responses of auto-regressive models remains a persistent challenge.
> Most existing works focus on language-only tasks or don't consider Multiple
> Choice Questions (MCQs) beyond 5-way options, both of which are critical
> capabilities to solve tasks in Fine-Grained Visual Classification (FGVC) where
> choice counts are in the hundreds to thousands and the choices are highly
> related. Furthermore, in this highly multi-way MCQ setting it is not clear how
> to extend LLM choice extraction to retrieval-based problems, where computing
> probabilities over the choice set is computationally costly. In this work we
> investigate nlg2choice, a simple two-stage method which first asks the MLLM an
> open-ended question for the task with minimal constraints, then uses text-only
> constrained decoding to predict the most likely choice. In retrieval settings,
> we compute the probability of the constrained response taking that choice with
> an early stopping method to significantly improve throughput. Our results show
> improvement over a suite of seven fine-grained visual datasets when evaluating
> in terms of classification and retrieval, and show that this performance holds
> over the various ways that users of LLMs can implement tasks in natural
> language.

