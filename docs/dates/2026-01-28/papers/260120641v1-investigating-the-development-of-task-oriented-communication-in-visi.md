---
layout: default
title: Investigating the Development of Task-Oriented Communication in Vision-Language Models
---

# Investigating the Development of Task-Oriented Communication in Vision-Language Models
**arXiv**：[2601.20641v1](https://arxiv.org/abs/2601.20641) · [PDF](https://arxiv.org/pdf/2601.20641.pdf)  
**作者**：Boaz Carmeli, Orr Paradise, Shafi Goldwasser, Yonatan Belinkov, Ron Meir  

**一句话要点**：研究视觉语言模型在协作推理任务中发展高效且隐蔽的任务导向通信协议

**关键词**：任务导向通信, 视觉语言模型, 指称游戏, 通信效率, 隐蔽协议, 协作推理

## 3 点简述
- 核心问题：探究LLM代理能否发展出不同于自然语言的任务导向通信协议，关注效率和隐蔽性
- 方法要点：使用指称游戏框架，在视觉语言模型代理间进行通信，以评估语言变体
- 实验或效果：实验显示视觉语言模型能发展出有效、任务适应的通信模式，并可能形成难以解释的隐蔽协议

## 摘要（原文）

> We investigate whether \emph{LLM-based agents} can develop task-oriented communication protocols that differ from standard natural language in collaborative reasoning tasks. Our focus is on two core properties such task-oriented protocols may exhibit: Efficiency -- conveying task-relevant information more concisely than natural language, and Covertness -- becoming difficult for external observers to interpret, raising concerns about transparency and control. To investigate these aspects, we use a referential-game framework in which vision-language model (VLM) agents communicate, providing a controlled, measurable setting for evaluating language variants. Experiments show that VLMs can develop effective, task-adapted communication patterns. At the same time, they can develop covert protocols that are difficult for humans and external agents to interpret. We also observe spontaneous coordination between similar models without explicitly shared protocols. These findings highlight both the potential and the risks of task-oriented communication, and position referential games as a valuable testbed for future work in this area.

