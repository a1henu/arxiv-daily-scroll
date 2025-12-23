---
layout: default
title: dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models
---

# dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models
**arXiv**：[2512.19433v1](https://arxiv.org/abs/2512.19433) · [PDF](https://arxiv.org/pdf/2512.19433.pdf)  
**作者**：Yi Xin, Siqi Luo, Qi Qin, Haoxing Chen, Kaiwen Zhu, Zhiwei Zhang, Yangfan He, Rongchao Zhang, Jinbin Bai, Shuo Cao, Bin Fu, Junjun He, Yihao Liu, Yuewen Cao, Xiaohong Liu  

**一句话要点**：提出dMLLM-TTS框架，通过高效分层搜索与自验证反馈，提升扩散多模态大语言模型的测试时扩展效率与生成质量。

**关键词**：扩散多模态大语言模型, 测试时扩展, 分层搜索算法, 自验证反馈, 图像生成, 文本图像对齐

## 3 点简述
- 核心问题：扩散多模态大语言模型的测试时扩展方法效率低且依赖外部验证器，限制生成潜力。
- 方法要点：设计O(N+T)复杂度的分层搜索算法，并引入基于模型内在图像理解能力的自验证反馈机制。
- 实验或效果：在GenEval基准测试中，显著提升生成质量，效率比线性搜索最高提升6倍。

## 摘要（原文）

> Diffusion Multi-modal Large Language Models (dMLLMs) have recently emerged as a novel architecture unifying image generation and understanding. However, developing effective and efficient Test-Time Scaling (TTS) methods to unlock their full generative potential remains an underexplored challenge. To address this, we propose dMLLM-TTS, a novel framework operating on two complementary scaling axes: (1) trajectory exploration scaling to enhance the diversity of generated hypotheses, and (2) iterative refinement scaling for stable generation. Conventional TTS approaches typically perform linear search across these two dimensions, incurring substantial computational costs of O(NT) and requiring an external verifier for best-of-N selection. To overcome these limitations, we propose two innovations. First, we design an efficient hierarchical search algorithm with O(N+T) complexity that adaptively expands and prunes sampling trajectories. Second, we introduce a self-verified feedback mechanism that leverages the dMLLMs' intrinsic image understanding capabilities to assess text-image alignment, eliminating the need for external verifier. Extensive experiments on the GenEval benchmark across three representative dMLLMs (e.g., Lumina-DiMOO, MMaDA, Muddit) show that our framework substantially improves generation quality while achieving up to 6x greater efficiency than linear search. Project page: https://github.com/Alpha-VLLM/Lumina-DiMOO.

