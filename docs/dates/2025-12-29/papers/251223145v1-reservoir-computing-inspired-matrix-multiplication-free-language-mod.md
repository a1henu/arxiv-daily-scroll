---
layout: default
title: Reservoir Computing inspired Matrix Multiplication-free Language Model
---

# Reservoir Computing inspired Matrix Multiplication-free Language Model
**arXiv**：[2512.23145v1](https://arxiv.org/abs/2512.23145) · [PDF](https://arxiv.org/pdf/2512.23145.pdf)  
**作者**：Takumi Shiratsuchi, Yuichiro Tanaka, Hakaru Tamukoh  

**一句话要点**：提出基于储层计算的矩阵乘法免费语言模型，以降低大语言模型的计算成本。

**关键词**：矩阵乘法免费语言模型, 储层计算, 计算效率优化, 参数减少, 训练加速, 推理加速

## 3 点简述
- 核心问题：大语言模型计算成本高，成为性能瓶颈。
- 方法要点：采用矩阵乘法免费架构，结合储层计算固定部分权重，减少训练开销。
- 实验或效果：参数减少19%，训练和推理时间分别降低9.9%和8.0%，性能与基线相当。

## 摘要（原文）

> Large language models (LLMs) have achieved state-of-the-art performance in natural language processing; however, their high computational cost remains a major bottleneck. In this study, we target computational efficiency by focusing on a matrix multiplication free language model (MatMul-free LM) and further reducing the training cost through an architecture inspired by reservoir computing. Specifically, we partially fix and share the weights of selected layers in the MatMul-free LM and insert reservoir layers to obtain rich dynamic representations without additional training overhead. Additionally, several operations are combined to reduce memory accesses. Experimental results show that the proposed architecture reduces the number of parameters by up to 19%, training time by 9.9%, and inference time by 8.0%, while maintaining comparable performance to the baseline model.

