---
layout: default
title: Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection
---

# Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection
**arXiv**：[2601.19245v1](https://arxiv.org/abs/2601.19245) · [PDF](https://arxiv.org/pdf/2601.19245.pdf)  
**作者**：Yongxin Deng, Zhen Fang, Yixuan Li, Ling Chen  

**一句话要点**：提出SpikeScore以解决大语言模型跨领域幻觉检测的泛化问题

**关键词**：幻觉检测, 跨领域泛化, 大语言模型, 多轮对话, 不确定性量化

## 3 点简述
- 研究跨领域幻觉检测问题，训练数据来自单一领域但需泛化到相关领域
- 基于多轮对话中不确定性波动现象，提出量化突变的SpikeScore方法
- 实验验证SpikeScore在跨领域检测中优于基线方法，提升泛化性能

## 摘要（原文）

> Hallucination detection is critical for deploying large language models (LLMs) in real-world applications. Existing hallucination detection methods achieve strong performance when the training and test data come from the same domain, but they suffer from poor cross-domain generalization. In this paper, we study an important yet overlooked problem, termed generalizable hallucination detection (GHD), which aims to train hallucination detectors on data from a single domain while ensuring robust performance across diverse related domains. In studying GHD, we simulate multi-turn dialogues following LLMs initial response and observe an interesting phenomenon: hallucination-initiated multi-turn dialogues universally exhibit larger uncertainty fluctuations than factual ones across different domains. Based on the phenomenon, we propose a new score SpikeScore, which quantifies abrupt fluctuations in multi-turn dialogues. Through both theoretical analysis and empirical validation, we demonstrate that SpikeScore achieves strong cross-domain separability between hallucinated and non-hallucinated responses. Experiments across multiple LLMs and benchmarks demonstrate that the SpikeScore-based detection method outperforms representative baselines in cross-domain generalization and surpasses advanced generalization-oriented methods, verifying the effectiveness of our method in cross-domain hallucination detection.

