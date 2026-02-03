---
layout: default
title: Repurposing Protein Language Models for Latent Flow-Based Fitness Optimization
---

# Repurposing Protein Language Models for Latent Flow-Based Fitness Optimization
**arXiv**：[2602.02425v1](https://arxiv.org/abs/2602.02425) · [PDF](https://arxiv.org/pdf/2602.02425.pdf)  
**作者**：Amaru Caceres Arroyo, Lea Bogensperger, Ahmed Allam, Michael Krauthammer, Konrad Schindler, Dominik Narnhofer  

**一句话要点**：提出CHASE框架，利用蛋白质语言模型嵌入和条件流匹配优化蛋白质适应度

**关键词**：蛋白质适应度优化, 蛋白质语言模型, 条件流匹配, 潜在空间压缩, 分类器自由引导, 合成数据引导

## 3 点简述
- 蛋白质适应度优化面临高维稀疏组合空间挑战，现有方法性能不足或计算成本高
- CHASE通过压缩预训练蛋白质语言模型嵌入到紧凑潜在空间，结合条件流匹配和分类器自由引导直接生成高适应度变体
- 在AAV和GFP基准测试中达到最优性能，并展示合成数据引导在数据受限场景下的增强效果

## 摘要（原文）

> Protein fitness optimization is challenged by a vast combinatorial landscape where high-fitness variants are extremely sparse. Many current methods either underperform or require computationally expensive gradient-based sampling. We present CHASE, a framework that repurposes the evolutionary knowledge of pretrained protein language models by compressing their embeddings into a compact latent space. By training a conditional flow-matching model with classifier-free guidance, we enable the direct generation of high-fitness variants without predictor-based guidance during the ODE sampling steps. CHASE achieves state-of-the-art performance on AAV and GFP protein design benchmarks. Finally, we show that bootstrapping with synthetic data can further enhance performance in data-constrained settings.

