---
layout: default
title: Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning
---

# Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning
**arXiv**：[2602.06584v1](https://arxiv.org/abs/2602.06584) · [PDF](https://arxiv.org/pdf/2602.06584.pdf)  
**作者**：Deqian Kong, Minglu Zhao, Aoyang Qin, Bo Pang, Chenxin Tao, David Hartmann, Edouardo Honig, Dehong Xu, Amit Kumar, Matt Sarte, Chuan Li, Jianwen Xie, Ying Nian Wu  

**一句话要点**：提出推理时反思框架，通过潜在思维向量实现数学推理的迭代自校正

**关键词**：数学推理, 潜在思维向量, 推理时反思, 迭代自校正, 梯度优化

## 3 点简述
- 标准思维链推理在单次前向传播中生成解决方案，缺乏早期错误恢复机制
- 方法将推理分解为连续潜在思维向量（声明性内容）和解码器（程序性生成），支持梯度优化
- 在GSM8K上训练0.2B参数模型，经30次反思迭代超越更大参数基线，展示推理时计算的有效性

## 摘要（原文）

> Standard chain-of-thought reasoning generates a solution in a single forward pass, committing irrevocably to each token and lacking a mechanism to recover from early errors. We introduce Inference-Time Rethinking, a generative framework that enables iterative self-correction by decoupling declarative latent thought vectors from procedural generation. We factorize reasoning into a continuous latent thought vector (what to reason about) and a decoder that verbalizes the trace conditioned on this vector (how to reason). Beyond serving as a declarative buffer, latent thought vectors compress the reasoning structure into a continuous representation that abstracts away surface-level token variability, making gradient-based optimization over reasoning strategies well-posed. Our prior model maps unstructured noise to a learned manifold of valid reasoning patterns, and at test time we employ a Gibbs-style procedure that alternates between generating a candidate trace and optimizing the latent vector to better explain that trace, effectively navigating the latent manifold to refine the reasoning strategy. Training a 0.2B-parameter model from scratch on GSM8K, our method with 30 rethinking iterations surpasses baselines with 10 to 15 times more parameters, including a 3B counterpart. This result demonstrates that effective mathematical reasoning can emerge from sophisticated inference-time computation rather than solely from massive parameter counts.

