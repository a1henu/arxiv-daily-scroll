---
layout: default
title: Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry
---

# Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry
**arXiv**：[2603.05450v1](https://arxiv.org/abs/2603.05450) · [PDF](https://arxiv.org/pdf/2603.05450.pdf)  
**作者**：Yifan Zhu, Mariah Bradford, Kenneth Lai, Timothy Obiso, Videep Venkatesha, James Pustejovsky, Nikhil Krishnaswamy  

**一句话要点**：提出分布式部分信息谜题以研究认知不对称下的共同基础构建

**关键词**：共同基础构建, 认知不对称, 多模态协作, 分布式部分信息谜题, 动态认知逻辑, 信念状态追踪

## 3 点简述
- 核心问题：多模态多方协作中，认知不对称导致共同基础构建困难，挑战AI系统能力。
- 方法要点：引入DPIP任务，创建多模态数据集，标注语音、手势和动作，支持命题内容和信念动态推理。
- 实验或效果：评估LLMs和基于DEL的管道，结果显示DPIP对LLMs追踪任务进展和信念状态构成挑战。

## 摘要（原文）

> Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

