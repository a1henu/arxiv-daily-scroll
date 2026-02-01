---
layout: default
title: Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding
---

# Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding
**arXiv**：[2601.21969v1](https://arxiv.org/abs/2601.21969) · [PDF](https://arxiv.org/pdf/2601.21969.pdf)  
**作者**：Yifan Zhu, Huiqiang Rong, Haoran Luo  

**一句话要点**：提出Token-Guard，通过自检解码实现令牌级幻觉控制，提升大语言模型生成可靠性。

**关键词**：幻觉控制, 自检解码, 令牌级生成, 大语言模型, 可靠性提升

## 3 点简述
- 核心问题：大语言模型常产生幻觉，现有解码方法缺乏显式控制。
- 方法要点：基于自检解码，在推理步骤进行内部验证和潜在空间风险评分。
- 实验效果：在HALU数据集上显著减少幻觉，提高生成准确性。

## 摘要（原文）

> Large Language Models (LLMs) often hallucinate, generating content inconsistent with the input. Retrieval-Augmented Generation (RAG) and Reinforcement Learning with Human Feedback (RLHF) can mitigate hallucinations but require resource-intensive retrieval or large-scale fine-tuning. Decoding-based methods are lighter yet lack explicit hallucination control. To address this, we present Token-Guard, a token-level hallucination control method based on self-checking decoding. Token-Guard performs internal verification at each reasoning step to detect hallucinated tokens before they propagate. Candidate fragments are further evaluated in a latent space with explicit hallucination risk scoring, while iterative pruning and regeneration dynamically correct detected errors. Experiments on HALU datasets show Token-Guard substantially reduces hallucinations and improves generation accuracy, offering a scalable, modular solution for reliable LLM outputs. Our code is publicly available.

