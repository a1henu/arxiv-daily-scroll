---
layout: default
title: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
---

# Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
**arXiv**：[2512.17183v1](https://arxiv.org/abs/2512.17183) · [PDF](https://arxiv.org/pdf/2512.17183.pdf)  
**作者**：Gang Zhang  

**一句话要点**：提出端到端框架以合成语义共语音手势并实时部署于人形机器人

**关键词**：语义手势合成, 人形机器人控制, 实时部署, 生成检索机制, 模仿学习, 运动重定向

## 3 点简述
- 核心问题：为人形机器人创建自然、表达性的非语言通信，解决语义手势生成与物理控制挑战。
- 方法要点：集成基于大语言模型的生成检索机制和自回归Motion-GPT模型，结合高保真模仿学习控制策略MotionTracker。
- 实验或效果：通过综合评估，系统生成语义恰当、节奏连贯的手势，并在Unitree G1机器人上准确执行，实现实时部署。

## 摘要（原文）

> We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

