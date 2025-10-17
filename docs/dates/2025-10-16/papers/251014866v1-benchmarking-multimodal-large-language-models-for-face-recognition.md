---
layout: default
title: Benchmarking Multimodal Large Language Models for Face Recognition
---

# Benchmarking Multimodal Large Language Models for Face Recognition
**arXiv**：[2510.14866v1](https://arxiv.org/abs/2510.14866) · [PDF](https://arxiv.org/pdf/2510.14866.pdf)  
**作者**：Hatef Otroshi Shahreza, Sébastien Marcel  

**一句话要点**：基准测试多模态大语言模型在面部识别中的性能，揭示其在零样本应用中的局限性

**关键词**：多模态大语言模型, 面部识别, 基准测试, 零样本学习, 开源模型

## 3 点简述
- 核心问题：多模态大语言模型在面部识别中的潜力未充分探索，需与专业模型比较。
- 方法要点：系统评估开源MLLMs在多个标准面部数据集上的表现。
- 实验或效果：MLLMs捕获语义线索，但在高精度零样本识别中落后于专业模型。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable performance
> across diverse vision-and-language tasks. However, their potential in face
> recognition remains underexplored. In particular, the performance of
> open-source MLLMs needs to be evaluated and compared with existing face
> recognition models on standard benchmarks with similar protocol. In this work,
> we present a systematic benchmark of state-of-the-art MLLMs for face
> recognition on several face recognition datasets, including LFW, CALFW, CPLFW,
> CFP, AgeDB and RFW. Experimental results reveal that while MLLMs capture rich
> semantic cues useful for face-related tasks, they lag behind specialized models
> in high-precision recognition scenarios in zero-shot applications. This
> benchmark provides a foundation for advancing MLLM-based face recognition,
> offering insights for the design of next-generation models with higher accuracy
> and generalization. The source code of our benchmark is publicly available in
> the project page.

