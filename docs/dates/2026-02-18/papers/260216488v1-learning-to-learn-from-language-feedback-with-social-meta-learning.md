---
layout: default
title: Learning to Learn from Language Feedback with Social Meta-Learning
---

# Learning to Learn from Language Feedback with Social Meta-Learning
**arXiv**：[2602.16488v1](https://arxiv.org/abs/2602.16488) · [PDF](https://arxiv.org/pdf/2602.16488.pdf)  
**作者**：Jonathan Cook, Diego Antognini, Martin Klissarov, Claudiu Musat, Edward Grefenstette  

**一句话要点**：提出社会元学习微调方法，使大语言模型在对话中主动寻求并利用语言反馈以解决复杂任务。

**关键词**：社会元学习, 语言反馈学习, 对话适应性, 任务泛化, 微调方法

## 3 点简述
- 核心问题：大语言模型在对话中难以主动学习和利用纠正反馈，导致对话静态且缺乏适应性。
- 方法要点：基于人类社会元学习，通过模拟教学对话微调模型，将静态任务转化为交互式社交学习问题。
- 实验或效果：模型在数学和编码任务上泛化能力强，能更好地处理信息不明确的任务，减少过早回答并主动询问信息。

## 摘要（原文）

> Large language models (LLMs) often struggle to learn from corrective feedback within a conversational context. They are rarely proactive in soliciting this feedback, even when faced with ambiguity, which can make their dialogues feel static, one-sided, and lacking the adaptive qualities of human conversation. To address these limitations, we draw inspiration from social meta-learning (SML) in humans - the process of learning how to learn from others. We formulate SML as a finetuning methodology, training LLMs to solicit and learn from language feedback in simulated pedagogical dialogues, where static tasks are converted into interactive social learning problems. SML effectively teaches models to use conversation to solve problems they are unable to solve in a single turn. This capability generalises across domains; SML on math problems produces models that better use feedback to solve coding problems and vice versa. Furthermore, despite being trained only on fully-specified problems, these models are better able to solve underspecified tasks where critical information is revealed over multiple turns. When faced with this ambiguity, SML-trained models make fewer premature answer attempts and are more likely to ask for the information they need. This work presents a scalable approach to developing AI systems that effectively learn from language feedback.

