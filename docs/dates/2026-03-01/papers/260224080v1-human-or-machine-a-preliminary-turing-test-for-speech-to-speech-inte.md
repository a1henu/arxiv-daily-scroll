---
layout: default
title: Human or Machine? A Preliminary Turing Test for Speech-to-Speech Interaction
---

# Human or Machine? A Preliminary Turing Test for Speech-to-Speech Interaction
**arXiv**：[2602.24080v1](https://arxiv.org/abs/2602.24080) · [PDF](https://arxiv.org/pdf/2602.24080.pdf)  
**作者**：Xiang Li, Jiabao Gao, Sipei Lin, Xuan Zhou, Chi Zhang, Bo Cheng, Jiale Han, Benyou Wang  

**一句话要点**：提出首个语音对话系统图灵测试，揭示人机差距并开发细粒度评估模型

**关键词**：语音对话系统, 图灵测试, 人机相似度评估, 细粒度标注, 副语言特征, 自动评估模型

## 3 点简述
- 核心问题：语音对话系统能否通过图灵测试，实现类人对话？
- 方法要点：收集2968条人类判断，基于18个维度细粒度标注对话人机相似度。
- 实验或效果：现有系统均未通过测试，瓶颈在于副语言特征、情感表达和对话个性。

## 摘要（原文）

> The pursuit of human-like conversational agents has long been guided by the Turing test. For modern speech-to-speech (S2S) systems, a critical yet unanswered question is whether they can converse like humans. To tackle this, we conduct the first Turing test for S2S systems, collecting 2,968 human judgments on dialogues between 9 state-of-the-art S2S systems and 28 human participants. Our results deliver a clear finding: no existing evaluated S2S system passes the test, revealing a significant gap in human-likeness. To diagnose this failure, we develop a fine-grained taxonomy of 18 human-likeness dimensions and crowd-annotate our collected dialogues accordingly. Our analysis shows that the bottleneck is not semantic understanding but stems from paralinguistic features, emotional expressivity, and conversational persona. Furthermore, we find that off-the-shelf AI models perform unreliably as Turing test judges. In response, we propose an interpretable model that leverages the fine-grained human-likeness ratings and delivers accurate and transparent human-vs-machine discrimination, offering a powerful tool for automatic human-likeness evaluation. Our work establishes the first human-likeness evaluation for S2S systems and moves beyond binary outcomes to enable detailed diagnostic insights, paving the way for human-like improvements in conversational AI systems.

