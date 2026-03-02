---
layout: default
title: CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation
---

# CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation
**arXiv**：[2602.24286v1](https://arxiv.org/abs/2602.24286) · [PDF](https://arxiv.org/pdf/2602.24286.pdf)  
**作者**：Weinan Dai, Hanlin Wu, Qiying Yu, Huan-ang Gao, Jiahao Li, Chengquan Jiang, Weiqiang Lou, Yufan Song, Hongli Yu, Jiaze Chen, Wei-Ying Ma, Ya-Qin Zhang, Jingjing Liu, Mingxuan Wang, Xin Liu, Hao Zhou  

**一句话要点**：提出CUDA Agent，通过大规模代理强化学习系统解决高性能CUDA内核生成问题。

**关键词**：CUDA内核生成, 代理强化学习, GPU优化, 大规模训练, 自动化验证

## 3 点简述
- 核心问题：GPU内核优化依赖专家知识，现有LLM方法在CUDA生成上性能不足。
- 方法要点：结合数据合成、技能增强环境和强化学习算法，提升模型优化能力。
- 实验或效果：在KernelBench上超越torch.compile和最强专有模型，实现显著加速。

## 摘要（原文）

> GPU kernel optimization is fundamental to modern deep learning but remains a highly specialized task requiring deep hardware expertise. Despite strong performance in general programming, large language models (LLMs) remain uncompetitive with compiler-based systems such as torch.compile for CUDA kernel generation. Existing CUDA code generation approaches either rely on training-free refinement or fine-tune models within fixed multi-turn execution-feedback loops, but both paradigms fail to fundamentally improve the model's intrinsic CUDA optimization ability, resulting in limited performance gains. We present CUDA Agent, a large-scale agentic reinforcement learning system that develops CUDA kernel expertise through three components: a scalable data synthesis pipeline, a skill-augmented CUDA development environment with automated verification and profiling to provide reliable reward signals, and reinforcement learning algorithmic techniques enabling stable training. CUDA Agent achieves state-of-the-art results on KernelBench, delivering 100\%, 100\%, and 92\% faster rate over torch.compile on KernelBench Level-1, Level-2, and Level-3 splits, outperforming the strongest proprietary models such as Claude Opus 4.5 and Gemini 3 Pro by about 40\% on the hardest Level-3 setting.

