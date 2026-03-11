---
layout: default
title: DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization
---

# DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization
**arXiv**：[2603.09180v1](https://arxiv.org/abs/2603.09180) · [PDF](https://arxiv.org/pdf/2603.09180.pdf)  
**作者**：Jianing Yang, Yusuke Fujita, Yui Sudo  

**一句话要点**：提出DuplexCascade以解决语音对话系统中全双工交互与LLM智能保留的平衡问题

**关键词**：全双工语音对话, 微话轮优化, 级联ASR-LLM-TTS, 流式控制令牌, 无VAD分割

## 3 点简述
- 核心问题：传统级联ASR-LLM-TTS系统依赖VAD分割导致半双工交互，而端到端模型难以维持对话智能
- 方法要点：采用无VAD的级联流式管道，将长话轮转换为微话轮交互，引入控制令牌协调流式约束下的LLM行为
- 实验或效果：在Full-DuplexBench和VoiceBench上实现开源语音对话系统中领先的全双工话轮转换和强对话智能

## 摘要（原文）

> Spoken dialog systems with cascaded ASR-LLM-TTS modules retain strong LLM intelligence, but VAD segmentation often forces half-duplex turns and brittle control. On the other hand, VAD-free end-to-end model support full-duplex interaction but is hard to maintain conversational intelligence. In this paper, we present DuplexCascade, a VAD-free cascaded streaming pipeline for full-duplex speech-to-speech dialogue. Our key idea is to convert conventional utterance-wise long turns into chunk-wise micro-turn interactions, enabling rapid bidirectional exchange while preserving the strengths of a capable text LLM. To reliably coordinate turn-taking and response timing, we introduce a set of conversational special control tokens that steer the LLM's behavior under streaming constraints. On Full-DuplexBench and VoiceBench, DuplexCascade delivers state-of-the-art full-duplex turn-taking and strong conversational intelligence among open-source speech-to-speech dialogue systems.

