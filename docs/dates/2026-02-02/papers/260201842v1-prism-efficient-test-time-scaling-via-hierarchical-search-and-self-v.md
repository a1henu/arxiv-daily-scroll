---
layout: default
title: Prism: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models
---

# Prism: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models
**arXiv**：[2602.01842v1](https://arxiv.org/abs/2602.01842) · [PDF](https://arxiv.org/pdf/2602.01842.pdf)  
**作者**：Jinbin Bai, Yixuan Li, Yuchen Zhu, Yi Xin, Qingyu Shi, Aosong Feng, Xiaohong Liu, Molei Tao, Jianru Xue, Xiangtai Li, Ming-Hsuan Yang  

**一句话要点**：提出Prism框架，通过分层搜索与自验证，高效提升离散扩散语言模型的测试时推理性能。

**关键词**：离散扩散语言模型, 测试时缩放, 分层搜索, 自验证, 并行解码, 推理优化

## 3 点简述
- 核心问题：测试时缩放方法不适用于离散扩散语言模型的并行解码，导致其生成潜力未充分挖掘。
- 方法要点：采用分层轨迹搜索动态分配计算，局部分支与部分重掩码探索多样性，自验证反馈替代外部验证器。
- 实验或效果：在数学推理和代码生成基准上，以更少函数评估匹配最佳性能，实现性能与效率的平衡。

## 摘要（原文）

> Inference-time compute has re-emerged as a practical way to improve LLM reasoning. Most test-time scaling (TTS) algorithms rely on autoregressive decoding, which is ill-suited to discrete diffusion language models (dLLMs) due to their parallel decoding over the entire sequence. As a result, developing effective and efficient TTS methods to unlock dLLMs' full generative potential remains an underexplored challenge. To address this, we propose Prism (Pruning, Remasking, and Integrated Self-verification Method), an efficient TTS framework for dLLMs that (i) performs Hierarchical Trajectory Search (HTS) which dynamically prunes and reallocates compute in an early-to-mid denoising window, (ii) introduces Local branching with partial remasking to explore diverse implementations while preserving high-confidence tokens, and (iii) replaces external verifiers with Self-Verified Feedback (SVF) obtained via self-evaluation prompts on intermediate completions. Across four mathematical reasoning and code generation benchmarks on three dLLMs, including LLaDA 8B Instruct, Dream 7B Instruct, and LLaDA 2.0-mini, our Prism achieves a favorable performance-efficiency trade-off, matching best-of-N performance with substantially fewer function evaluations (NFE). The code is released at https://github.com/viiika/Prism.

