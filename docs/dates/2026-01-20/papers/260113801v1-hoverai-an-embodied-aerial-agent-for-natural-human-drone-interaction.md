---
layout: default
title: HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction
---

# HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction
**arXiv**：[2601.13801v1](https://arxiv.org/abs/2601.13801) · [PDF](https://arxiv.org/pdf/2601.13801.pdf)  
**作者**：Yuhua Jin, Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Fawad Mehboob, Issatay Tokmurziyev, Miguel Altamirano Cabrera, Muhammad Ahsan Mustafa, Dzmitry Tsetserukou  

**一句话要点**：提出HoverAI以解决无人机在人居环境中意图传达不足的问题，通过集成移动性、视觉投影和对话AI实现自然交互。

**关键词**：无人机交互, 多模态AI, 视觉投影, 对话系统, 空间感知, 人机交互

## 3 点简述
- 核心问题：无人机在人居环境中因通信机制不足导致意图不明确，影响交互安全与效率。
- 方法要点：结合无人机移动、MEMS激光投影和实时对话AI，通过多模态管道处理视觉与语音输入，生成自适应唇形同步的虚拟形象响应。
- 实验或效果：评估显示高准确度的命令识别（F1: 0.90）、人口统计估计（性别F1: 0.89，年龄MAE: 5.14年）和语音转录（WER: 0.181）。

## 摘要（原文）

> Drones operating in human-occupied spaces suffer from insufficient communication mechanisms that create uncertainty about their intentions. We present HoverAI, an embodied aerial agent that integrates drone mobility, infrastructure-independent visual projection, and real-time conversational AI into a unified platform. Equipped with a MEMS laser projector, onboard semi-rigid screen, and RGB camera, HoverAI perceives users through vision and voice, responding via lip-synced avatars that adapt appearance to user demographics. The system employs a multimodal pipeline combining VAD, ASR (Whisper), LLM-based intent classification, RAG for dialogue, face analysis for personalization, and voice synthesis (XTTS v2). Evaluation demonstrates high accuracy in command recognition (F1: 0.90), demographic estimation (gender F1: 0.89, age MAE: 5.14 years), and speech transcription (WER: 0.181). By uniting aerial robotics with adaptive conversational AI and self-contained visual output, HoverAI introduces a new class of spatially-aware, socially responsive embodied agents for applications in guidance, assistance, and human-centered interaction.

