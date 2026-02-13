---
layout: default
title: Differentially Private and Communication Efficient Large Language Model Split Inference via Stochastic Quantization and Soft Prompt
---

# Differentially Private and Communication Efficient Large Language Model Split Inference via Stochastic Quantization and Soft Prompt
**arXiv**：[2602.11513v1](https://arxiv.org/abs/2602.11513) · [PDF](https://arxiv.org/pdf/2602.11513.pdf)  
**作者**：Yujie Gu, Richeng Jin, Xiaoyu Ji, Yier Jin, Wenyuan Xu  

**一句话要点**：提出DEL框架，通过随机量化和软提示实现差分隐私与通信高效的大语言模型分割推理

**关键词**：差分隐私, 通信效率, 大语言模型推理, 随机量化, 软提示, 分割计算

## 3 点简述
- 核心问题：LLM本地部署受限，现有隐私保护方法通信和计算开销大
- 方法要点：嵌入投影和差分隐私随机量化降低通信，服务器端软提示补偿效用损失
- 实验或效果：在文本生成和自然语言理解基准上验证有效性，首次用软提示优化隐私-效用权衡

## 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable performance and received significant research interest. The enormous computational demands, however, hinder the local deployment on devices with limited resources. The current prevalent LLM inference paradigms require users to send queries to the service providers for processing, which raises critical privacy concerns. Existing approaches propose to allow the users to obfuscate the token embeddings before transmission and utilize local models for denoising. Nonetheless, transmitting the token embeddings and deploying local models may result in excessive communication and computation overhead, preventing practical implementation. In this work, we propose \textbf{DEL}, a framework for \textbf{D}ifferentially private and communication \textbf{E}fficient \textbf{L}LM split inference. More specifically, an embedding projection module and a differentially private stochastic quantization mechanism are proposed to reduce the communication overhead in a privacy-preserving manner. To eliminate the need for local models, we adapt soft prompt at the server side to compensate for the utility degradation caused by privacy. To the best of our knowledge, this is the first work that utilizes soft prompt to improve the trade-off between privacy and utility in LLM inference, and extensive experiments on text generation and natural language understanding benchmarks demonstrate the effectiveness of the proposed method.

