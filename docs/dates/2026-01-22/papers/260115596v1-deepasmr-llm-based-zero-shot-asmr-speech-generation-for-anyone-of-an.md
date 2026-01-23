---
layout: default
title: DeepASMR: LLM-Based Zero-Shot ASMR Speech Generation for Anyone of Any Voice
---

# DeepASMR: LLM-Based Zero-Shot ASMR Speech Generation for Anyone of Any Voice
**arXiv**：[2601.15596v1](https://arxiv.org/abs/2601.15596) · [PDF](https://arxiv.org/pdf/2601.15596.pdf)  
**作者**：Leying Zhang, Tingxiao Zhou, Haiyang Sun, Mengxiao Bi, Yanmin Qian  

**一句话要点**：提出DeepASMR框架，实现基于LLM的零样本ASMR语音生成，适用于任意说话人

**关键词**：零样本语音生成, ASMR合成, LLM编码, 流匹配解码, 多说话人语料库, 语音风格分离

## 3 点简述
- 核心问题：现有TTS系统难以生成低强度、非浊音的ASMR语音，且需零样本说话人适应
- 方法要点：利用离散语音令牌分离风格与音色，结合LLM编码和流匹配解码器进行合成
- 实验或效果：在DeepASMR-DB数据集上验证，实现高自然度和风格保真度，支持零样本生成

## 摘要（原文）

> While modern Text-to-Speech (TTS) systems achieve high fidelity for read-style speech, they struggle to generate Autonomous Sensory Meridian Response (ASMR), a specialized, low-intensity speech style essential for relaxation. The inherent challenges include ASMR's subtle, often unvoiced characteristics and the demand for zero-shot speaker adaptation. In this paper, we introduce DeepASMR, the first framework designed for zero-shot ASMR generation. We demonstrate that a single short snippet of a speaker's ordinary, read-style speech is sufficient to synthesize high-fidelity ASMR in their voice, eliminating the need for whispered training data from the target speaker. Methodologically, we first identify that discrete speech tokens provide a soft factorization of ASMR style from speaker timbre. Leveraging this insight, we propose a two-stage pipeline incorporating a Large Language Model (LLM) for content-style encoding and a flow-matching acoustic decoder for timbre reconstruction. Furthermore, we contribute DeepASMR-DB, a comprehensive 670-hour English-Chinese multi-speaker ASMR speech corpus, and introduce a novel evaluation protocol integrating objective metrics, human listening tests, LLM-based scoring and unvoiced speech analysis. Extensive experiments confirm that DeepASMR achieves state-of-the-art naturalness and style fidelity in ASMR generation for anyone of any voice, while maintaining competitive performance on normal speech synthesis.

