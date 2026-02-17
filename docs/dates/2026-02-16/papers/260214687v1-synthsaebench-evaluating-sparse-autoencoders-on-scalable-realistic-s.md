---
layout: default
title: SynthSAEBench: Evaluating Sparse Autoencoders on Scalable Realistic Synthetic Data
---

# SynthSAEBench: Evaluating Sparse Autoencoders on Scalable Realistic Synthetic Data
**arXiv**：[2602.14687v1](https://arxiv.org/abs/2602.14687) · [PDF](https://arxiv.org/pdf/2602.14687.pdf)  
**作者**：David Chanin, Adrià Garriga-Alonso  

**一句话要点**：提出SynthSAEBench以解决稀疏自编码器评估中数据噪声大和规模小的问题

**关键词**：稀疏自编码器, 合成数据基准, 特征评估, 架构验证, 失败模式分析

## 3 点简述
- 核心问题：现有稀疏自编码器基准在大型语言模型上噪声过大，合成数据实验规模小且不真实，难以有效评估架构改进。
- 方法要点：开发SynthSAEBench工具包，生成大规模合成数据，模拟特征相关性、层次性和叠加性，并提供标准化基准模型SynthSAEBench-16k。
- 实验或效果：基准重现了稀疏自编码器在大型语言模型中的现象，如重建与潜在质量指标脱节，并识别出新失败模式：匹配追踪稀疏自编码器利用叠加噪声改进重建而未学习真实特征。

## 摘要（原文）

> Improving Sparse Autoencoders (SAEs) requires benchmarks that can precisely validate architectural innovations. However, current SAE benchmarks on LLMs are often too noisy to differentiate architectural improvements, and current synthetic data experiments are too small-scale and unrealistic to provide meaningful comparisons. We introduce SynthSAEBench, a toolkit for generating large-scale synthetic data with realistic feature characteristics including correlation, hierarchy, and superposition, and a standardized benchmark model, SynthSAEBench-16k, enabling direct comparison of SAE architectures. Our benchmark reproduces several previously observed LLM SAE phenomena, including the disconnect between reconstruction and latent quality metrics, poor SAE probing results, and a precision-recall trade-off mediated by L0. We further use our benchmark to identify a new failure mode: Matching Pursuit SAEs exploit superposition noise to improve reconstruction without learning ground-truth features, suggesting that more expressive encoders can easily overfit. SynthSAEBench complements LLM benchmarks by providing ground-truth features and controlled ablations, enabling researchers to precisely diagnose SAE failure modes and validate architectural improvements before scaling to LLMs.

