---
layout: default
title: Salience-SGG: Enhancing Unbiased Scene Graph Generation with Iterative Salience Estimation
---

# Salience-SGG: Enhancing Unbiased Scene Graph Generation with Iterative Salience Estimation
**arXiv**：[2601.08728v1](https://arxiv.org/abs/2601.08728) · [PDF](https://arxiv.org/pdf/2601.08728.pdf)  
**作者**：Runfeng Qu, Ole Hall, Pia K Bideau, Julie Ouerfelli-Ethier, Martin Rolfs, Klaus Obermayer, Olaf Hellwich  

**一句话要点**：提出Salience-SGG框架，通过迭代显著性估计增强无偏场景图生成的空间理解能力

**关键词**：场景图生成, 无偏学习, 显著性估计, 空间理解, 长尾分布, 迭代解码

## 3 点简述
- 场景图生成存在长尾分布问题，导致模型偏向常见关系，空间理解不足
- 引入迭代显著性解码器，强调具有显著空间结构的三元组，并使用语义无关显著性标签指导
- 在多个数据集上实现先进性能，提升无偏方法在空间定位方面的表现

## 摘要（原文）

> Scene Graph Generation (SGG) suffers from a long-tailed distribution, where a few predicate classes dominate while many others are underrepresented, leading to biased models that underperform on rare relations. Unbiased-SGG methods address this issue by implementing debiasing strategies, but often at the cost of spatial understanding, resulting in an over-reliance on semantic priors. We introduce Salience-SGG, a novel framework featuring an Iterative Salience Decoder (ISD) that emphasizes triplets with salient spatial structures. To support this, we propose semantic-agnostic salience labels guiding ISD. Evaluations on Visual Genome, Open Images V6, and GQA-200 show that Salience-SGG achieves state-of-the-art performance and improves existing Unbiased-SGG methods in their spatial understanding as demonstrated by the Pairwise Localization Average Precision

