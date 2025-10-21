---
layout: default
title: From Preferences to Prejudice: The Role of Alignment Tuning in Shaping Social Bias in Video Diffusion Models
---

# From Preferences to Prejudice: The Role of Alignment Tuning in Shaping Social Bias in Video Diffusion Models
**arXiv**：[2510.17247v1](https://arxiv.org/abs/2510.17247) · [PDF](https://arxiv.org/pdf/2510.17247.pdf)  
**作者**：Zefan Cai, Haoyi Qiu, Haozhe Zhao, Ke Wan, Jiachen Li, Jiuxiang Gu, Wen Xiao, Nanyun Peng, Junjie Hu  

**一句话要点**：提出VideoBiasEval框架以评估视频扩散模型对齐调优中的社会偏见

**关键词**：视频扩散模型, 对齐调优, 社会偏见评估, 偏见放大, 多粒度指标, 时间稳定性

## 3 点简述
- 对齐调优在提升视频生成质量时可能无意中编码和放大社会偏见
- 引入VideoBiasEval框架，基于事件提示和多粒度指标系统评估偏见
- 实验显示对齐调优强化偏见并使其在视频中时间稳定

## 摘要（原文）

> Recent advances in video diffusion models have significantly enhanced
> text-to-video generation, particularly through alignment tuning using reward
> models trained on human preferences. While these methods improve visual
> quality, they can unintentionally encode and amplify social biases. To
> systematically trace how such biases evolve throughout the alignment pipeline,
> we introduce VideoBiasEval, a comprehensive diagnostic framework for evaluating
> social representation in video generation. Grounded in established social bias
> taxonomies, VideoBiasEval employs an event-based prompting strategy to
> disentangle semantic content (actions and contexts) from actor attributes
> (gender and ethnicity). It further introduces multi-granular metrics to
> evaluate (1) overall ethnicity bias, (2) gender bias conditioned on ethnicity,
> (3) distributional shifts in social attributes across model variants, and (4)
> the temporal persistence of bias within videos. Using this framework, we
> conduct the first end-to-end analysis connecting biases in human preference
> datasets, their amplification in reward models, and their propagation through
> alignment-tuned video diffusion models. Our results reveal that alignment
> tuning not only strengthens representational biases but also makes them
> temporally stable, producing smoother yet more stereotyped portrayals. These
> findings highlight the need for bias-aware evaluation and mitigation throughout
> the alignment process to ensure fair and socially responsible video generation.

