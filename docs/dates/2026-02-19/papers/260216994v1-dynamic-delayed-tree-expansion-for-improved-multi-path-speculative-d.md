---
layout: default
title: Dynamic Delayed Tree Expansion For Improved Multi-Path Speculative Decoding
---

# Dynamic Delayed Tree Expansion For Improved Multi-Path Speculative Decoding
**arXiv**：[2602.16994v1](https://arxiv.org/abs/2602.16994) · [PDF](https://arxiv.org/pdf/2602.16994.pdf)  
**作者**：Rahul Thomas, Teo Kitanovski, Micah Goldblum, Arka Pal  

**一句话要点**：提出动态延迟树扩展以改进多路径推测解码，提升吞吐量

**关键词**：推测解码, 多路径采样, 延迟树扩展, 最优传输, 神经选择器, 吞吐量优化

## 3 点简述
- 系统评估多路径推测解码的验证策略，发现遍历验证优于基于最优传输的方法
- 提出延迟树扩展，通过延迟分支点提高多令牌接受率，保持目标分布
- 开发动态神经选择器，使基于最优传输的方法首次超越遍历验证，平均吞吐量提升5%

## 摘要（原文）

> Multi-path speculative decoding accelerates lossless sampling from a target model by using a cheaper draft model to generate a draft tree of tokens, and then applies a verification algorithm that accepts a subset of these. While prior work has proposed various verification algorithms for i.i.d rollouts, their relative performance under matched settings remains unclear. In this work, we firstly present a systematic evaluation of verification strategies across model families, tasks, and sampling regimes, and find that Traversal Verification dominates consistently, with OT-based methods lagging far behind. Our analysis uncovers that this occurs because OT-based methods achieve high multi-token acceptance near the root of the draft tree, while multi-token gains are most impactful deeper in the draft tree, where draft and target distributions diverge. Based on this insight, we propose delayed tree expansion, which drafts a partial single path, delaying the i.i.d. branching point. We show that delayed tree expansion preserves the target distribution and improves on root-node i.i.d rollouts. Further, we develop a dynamic neural selector that estimates the expected block efficiency of optimal-transport-based verification methods from draft and target features, enabling context-dependent expansion decisions. Our neural selector allows OT-based methods like SpecInfer to outperform Traversal Verification for the first time, achieving 5% higher average throughput across a wide range of models, datasets, and sampling settings.

