---
layout: default
title: Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding
---

# Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding
**arXiv**：[2603.06193v1](https://arxiv.org/abs/2603.06193) · [PDF](https://arxiv.org/pdf/2603.06193.pdf)  
**作者**：Hoseong Ahn, Jeongyun Chae, Yoonji Park, Kyuhong Shim  

**一句话要点**：提出Whisper-CD，基于多负例对比解码解决Whisper长语音识别中的幻觉和错误累积问题。

**关键词**：长语音识别, 对比解码, 无训练推理, 幻觉抑制, Whisper模型, 声学扰动

## 3 点简述
- 核心问题：Whisper等大模型在长语音识别中易产生幻觉、重复和内容遗漏，错误随解码上下文累积。
- 方法要点：通过高斯噪声注入、静音信号和音频时间偏移三种声学扰动构建负例，使用log-sum-exp聚合进行无训练对比解码。
- 实验或效果：在五个英语长语音基准上，WER降低最高24.3pp，token生成吞吐量比波束搜索快48%，无需训练即可部署。

## 摘要（原文）

> Long-form speech recognition with large encoder-decoder models such as Whisper often exhibit hallucinations, repetition loops, and content omissions. These errors can accumulate and be further amplified when the previous segment's transcription is used as decoding context. We propose Whisper-CD, a training-free contrastive decoding framework that contrasts clean-audio logits against negative logits computed from three acoustically motivated perturbations: Gaussian noise injection, silence signal, and audio temporal shift. We aggregate these negatives via the log-sum-exp operator, building a unified multi-negative objective for token-by-token decoding. Across five English long-form benchmarks, Whisper-CD reduces WER by up to 24.3pp on CORAAL and shows 48% faster token generation throughput than beam search. Because Whisper-CD operates purely at inference time, it can be applied as a drop-in replacement to already-deployed Whisper systems without retraining.

