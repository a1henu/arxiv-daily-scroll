---
layout: default
title: Rethinking LLM-as-a-Judge: Representation-as-a-Judge with Small Language Models via Semantic Capacity Asymmetry
---

# Rethinking LLM-as-a-Judge: Representation-as-a-Judge with Small Language Models via Semantic Capacity Asymmetry
**arXiv**：[2601.22588v1](https://arxiv.org/abs/2601.22588) · [PDF](https://arxiv.org/pdf/2601.22588.pdf)  
**作者**：Zhuochun Li, Yong Zhang, Ming Li, Yuelyu Ji, Yiming Zeng, Ning Cheng, Yun Zhu, Yanmeng Wang, Shaojun Wang, Jing Xiao, Daqing He  

**一句话要点**：提出Representation-as-a-Judge范式，利用小模型内部表示替代大模型生成进行高效评估

**关键词**：语义容量不对称, 表示作为评估, 小语言模型, 内部表示探测, 解码无关评估

## 3 点简述
- 核心问题：LLM-as-a-Judge范式成本高、不透明且对提示敏感，需更高效评估方法
- 方法要点：基于语义容量不对称假设，通过INSPECTOR框架从小模型隐藏状态预测评估分数
- 实验或效果：在推理基准上，INSPECTOR优于基于提示的小模型，接近大模型评估效果

## 摘要（原文）

> Large language models (LLMs) are widely used as reference-free evaluators via prompting, but this "LLM-as-a-Judge" paradigm is costly, opaque, and sensitive to prompt design. In this work, we investigate whether smaller models can serve as efficient evaluators by leveraging internal representations instead of surface generation. We uncover a consistent empirical pattern: small LMs, despite with weak generative ability, encode rich evaluative signals in their hidden states. This motivates us to propose the Semantic Capacity Asymmetry Hypothesis: evaluation requires significantly less semantic capacity than generation and can be grounded in intermediate representations, suggesting that evaluation does not necessarily need to rely on large-scale generative models but can instead leverage latent features from smaller ones. Our findings motivate a paradigm shift from LLM-as-a-Judge to Representation-as-a-Judge, a decoding-free evaluation strategy that probes internal model structure rather than relying on prompted output. We instantiate this paradigm through INSPECTOR, a probing-based framework that predicts aspect-level evaluation scores from small model representations. Experiments on reasoning benchmarks (GSM8K, MATH, GPQA) show that INSPECTOR substantially outperforms prompting-based small LMs and closely approximates full LLM judges, while offering a more efficient, reliable, and interpretable alternative for scalable evaluation.

