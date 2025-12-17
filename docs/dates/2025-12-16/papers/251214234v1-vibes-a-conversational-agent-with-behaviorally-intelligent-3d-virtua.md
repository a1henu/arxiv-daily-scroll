---
layout: default
title: ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
---

# ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
**arXiv**：[2512.14234v1](https://arxiv.org/abs/2512.14234) · [PDF](https://arxiv.org/pdf/2512.14234.pdf)  
**作者**：Juze Zhang, Changan Chen, Xin Chen, Heng Yu, Tiange Xiang, Ali Sartaz Khan, Shrinidhi K. Lakshmikanth, Ehsan Adeli  

**一句话要点**：提出ViBES模型，通过多模态专家混合架构实现对话中语言与身体动作的联合规划，以增强3D虚拟代理的社会交互能力。

**关键词**：多模态对话代理, 语音-语言-行为模型, 多模态专家混合, 3D虚拟身体, 社会交互, 联合规划

## 3 点简述
- 核心问题：现有系统将人类行为建模为固定话语到动作的翻译任务，导致时序脆弱、社会基础弱和多模态堆栈碎片化。
- 方法要点：采用语音-语言-行为模型，基于多模态专家混合架构，通过跨专家注意力共享信息，支持混合主动交互。
- 实验或效果：在多轮对话基准测试中，在对话-动作对齐和行为质量指标上优于强基线，实现可控的社会化3D交互。

## 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at: ai.stanford.edu/~juze/ViBES/

