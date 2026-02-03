---
layout: default
title: PISCES: Annotation-free Text-to-Video Post-Training via Optimal Transport-Aligned Rewards
---

# PISCES: Annotation-free Text-to-Video Post-Training via Optimal Transport-Aligned Rewards
**arXiv**：[2602.01624v1](https://arxiv.org/abs/2602.01624) · [PDF](https://arxiv.org/pdf/2602.01624.pdf)  
**作者**：Minh-Quan Le, Gaurav Mittal, Cheng Zhao, David Gu, Dimitris Samaras, Mei Chen  

**一句话要点**：提出PISCES，通过双重最优传输对齐奖励实现无标注文本到视频后训练，提升生成质量与语义对齐。

**关键词**：文本到视频生成, 后训练优化, 最优传输, 无标注学习, 奖励对齐, 视频质量评估

## 3 点简述
- 核心问题：现有基于奖励的后训练方法依赖大规模人工标注或预训练模型未对齐嵌入，导致可扩展性受限或监督效果不佳。
- 方法要点：引入双重最优传输对齐奖励模块，在分布和离散标记层面桥接文本与视频嵌入，实现质量奖励和语义奖励。
- 实验或效果：在短长视频生成任务中，PISCES在VBench质量和语义得分上优于有标注和无标注方法，人类偏好研究验证其有效性。

## 摘要（原文）

> Text-to-video (T2V) generation aims to synthesize videos with high visual quality and temporal consistency that are semantically aligned with input text. Reward-based post-training has emerged as a promising direction to improve the quality and semantic alignment of generated videos. However, recent methods either rely on large-scale human preference annotations or operate on misaligned embeddings from pre-trained vision-language models, leading to limited scalability or suboptimal supervision. We present $\texttt{PISCES}$, an annotation-free post-training algorithm that addresses these limitations via a novel Dual Optimal Transport (OT)-aligned Rewards module. To align reward signals with human judgment, $\texttt{PISCES}$ uses OT to bridge text and video embeddings at both distributional and discrete token levels, enabling reward supervision to fulfill two objectives: (i) a Distributional OT-aligned Quality Reward that captures overall visual quality and temporal coherence; and (ii) a Discrete Token-level OT-aligned Semantic Reward that enforces semantic, spatio-temporal correspondence between text and video tokens. To our knowledge, $\texttt{PISCES}$ is the first to improve annotation-free reward supervision in generative post-training through the lens of OT. Experiments on both short- and long-video generation show that $\texttt{PISCES}$ outperforms both annotation-based and annotation-free methods on VBench across Quality and Semantic scores, with human preference studies further validating its effectiveness. We show that the Dual OT-aligned Rewards module is compatible with multiple optimization paradigms, including direct backpropagation and reinforcement learning fine-tuning.

