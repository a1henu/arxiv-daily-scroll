---
layout: default
title: Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding
---

# Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding
**arXiv**：[2601.21969v1](https://arxiv.org/abs/2601.21969) · [PDF](https://arxiv.org/pdf/2601.21969.pdf)  
**作者**：Yifan Zhu, Huiqiang Rong, Haoran Luo  

**一句话要点**：提出Token-Guard，通过自检解码实现令牌级幻觉控制以提升LLM生成可靠性

**关键词**：幻觉控制, 自检解码, 令牌级验证, 潜在空间评分, 动态修剪, LLM可靠性

## 3 点简述
- 核心问题：LLM常产生幻觉，现有解码方法缺乏显式控制，资源消耗大
- 方法要点：基于自检解码，在推理步骤进行内部验证和潜在空间风险评分，动态修剪与再生
- 实验或效果：在HALU数据集上显著减少幻觉，提高生成准确性，提供可扩展模块化方案

## 摘要（原文）

> Large Language Models (LLMs) often hallucinate, generating content inconsistent with the input. Retrieval-Augmented Generation (RAG) and Reinforcement Learning with Human Feedback (RLHF) can mitigate hallucinations but require resource-intensive retrieval or large-scale fine-tuning. Decoding-based methods are lighter yet lack explicit hallucination control. To address this, we present Token-Guard, a token-level hallucination control method based on self-checking decoding. Token-Guard performs internal verification at each reasoning step to detect hallucinated tokens before they propagate. Candidate fragments are further evaluated in a latent space with explicit hallucination risk scoring, while iterative pruning and regeneration dynamically correct detected errors. Experiments on HALU datasets show Token-Guard substantially reduces hallucinations and improves generation accuracy, offering a scalable, modular solution for reliable LLM outputs. Our code is publicly available.

