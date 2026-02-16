---
layout: default
title: ADEPT: RL-Aligned Agentic Decoding of Emotion via Evidence Probing Tools -- From Consensus Learning to Ambiguity-Driven Emotion Reasoning
---

# ADEPT: RL-Aligned Agentic Decoding of Emotion via Evidence Probing Tools -- From Consensus Learning to Ambiguity-Driven Emotion Reasoning
**arXiv**：[2602.12714v1](https://arxiv.org/abs/2602.12714) · [PDF](https://arxiv.org/pdf/2602.12714.pdf)  
**作者**：Esther Sun, Bo-Hao Su, Abinay Reddy Naini, Shinji Watanabe, Carlos Busso  

**一句话要点**：提出ADEPT框架，通过多轮证据探测工具解决语音大语言模型在情感推理中缺乏可验证声学证据的问题。

**关键词**：情感识别, 语音大语言模型, 证据探测工具, 多轮推理, 声学证据, 强化学习对齐

## 3 点简述
- 核心问题：语音大语言模型在情感推理中常产生无根据、文本偏见的判断，缺乏可验证声学证据。
- 方法要点：将情感识别重构为多轮查询过程，使用语义和声学探测工具进行候选生成、证据收集和裁决。
- 实验或效果：在多数设置中提升主要情感准确性，显著改善次要情感表征，并生成基于可审计证据的解释。

## 摘要（原文）

> Speech Large Language Models (SLLMs) enable high-level emotion reasoning but often produce ungrounded, text-biased judgments without verifiable acoustic evidence. In contrast, self-supervised speech encoders such as WavLM provide strong acoustic representations yet remain opaque discriminative models with limited interpretability. To bridge this gap, we introduce ADEPT (Agentic Decoding of Emotion via Evidence Probing Tools), a framework that reframes emotion recognition as a multi-turn inquiry process rather than a single-pass prediction. ADEPT transforms an SLLM into an agent that maintains an evolving candidate emotion set and adaptively invokes dedicated semantic and acoustic probing tools within a structured pipeline of candidate generation, evidence collection, and adjudication. Crucially, ADEPT enables a paradigm shift from consensus learning to ambiguity-driven emotion reasoning. Since human affect exhibits inherent complexity and frequent co-occurrence of emotions, we treat minority annotations as informative perceptual signals rather than discarding them as noise. Finally, we integrate Group Relative Policy Optimization (GRPO) with an Evidence Trust Gate to explicitly couple tool-usage behaviors with prediction quality and enforce evidence-grounded reasoning. Experiments show that ADEPT improves primary emotion accuracy in most settings while substantially improving minor emotion characterization, producing explanations grounded in auditable acoustic and semantic evidence.

