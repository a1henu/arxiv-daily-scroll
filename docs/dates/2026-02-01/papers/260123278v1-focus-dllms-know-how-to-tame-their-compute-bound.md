---
layout: default
title: FOCUS: DLLMs Know How to Tame Their Compute Bound
---

# FOCUS: DLLMs Know How to Tame Their Compute Bound
**arXiv**：[2601.23278v1](https://arxiv.org/abs/2601.23278) · [PDF](https://arxiv.org/pdf/2601.23278.pdf)  
**作者**：Kaihua Liang, Xin Tan, An Zhong, Hong Xu, Marco Canini  

**一句话要点**：提出FOCUS系统以解决扩散大语言模型解码计算浪费问题

**关键词**：扩散大语言模型, 解码优化, 注意力机制, 推理系统, 计算效率

## 3 点简述
- 核心问题：DLLM解码时计算并行化但多数令牌不可解码，导致计算浪费
- 方法要点：基于注意力重要性动态聚焦计算于可解码令牌，提升有效批大小
- 实验或效果：在LMDeploy上实现最高3.52倍吞吐提升，保持或改进生成质量

## 摘要（原文）

> Diffusion Large Language Models (DLLMs) offer a compelling alternative to Auto-Regressive models, but their deployment is constrained by high decoding cost. In this work, we identify a key inefficiency in DLLM decoding: while computation is parallelized over token blocks, only a small subset of tokens is decodable at each diffusion step, causing most compute to be wasted on non-decodable tokens. We further observe a strong correlation between attention-derived token importance and token-wise decoding probability. Based on this insight, we propose FOCUS -- an inference system designed for DLLMs. By dynamically focusing computation on decodable tokens and evicting non-decodable ones on-the-fly, FOCUS increases the effective batch size, alleviating compute limitations and enabling scalable throughput. Empirical evaluations demonstrate that FOCUS achieves up to 3.52$\times$ throughput improvement over the production-grade engine LMDeploy, while preserving or improving generation quality across multiple benchmarks. The FOCUS system is publicly available on GitHub: https://github.com/sands-lab/FOCUS.

