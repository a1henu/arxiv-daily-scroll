---
layout: default
title: WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation
---

# WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation
**arXiv**：[2603.05299v1](https://arxiv.org/abs/2603.05299) · [PDF](https://arxiv.org/pdf/2603.05299.pdf)  
**作者**：Luca Della Libera, Cem Subakan, Mirco Ravanelli  

**一句话要点**：提出WavSLM，通过WavLM蒸馏实现单流语音语言建模，无需文本监督。

**关键词**：语音语言建模, 自监督学习, 蒸馏训练, 单流生成, 语音生成, 流式推理

## 3 点简述
- 核心问题：语音中语义与声学信息纠缠，现有模型多依赖文本或复杂架构，偏离单流生成预训练范式。
- 方法要点：量化并蒸馏自监督WavLM表示到单一码本，优化自回归下一块预测目标，实现单流建模。
- 实验或效果：在一致性基准和语音生成上表现竞争性，参数少、训练数据少，支持流式推理。

## 摘要（原文）

> Large language models show that simple autoregressive training can yield scalable and coherent generation, but extending this paradigm to speech remains challenging due to the entanglement of semantic and acoustic information. Most existing speech language models rely on text supervision, hierarchical token streams, or complex hybrid architectures, departing from the single-stream generative pretraining paradigm that has proven effective in text. In this work, we introduce WavSLM, a speech language model trained by quantizing and distilling self-supervised WavLM representations into a single codebook and optimizing an autoregressive next-chunk prediction objective. WavSLM jointly models semantic and acoustic information within a single token stream without text supervision or text pretraining. Despite its simplicity, it achieves competitive performance on consistency benchmarks and speech generation while using fewer parameters, less training data, and supporting streaming inference. Demo samples are available at https://lucadellalib.github.io/wavslm-web/.

