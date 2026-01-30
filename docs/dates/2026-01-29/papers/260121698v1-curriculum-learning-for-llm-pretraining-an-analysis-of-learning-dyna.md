---
layout: default
title: Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics
---

# Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics
**arXiv**：[2601.21698v1](https://arxiv.org/abs/2601.21698) · [PDF](https://arxiv.org/pdf/2601.21698.pdf)  
**作者**：Mohamed Elgaar, Hadi Amiri  

**一句话要点**：分析课程学习对LLM预训练学习动态的影响，揭示其通过稳定优化而非创建新阶段提升性能

**关键词**：课程学习, LLM预训练, 学习动态分析, 梯度方差控制, 优化稳定性

## 3 点简述
- 核心问题：课程学习是否改变学习轨迹或仅重排数据暴露顺序
- 方法要点：基于语言学动机设计三种课程，对比随机排序训练Pythia模型
- 实验或效果：课程学习减少梯度噪声和输出头谱饱和，增益随模型规模缩小

## 摘要（原文）

> Curriculum learning changes the order of pre-training data, but it remains unclear whether it changes the learning trajectory or mainly reorders exposure over a fixed trajectory. We train Pythia models (14M-410M parameters) for 300B tokens under three linguistically motivated curricula-Age-of-Acquisition, word frequency, and Verb Variation (VV)-and compare each against Random ordering; at 1B parameters we compare Random and VV. Across orderings, training follows a shared sequence of latent phases, while curricula mainly change within-phase data exposure. In smaller models (up to 160M parameters), Random ordering exhibits higher gradient noise and stronger late-training output-head spectral saturation, alongside lower final accuracy; curricula reduce both effects at matched compute. At larger scales, saturation differences are smaller and curriculum gains shrink. We formalize the link between difficulty pacing and optimization stability in an idealized analysis based on gradient-variance control, and our results point to a practical takeaway: curricula help by stabilizing within-phase optimization rather than by creating new phases.

