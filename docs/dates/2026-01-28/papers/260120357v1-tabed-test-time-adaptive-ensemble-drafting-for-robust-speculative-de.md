---
layout: default
title: TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
---

# TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
**arXiv**：[2601.20357v1](https://arxiv.org/abs/2601.20357) · [PDF](https://arxiv.org/pdf/2601.20357.pdf)  
**作者**：Minjae Lee, Wonjun Kang, Byeongkeun Ahn, Christian Classen, Kevin Galim, Seunghyuk Oh, Minghao Yan, Hyung Il Koo, Kangwook Lee  

**一句话要点**：提出测试时自适应集成草稿方法TABED，以增强大型视觉语言模型的推测解码鲁棒性。

**关键词**：推测解码, 大型视觉语言模型, 测试时自适应, 集成学习, 推理加速

## 3 点简述
- 核心问题：推测解码在大型视觉语言模型中性能波动，缺乏场景适应性。
- 方法要点：动态集成多个草稿，利用历史偏差进行自适应调整，无需训练。
- 实验或效果：在11个数据集上平均加速1.74倍，比单草稿方法提升5%。

## 摘要（原文）

> Speculative decoding (SD) has proven effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel. However, SD remains largely unexplored for Large Vision-Language Models (LVLMs), which extend LLMs to process both image and text prompts. To address this gap, we benchmark existing inference methods with small draft models on 11 datasets across diverse input scenarios and observe scenario-specific performance fluctuations. Motivated by these findings, we propose Test-time Adaptive Batched Ensemble Drafting (TABED), which dynamically ensembles multiple drafts obtained via batch inference by leveraging deviations from past ground truths available in the SD setting. The dynamic ensemble method achieves an average robust walltime speedup of 1.74x over autoregressive decoding and a 5% improvement over single drafting methods, while remaining training-free and keeping ensembling costs negligible through parameter sharing. With its plug-and-play compatibility, we further enhance TABED by integrating advanced verification and alternative drafting methods. Code and custom-trained models are available at https://github.com/furiosa-ai/TABED.

