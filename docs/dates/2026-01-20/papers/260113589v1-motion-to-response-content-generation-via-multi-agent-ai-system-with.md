---
layout: default
title: Motion-to-Response Content Generation via Multi-Agent AI System with Real-Time Safety Verification
---

# Motion-to-Response Content Generation via Multi-Agent AI System with Real-Time Safety Verification
**arXiv**：[2601.13589v1](https://arxiv.org/abs/2601.13589) · [PDF](https://arxiv.org/pdf/2601.13589.pdf)  
**作者**：HyeYoung Lee  

**一句话要点**：提出基于多智能体AI系统的实时安全内容生成方法，用于音频情感驱动的响应媒体内容生成。

**关键词**：多智能体系统, 实时内容生成, 安全验证, 情感识别, 模块化架构

## 3 点简述
- 核心问题：传统语音情感识别研究侧重于分类精度，缺乏将情感状态转化为安全、可控响应内容的方法。
- 方法要点：采用四智能体协作架构，包括情感识别、响应策略决策、内容参数生成和安全验证，实现实时内容生成与安全过滤。
- 实验或效果：在公共数据集上，系统达到73.2%情感识别准确率、89.4%响应模式一致性和100%安全合规，推理延迟低于100毫秒。

## 摘要（原文）

> This paper proposes a multi-agent artificial intelligence system that generates response-oriented media content in real time based on audio-derived emotional signals. Unlike conventional speech emotion recognition studies that focus primarily on classification accuracy, our approach emphasizes the transformation of inferred emotional states into safe, age-appropriate, and controllable response content through a structured pipeline of specialized AI agents. The proposed system comprises four cooperative agents: (1) an Emotion Recognition Agent with CNN-based acoustic feature extraction, (2) a Response Policy Decision Agent for mapping emotions to response modes, (3) a Content Parameter Generation Agent for producing media control parameters, and (4) a Safety Verification Agent enforcing age-appropriateness and stimulation constraints. We introduce an explicit safety verification loop that filters generated content before output, ensuring compliance with predefined rules. Experimental results on public datasets demonstrate that the system achieves 73.2% emotion recognition accuracy, 89.4% response mode consistency, and 100% safety compliance while maintaining sub-100ms inference latency suitable for on-device deployment. The modular architecture enables interpretability and extensibility, making it applicable to child-adjacent media, therapeutic applications, and emotionally responsive smart devices.

