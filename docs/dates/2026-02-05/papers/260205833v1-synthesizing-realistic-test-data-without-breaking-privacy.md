---
layout: default
title: Synthesizing Realistic Test Data without Breaking Privacy
---

# Synthesizing Realistic Test Data without Breaking Privacy
**arXiv**：[2602.05833v1](https://arxiv.org/abs/2602.05833) · [PDF](https://arxiv.org/pdf/2602.05833.pdf)  
**作者**：Laura Plein, Alexi Turcotte, Arina Hallemans, Andreas Zeller  

**一句话要点**：提出基于模糊测试的隐私保护合成数据生成方法，以间接利用原始数据生成统计分布相似的测试数据集。

**关键词**：隐私保护, 合成数据生成, 模糊测试, 统计分布保持, 成员推断攻击防御

## 3 点简述
- 核心问题：现有GAN方法在生成合成数据时，因直接利用原始数据训练，易受成员推断或数据集重建攻击，且准确性不足。
- 方法要点：采用模糊测试生成器从输入规范生成数据，结合判别器评估与原始数据的统计相似性，通过进化样本实现隐私保护。
- 实验或效果：在四个数据集上评估，显示方法能生成高实用性合成数据，同时有效保护隐私。

## 摘要（原文）

> There is a need for synthetic training and test datasets that replicate statistical distributions of original datasets without compromising their confidentiality. A lot of research has been done in leveraging Generative Adversarial Networks (GANs) for synthetic data generation. However, the resulting models are either not accurate enough or are still vulnerable to membership inference attacks (MIA) or dataset reconstruction attacks since the original data has been leveraged in the training process. In this paper, we explore the feasibility of producing a synthetic test dataset with the same statistical properties as the original one, with only indirectly leveraging the original data in the generation process. The approach is inspired by GANs, with a generation step and a discrimination step. However, in our approach, we use a test generator (a fuzzer) to produce test data from an input specification, preserving constraints set by the original data; a discriminator model determines how close we are to the original data. By evolving samples and determining "good samples" with the discriminator, we can generate privacy-preserving data that follows the same statistical distributions are the original dataset, leading to a similar utility as the original data. We evaluated our approach on four datasets that have been used to evaluate the state-of-the-art techniques. Our experiments highlight the potential of our approach towards generating synthetic datasets that have high utility while preserving privacy.

