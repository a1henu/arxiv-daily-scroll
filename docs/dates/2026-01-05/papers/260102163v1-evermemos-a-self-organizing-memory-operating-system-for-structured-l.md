---
layout: default
title: EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning
---

# EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning
**arXiv**：[2601.02163v1](https://arxiv.org/abs/2601.02163) · [PDF](https://arxiv.org/pdf/2601.02163.pdf)  
**作者**：Chuanrui Hu, Xingze Gao, Zuyi Zhou, Dannong Xu, Yi Bai, Xintong Li, Hui Zhang, Tong Li, Chong Zhang, Lidong Bing, Yafeng Deng  

**一句话要点**：提出EverMemOS自组织记忆操作系统，以解决大语言模型在长期交互中上下文窗口有限的问题。

**关键词**：自组织记忆系统, 长期推理, 记忆增强, 用户画像, 前瞻信号, 大语言模型代理

## 3 点简述
- 核心问题：大语言模型在长期交互中因上下文窗口有限，难以维持连贯行为。
- 方法要点：通过情景痕迹形成、语义整合和重构回忆，实现记忆的自组织生命周期管理。
- 实验或效果：在LoCoMo和LongMemEval上达到最先进性能，支持用户画像和前瞻能力。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed as long-term interactive agents, yet their limited context windows make it difficult to sustain coherent behavior over extended interactions. Existing memory systems often store isolated records and retrieve fragments, limiting their ability to consolidate evolving user states and resolve conflicts. We introduce EverMemOS, a self-organizing memory operating system that implements an engram-inspired lifecycle for computational memory. Episodic Trace Formation converts dialogue streams into MemCells that capture episodic traces, atomic facts, and time-bounded Foresight signals. Semantic Consolidation organizes MemCells into thematic MemScenes, distilling stable semantic structures and updating user profiles. Reconstructive Recollection performs MemScene-guided agentic retrieval to compose the necessary and sufficient context for downstream reasoning. Experiments on LoCoMo and LongMemEval show that EverMemOS achieves state-of-the-art performance on memory-augmented reasoning tasks. We further report a profile study on PersonaMem v2 and qualitative case studies illustrating chat-oriented capabilities such as user profiling and Foresight. Code is available at https://github.com/EverMind-AI/EverMemOS.

