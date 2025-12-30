---
layout: default
title: Memorization in 3D Shape Generation: An Empirical Study
---

# Memorization in 3D Shape Generation: An Empirical Study
**arXiv**：[2512.23628v1](https://arxiv.org/abs/2512.23628) · [PDF](https://arxiv.org/pdf/2512.23628.pdf)  
**作者**：Shu Pu, Boya Zeng, Kaichen Zhou, Mengyu Wang, Zhuang Liu  

**一句话要点**：提出评估框架量化3D生成模型记忆化，分析数据与建模设计影响

**关键词**：3D形状生成, 记忆化评估, 扩散模型, 数据安全, 生成多样性

## 3 点简述
- 核心问题：3D生成模型是否依赖训练数据记忆化，影响数据安全与生成多样性
- 方法要点：设计量化框架评估记忆化，基于Vecset扩散模型进行控制实验
- 实验或效果：发现数据模态、多样性、条件细化增加记忆化，建模中适度引导尺度峰值，可通过长Vecset和旋转增强缓解

## 摘要（原文）

> Generative models are increasingly used in 3D vision to synthesize novel shapes, yet it remains unclear whether their generation relies on memorizing training shapes. Understanding their memorization could help prevent training data leakage and improve the diversity of generated results. In this paper, we design an evaluation framework to quantify memorization in 3D generative models and study the influence of different data and modeling designs on memorization. We first apply our framework to quantify memorization in existing methods. Next, through controlled experiments with a latent vector-set (Vecset) diffusion model, we find that, on the data side, memorization depends on data modality, and increases with data diversity and finer-grained conditioning; on the modeling side, it peaks at a moderate guidance scale and can be mitigated by longer Vecsets and simple rotation augmentation. Together, our framework and analysis provide an empirical understanding of memorization in 3D generative models and suggest simple yet effective strategies to reduce it without degrading generation quality. Our code is available at https://github.com/zlab-princeton/3d_mem.

