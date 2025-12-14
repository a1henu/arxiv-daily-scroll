---
layout: default
title: EchoingPixels: Cross-Modal Adaptive Token Reduction for Efficient Audio-Visual LLMs
---

# EchoingPixels: Cross-Modal Adaptive Token Reduction for Efficient Audio-Visual LLMs
**arXiv**：[2512.10324v1](https://arxiv.org/abs/2512.10324) · [PDF](https://arxiv.org/pdf/2512.10324.pdf)  
**作者**：Chao Gong, Depeng Wang, Zhipeng Wei, Ya Guo, Huijia Zhu, Jingjing Chen  

**一句话要点**：提出EchoingPixels框架，通过跨模态自适应令牌减少解决音频-视觉大语言模型的计算效率瓶颈。

**关键词**：音频-视觉大语言模型, 令牌减少, 跨模态交互, 计算效率优化, 自适应预算分配, 时间建模

## 3 点简述
- 音频-视觉大语言模型面临大量音频和视频令牌导致的计算开销过高问题，现有单模态令牌减少方法无法利用跨模态协同。
- 核心模块Cross-Modal Semantic Sieve（CS2）实现早期音频-视觉交互，从联合令牌池中自适应减少令牌，并设计Sync-RoPE保持稀疏令牌的时间关系。
- 实验表明，仅使用5-20%原始令牌即可达到基线性能，实现2-3倍加速和内存减少。

## 摘要（原文）

> Audio-Visual Large Language Models (AV-LLMs) face prohibitive computational overhead from massive audio and video tokens. Token reduction, while extensively explored for video-only LLMs, is insufficient for the audio-visual domain, as these unimodal methods cannot leverage audio-visual cross-modal synergies. Furthermore, the distinct and dynamic information densities of audio and video render static budgets per modality suboptimal. How to perform token reduction on a joint audio-visual stream thus remains an unaddressed bottleneck. To fill this gap, we introduce EchoingPixels, a framework inspired by the coexistence and interaction of visuals and sound in real-world scenes. The core of our framework is the Cross-Modal Semantic Sieve (CS2), a module enabling early audio-visual interaction. Instead of compressing modalities independently, CS2 co-attends to the joint multimodal stream and reduces tokens from an entire combined pool of audio-visual tokens rather than using fixed budgets per modality. This single-pool approach allows it to adaptively allocate the token budget across both modalities and dynamically identify salient tokens in concert. To ensure this aggressive reduction preserves the vital temporal modeling capability, we co-design a Synchronization-Augmented RoPE (Sync-RoPE) to maintain critical temporal relationships for the sparsely selected tokens. Extensive experiments demonstrate that EchoingPixels achieves performance comparable to strong baselines using only 5-20% of the original tokens, with a 2-3x speedup and memory reduction.

