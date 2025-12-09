---
layout: default
title: Minimum Bayes Risk Decoding for Error Span Detection in Reference-Free Automatic Machine Translation Evaluation
---

# Minimum Bayes Risk Decoding for Error Span Detection in Reference-Free Automatic Machine Translation Evaluation
**arXiv**：[2512.07540v1](https://arxiv.org/abs/2512.07540) · [PDF](https://arxiv.org/pdf/2512.07540.pdf)  
**作者**：Boxuan Lyu, Haiyue Song, Hidetaka Kamigaito, Chenchen Ding, Hideki Tanaka, Masao Utiyama, Kotaro Funakoshi, Manabu Okumura  

**一句话要点**：提出最小贝叶斯风险解码以解决生成式错误跨度检测中模型似然与人工标注不一致的问题

**关键词**：错误跨度检测, 最小贝叶斯风险解码, 机器翻译评估, 生成式模型, 蒸馏训练

## 3 点简述
- 核心问题：生成式错误跨度检测方法中，最大后验解码假设模型概率与人工标注相似度完美相关，但实际存在不一致。
- 方法要点：应用最小贝叶斯风险解码，使用句子和跨度级相似度度量作为效用函数，选择更接近人工标注的候选假设。
- 实验或效果：实验显示最小贝叶斯风险解码在系统、句子和跨度级别优于基线，并通过蒸馏消除推理延迟瓶颈。

## 摘要（原文）

> Error Span Detection (ESD) is a subtask of automatic machine translation evaluation that localizes error spans in translations and labels their severity. State-of-the-art generative ESD methods typically decode using Maximum a Posteriori (MAP), assuming that model-estimated probabilities are perfectly correlated with similarity to human annotation. However, we observed that annotations dissimilar to the human annotation could achieve a higher model likelihood than the human annotation. We address this issue by applying Minimum Bayes Risk (MBR) decoding to generative ESD models. Specifically, we employ sentence- and span-level similarity metrics as utility functions to select candidate hypotheses based on their approximate similarity to the human annotation. Extensive experimental results show that our MBR decoding outperforms the MAP baseline at the system, sentence, and span-levels. Furthermore, to mitigate the computational cost of MBR decoding, we demonstrate that applying MBR distillation enables a standard greedy model to match MBR decoding performance, effectively eliminating the inference-time latency bottleneck.

