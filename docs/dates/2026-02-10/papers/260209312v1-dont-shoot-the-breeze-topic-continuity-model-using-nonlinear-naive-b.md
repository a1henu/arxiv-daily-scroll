---
layout: default
title: Don't Shoot The Breeze: Topic Continuity Model Using Nonlinear Naive Bayes With Attention
---

# Don't Shoot The Breeze: Topic Continuity Model Using Nonlinear Naive Bayes With Attention
**arXiv**：[2602.09312v1](https://arxiv.org/abs/2602.09312) · [PDF](https://arxiv.org/pdf/2602.09312.pdf)  
**作者**：Shu-Ting Pi, Pradeep Bagavan, Yejia Li, Disha, Qun Liu  

**一句话要点**：提出基于非线性朴素贝叶斯与注意力机制的主题连续性模型，以评估LLM聊天机器人响应是否保持对话主题。

**关键词**：主题连续性模型, 非线性朴素贝叶斯, 注意力机制, LLM聊天机器人, 可解释NLU

## 3 点简述
- 核心问题：LLM聊天机器人中主题突变导致用户体验差和计算资源浪费。
- 方法要点：扩展NLU模型为可量化公式，引入注意力机制和对数非线性增强主题连续性捕捉。
- 实验或效果：模型在长复杂对话中优于传统方法，具有线性时间复杂度和可解释性。

## 摘要（原文）

> Utilizing Large Language Models (LLM) as chatbots in diverse business scenarios often presents the challenge of maintaining topic continuity. Abrupt shifts in topics can lead to poor user experiences and inefficient utilization of computational resources. In this paper, we present a topic continuity model aimed at assessing whether a response aligns with the initial conversation topic. Our model is built upon the expansion of the corresponding natural language understanding (NLU) model into quantifiable terms using a Naive Bayes approach. Subsequently, we have introduced an attention mechanism and logarithmic nonlinearity to enhance its capability to capture topic continuity. This approach allows us to convert the NLU model into an interpretable analytical formula. In contrast to many NLU models constrained by token limits, our proposed model can seamlessly handle conversations of any length with linear time complexity. Furthermore, the attention mechanism significantly improves the model's ability to identify topic continuity in complex conversations. According to our experiments, our model consistently outperforms traditional methods, particularly in handling lengthy and intricate conversations. This unique capability offers us an opportunity to ensure the responsible and interpretable use of LLMs.

