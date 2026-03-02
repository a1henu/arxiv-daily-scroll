---
layout: default
title: Task-Centric Acceleration of Small-Language Models
---

# Task-Centric Acceleration of Small-Language Models
**arXiv**：[2602.24174v1](https://arxiv.org/abs/2602.24174) · [PDF](https://arxiv.org/pdf/2602.24174.pdf)  
**作者**：Dor Tsur, Sharon Adar, Ran Levy  

**一句话要点**：提出TASC框架以加速小语言模型在任务特定应用中的推理效率

**关键词**：小语言模型加速, 任务自适应序列压缩, 推测解码, 词汇扩展, 低延迟推理

## 3 点简述
- 核心问题：小语言模型在高吞吐量、低延迟场景中效率不足，需优化任务特定性能
- 方法要点：TASC包括TASC-ft（微调时扩展词汇）和TASC-spec（推理时无训练推测解码）
- 实验或效果：在低输出变异性生成任务中，方法提升推理效率并保持任务性能

## 摘要（原文）

> Small language models (SLMs) have emerged as efficient alternatives to large language models for task-specific applications. However, they are often employed in high-volume, low-latency settings, where efficiency is crucial. We propose TASC, Task-Adaptive Sequence Compression, a framework for SLM acceleration comprising two use-cases: When performing SLM fine-tuning, we propose TASC-ft, which iteratively enriches the tokenizer vocabulary with high-frequency output n-grams and then fine-tunes the model to utilize the expanded vocabulary. Next, we propose an inference-time method, termed TASC-spec. TASC-spec is a lightweight, training-free speculative decoding method that constructs an n-gram draft model from the task's output corpus, mixing task and context n-gram information.TASC-spec avoids any additional training, while bypassing draft-target vocabulary alignment constraints. We demonstrate the effectiveness of both methods across multiple low output-variability generation tasks. Our methods show consistent improvements in inference efficiency while maintaining task performance.

