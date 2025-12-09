---
layout: default
title: Improving the Throughput of Diffusion-based Large Language Models via a Training-Free Confidence-Aware Calibration
---

# Improving the Throughput of Diffusion-based Large Language Models via a Training-Free Confidence-Aware Calibration
**arXiv**：[2512.07173v1](https://arxiv.org/abs/2512.07173) · [PDF](https://arxiv.org/pdf/2512.07173.pdf)  
**作者**：Jucheng Shen, Gaurav Sarkar, Yeonju Ro, Sharath Nittur Sridhar, Zhangyang Wang, Aditya Akella, Souvik Kundu  

**一句话要点**：提出CadLLM以加速基于扩散的大语言模型推理吞吐量

**关键词**：扩散大语言模型, 推理加速, 训练无关方法, 置信度校准, KV缓存, 吞吐量优化

## 3 点简述
- 核心问题：扩散大语言模型推理吞吐量低，需提升效率。
- 方法要点：基于置信度动态调整生成参数，无需训练，兼容KV缓存模型。
- 实验或效果：在四个任务上实现最高2.28倍吞吐量提升，保持准确率。

## 摘要（原文）

> We present CadLLM, a training-free method to accelerate the inference throughput of diffusion-based LLMs (dLLMs). We first investigate the dynamic nature of token unmasking confidence across blocks and steps. Based on this observation, we present a lightweight adaptive approach that controls the generation block size, step size, and threshold based on the average confidence of unmasked tokens. We further reduce softmax overhead by dynamically leveraging a subset of the vocabulary to regulate sampling breadth. CadLLM is a plug-and-play, model-agnostic method compatible with KV-cache-based dLLMs. Extensive experiments on four popular tasks demonstrate that CadLLM yields up to 2.28x throughput improvement over the state-of-the-art baseline with competitive accuracy.

