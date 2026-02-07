---
layout: default
title: Synthesizing Realistic Test Data without Breaking Privacy
---

# Synthesizing Realistic Test Data without Breaking Privacy
**arXiv**：[2602.05833v1](https://arxiv.org/abs/2602.05833) · [PDF](https://arxiv.org/pdf/2602.05833.pdf)  
**作者**：Laura Plein, Alexi Turcotte, Arina Hallemans, Andreas Zeller  

**一句话要点**：提出基于模糊测试的合成数据生成方法，以在保护隐私的同时保持数据统计特性

**关键词**：合成数据生成, 隐私保护, 模糊测试, 统计分布保持, 生成对抗网络

## 3 点简述
- 核心问题：现有GAN方法在合成数据时易受隐私攻击，且准确性不足
- 方法要点：使用模糊测试生成数据，结合判别器评估与原始数据统计相似性
- 实验或效果：在四个数据集上验证，生成数据具有高实用性和隐私保护能力

## 摘要（原文）

> There is a need for synthetic training and test datasets that replicate statistical distributions of original datasets without compromising their confidentiality. A lot of research has been done in leveraging Generative Adversarial Networks (GANs) for synthetic data generation. However, the resulting models are either not accurate enough or are still vulnerable to membership inference attacks (MIA) or dataset reconstruction attacks since the original data has been leveraged in the training process. In this paper, we explore the feasibility of producing a synthetic test dataset with the same statistical properties as the original one, with only indirectly leveraging the original data in the generation process. The approach is inspired by GANs, with a generation step and a discrimination step. However, in our approach, we use a test generator (a fuzzer) to produce test data from an input specification, preserving constraints set by the original data; a discriminator model determines how close we are to the original data. By evolving samples and determining "good samples" with the discriminator, we can generate privacy-preserving data that follows the same statistical distributions are the original dataset, leading to a similar utility as the original data. We evaluated our approach on four datasets that have been used to evaluate the state-of-the-art techniques. Our experiments highlight the potential of our approach towards generating synthetic datasets that have high utility while preserving privacy.

