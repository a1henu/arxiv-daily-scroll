---
layout: default
title: Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding
---

# Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding
**arXiv**：[2603.04977v1](https://arxiv.org/abs/2603.04977) · [PDF](https://arxiv.org/pdf/2603.04977.pdf)  
**作者**：Zheng Wang, Haoran Chen, Haoxuan Qin, Zhipeng Wei, Tianwen Qian, Cong Bai  

**一句话要点**：提出VideoHV-Agent框架，通过假设验证多智能体解决长视频理解中的语义漂移和计算冗余问题。

**关键词**：长视频理解, 假设验证框架, 多智能体系统, 视频问答, 语义漂移缓解, 计算效率优化

## 3 点简述
- 核心问题：长视频理解面临视觉冗余、长程依赖，以及链式思维和检索方法易导致语义漂移和相关性错误。
- 方法要点：基于视频摘要，采用Thinker、Judge、Verifier和Answer多智能体，将问答重构为结构化假设验证过程，先思考后验证。
- 实验或效果：在三个长视频理解基准测试中达到最先进准确率，同时提升可解释性、逻辑严谨性并降低计算成本。

## 摘要（原文）

> Long video understanding is challenging due to dense visual redundancy, long-range temporal dependencies, and the tendency of chain-of-thought and retrieval-based agents to accumulate semantic drift and correlation-driven errors. We argue that long-video reasoning should begin not with reactive retrieval, but with deliberate task formulation: the model must first articulate what must be true in the video for each candidate answer to hold. This thinking-before-finding principle motivates VideoHV-Agent, a framework that reformulates video question answering as a structured hypothesis-verification process. Based on video summaries, a Thinker rewrites answer candidates into testable hypotheses, a Judge derives a discriminative clue specifying what evidence must be checked, a Verifier grounds and tests the clue using localized, fine-grained video content, and an Answer agent integrates validated evidence to produce the final answer. Experiments on three long-video understanding benchmarks show that VideoHV-Agent achieves state-of-the-art accuracy while providing enhanced interpretability, improved logical soundness, and lower computational cost. We make our code publicly available at: https://github.com/Haorane/VideoHV-Agent.

