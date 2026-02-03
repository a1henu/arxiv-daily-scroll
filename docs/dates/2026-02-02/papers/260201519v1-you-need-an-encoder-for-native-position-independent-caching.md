---
layout: default
title: You Need an Encoder for Native Position-Independent Caching
---

# You Need an Encoder for Native Position-Independent Caching
**arXiv**：[2602.01519v1](https://arxiv.org/abs/2602.01519) · [PDF](https://arxiv.org/pdf/2602.01519.pdf)  
**作者**：Shiju Zhao, Junhao Hu, Jiaqi Zheng, Guihai Chen  

**一句话要点**：提出原生位置无关缓存方法COMB，通过引入编码器解决大语言模型KV缓存效率低的问题。

**关键词**：位置无关缓存, 大语言模型优化, KV缓存系统, 编码器-解码器架构, 推理加速

## 3 点简述
- 核心问题：大语言模型的KV缓存基于前缀，处理任意顺序检索的上下文时效率低下。
- 方法要点：在仅解码器LLMs中重新引入编码器，并显式训练以支持位置无关缓存。
- 实验或效果：COMB降低首词生成时间51-94%，提升吞吐量3倍，保持可比准确性。

## 摘要（原文）

> The Key-Value (KV) cache of Large Language Models (LLMs) is prefix-based, making it highly inefficient for processing contexts retrieved in arbitrary order. Position-Independent Caching (PIC) has been proposed to enable KV reuse without positional constraints; however, existing approaches often incur substantial accuracy degradation, limiting their practical adoption. To address this issue, we propose native PIC by reintroducing the encoder to prevalent decoder-only LLMs and explicitly training it to support PIC. We further develop COMB, a PIC-aware caching system that integrates seamlessly with existing inference frameworks. Experimental results show that COMB reduces Time-to-First-Token (TTFT) by 51-94% and increases throughput by 3$\times$ with comparable accuracy. Furthermore, the quality improvement when using DeepSeek-V2-Lite-Chat demonstrates the applicability of COMB to other types of decoder-only LLMs. Our code is available at https://github.com/shijuzhao/Comb.

