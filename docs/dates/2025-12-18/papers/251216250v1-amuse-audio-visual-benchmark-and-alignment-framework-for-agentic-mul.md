---
layout: default
title: AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding
---

# AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding
**arXiv**：[2512.16250v1](https://arxiv.org/abs/2512.16250) · [PDF](https://arxiv.org/pdf/2512.16250.pdf)  
**作者**：Sanjoy Chowdhury, Karren D. Yang, Xudong Liu, Fartash Faghri, Pavan Kumar Anasosalu Vasu, Oncel Tuzel, Dinesh Manocha, Chun-Liang Li, Raviteja Vemulapalli  

**一句话要点**：提出AMUSE基准与RAFT框架以提升多模态模型在多说话者音频-视频场景中的代理推理能力

**关键词**：多模态大语言模型, 音频-视频理解, 多说话者对话, 代理推理, 基准评估, 对齐框架

## 3 点简述
- 核心问题：当前MLLMs在多说话者对话场景中代理推理能力弱，难以跟踪说话者、维持角色和跨时间接地事件
- 方法要点：AMUSE基准设计代理性任务，RAFT框架结合奖励优化与多模态自评估进行数据高效对齐
- 实验或效果：使用RAFT在AMUSE基准上实现最高39.52%的相对准确率提升

## 摘要（原文）

> Recent multimodal large language models (MLLMs) such as GPT-4o and Qwen3-Omni show strong perception but struggle in multi-speaker, dialogue-centric settings that demand agentic reasoning tracking who speaks, maintaining roles, and grounding events across time. These scenarios are central to multimodal audio-video understanding, where models must jointly reason over audio and visual streams in applications such as conversational video assistants and meeting analytics. We introduce AMUSE, a benchmark designed around tasks that are inherently agentic, requiring models to decompose complex audio-visual interactions into planning, grounding, and reflection steps. It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families, including spatio-temporal speaker grounding and multimodal dialogue summarization. Across all modes, current models exhibit weak multi-speaker reasoning and inconsistent behavior under both non-agentic and agentic evaluation. Motivated by the inherently agentic nature of these tasks and recent advances in LLM agents, we propose RAFT, a data-efficient agentic alignment framework that integrates reward optimization with intrinsic multimodal self-evaluation as reward and selective parameter adaptation for data and parameter efficient updates. Using RAFT, we achieve up to 39.52\% relative improvement in accuracy on our benchmark. Together, AMUSE and RAFT provide a practical platform for examining agentic reasoning in multimodal models and improving their capabilities.

