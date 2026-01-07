---
layout: default
title: Lil: Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage
---

# Lil: Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage
**arXiv**：[2601.03043v1](https://arxiv.org/abs/2601.03043) · [PDF](https://arxiv.org/pdf/2601.03043.pdf)  
**作者**：Junhao Hu, Fangze Li, Mingtao Xu, Feifan Meng, Shiju Zhao, Tiancheng Hu, Ting Peng, Anmin Liu, Wenrui Huang, Chenxu Liu, Ziyue Hua, Tao Xie  

**一句话要点**：提出早期停止算法以解决稀疏注意力在长解码阶段导致序列变长的问题

**关键词**：稀疏注意力, 长解码阶段, 早期停止算法, 推理效率, 大语言模型

## 3 点简述
- 核心问题：稀疏注意力算法在解码阶段可能因信息丢失导致序列显著变长，增加端到端复杂度
- 方法要点：设计早期停止算法，检测稀疏解码中信息损失超过信息增益的阈值
- 实验或效果：在推理密集型基准测试中，减少高达90%的令牌消耗，准确率下降小于2%

## 摘要（原文）

> Large language models (LLMs) demonstrate strong capabilities across a wide range of complex tasks and are increasingly deployed at scale, placing significant demands on inference efficiency. Prior work typically decomposes inference into prefill and decode stages, with the decode stage dominating total latency. To reduce time and memory complexity in the decode stage, a line of work introduces sparse-attention algorithms. In this paper, we show, both empirically and theoretically, that sparse attention can paradoxically increase end-to-end complexity: information loss often induces significantly longer sequences, a phenomenon we term ``Less is Less'' (Lil). To mitigate the Lil problem, we propose an early-stopping algorithm that detects the threshold where information loss exceeds information gain during sparse decoding. Our early-stopping algorithm reduces token consumption by up to 90% with a marginal accuracy degradation of less than 2% across reasoning-intensive benchmarks.

