---
layout: default
title: Understanding Multi-Agent Reasoning with Large Language Models for Cartoon VQA
---

# Understanding Multi-Agent Reasoning with Large Language Models for Cartoon VQA
**arXiv**：[2601.03073v1](https://arxiv.org/abs/2601.03073) · [PDF](https://arxiv.org/pdf/2601.03073.pdf)  
**作者**：Tong Wu, Thanet Markchom  

**一句话要点**：提出多智能体大语言模型框架以解决卡通视觉问答中的视觉抽象与叙事推理挑战

**关键词**：卡通视觉问答, 多智能体推理, 大语言模型, 视觉抽象, 叙事上下文, 结构化推理

## 3 点简述
- 核心问题：卡通图像VQA面临视觉抽象夸张和叙事驱动上下文理解不足的挑战
- 方法要点：设计视觉、语言和批评三个智能体协作，整合视觉线索与叙事上下文进行结构化推理
- 实验或效果：在Pororo和Simpsons数据集上评估，分析各智能体对预测的贡献，深化对多智能体行为的理解

## 摘要（原文）

> Visual Question Answering (VQA) for stylised cartoon imagery presents challenges, such as interpreting exaggerated visual abstraction and narrative-driven context, which are not adequately addressed by standard large language models (LLMs) trained on natural images. To investigate this issue, a multi-agent LLM framework is introduced, specifically designed for VQA tasks in cartoon imagery. The proposed architecture consists of three specialised agents: visual agent, language agent and critic agent, which work collaboratively to support structured reasoning by integrating visual cues and narrative context. The framework was systematically evaluated on two cartoon-based VQA datasets: Pororo and Simpsons. Experimental results provide a detailed analysis of how each agent contributes to the final prediction, offering a deeper understanding of LLM-based multi-agent behaviour in cartoon VQA and multimodal inference.

