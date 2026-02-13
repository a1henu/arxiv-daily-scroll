---
layout: default
title: Do MLLMs Really Understand Space? A Mathematical Reasoning Evaluation
---

# Do MLLMs Really Understand Space? A Mathematical Reasoning Evaluation
**arXiv**：[2602.11635v1](https://arxiv.org/abs/2602.11635) · [PDF](https://arxiv.org/pdf/2602.11635.pdf)  
**作者**：Shuo Lu, Jianjie Cheng, Yinuo Xu, Yongcan Yu, Lijun Sheng, Peijie Wang, Siru Jiang, Yongguan Hu, Run Ling, Yihua Shao, Ao Ma, Wei Feng, Lingxiao He, Meng Wang, Qianlong Xie, Xingxing Wang, Ran He, Jian Liang  

**一句话要点**：提出MathSpatial框架以评估和改进多模态大语言模型在数学空间推理上的能力

**关键词**：多模态大语言模型, 数学空间推理, 基准测试, 结构化推理, 微调优化, 感知与推理分离

## 3 点简述
- 核心问题：MLLMs在数学空间推理任务上表现不佳，准确率低于60%，远逊于人类水平。
- 方法要点：MathSpatial包括基准测试、训练数据集和结构化推理追踪，以分离感知与推理。
- 实验或效果：在Qwen2.5-VL-7B上微调后，实现竞争性准确率并减少25%的令牌使用。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved strong performance on perception-oriented tasks, yet their ability to perform mathematical spatial reasoning, defined as the capacity to parse and manipulate two- and three-dimensional relations, remains unclear. Humans easily solve textbook-style spatial reasoning problems with over 95\% accuracy, but we find that most leading MLLMs fail to reach even 60\% on the same tasks. This striking gap highlights spatial reasoning as a fundamental weakness of current models. To investigate this gap, we present MathSpatial, a unified framework for evaluating and improving spatial reasoning in MLLMs. MathSpatial includes three complementary components: (i) MathSpatial-Bench, a benchmark of 2K problems across three categories and eleven subtypes, designed to isolate reasoning difficulty from perceptual noise; (ii) MathSpatial-Corpus, a training dataset of 8K additional problems with verified solutions; and (iii) MathSpatial-SRT, which models reasoning as structured traces composed of three atomic operations--Correlate, Constrain, and Infer. Experiments show that fine-tuning Qwen2.5-VL-7B on MathSpatial achieves competitive accuracy while reducing tokens by 25\%. MathSpatial provides the first large-scale resource that disentangles perception from reasoning, enabling precise measurement and comprehensive understanding of mathematical spatial reasoning in MLLMs.

