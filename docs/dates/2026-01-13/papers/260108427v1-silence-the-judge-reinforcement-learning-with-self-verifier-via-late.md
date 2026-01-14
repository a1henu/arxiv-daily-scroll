---
layout: default
title: Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering
---

# Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering
**arXiv**：[2601.08427v1](https://arxiv.org/abs/2601.08427) · [PDF](https://arxiv.org/pdf/2601.08427.pdf)  
**作者**：Nonghai Zhang, Weitao Ma, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He, Jingwen Xu  

**一句话要点**：提出Latent-GRPO框架，通过潜在空间几何聚类实现强化学习自验证，以降低对外部验证器的依赖。

**关键词**：强化学习, 潜在空间几何, 自验证, 聚类算法, 推理优化, 计算效率

## 3 点简述
- 核心问题：GRPO依赖昂贵外部验证器或人工规则，导致计算成本高、训练延迟和稀疏奖励问题。
- 方法要点：基于正确推理轨迹终端令牌表示形成密集簇的几何特性，引入IRCE算法生成密集连续奖励。
- 实验或效果：在多个数据集上保持性能，训练速度提升超2倍，并展示强泛化能力和鲁棒性。

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) significantly enhances the reasoning performance of Large Language Models (LLMs). However, this success heavily relies on expensive external verifiers or human rules. Such dependency not only leads to significant computational costs and training latency, but also yields sparse rewards that hinder optimization efficiency. To address these challenges, we propose Latent-GRPO, a framework that derives intrinsic rewards directly from latent space geometry. Crucially, our empirical analysis reveals a compelling geometric property: terminal token representations of correct reasoning trajectories form dense clusters with high intra-class similarity, whereas incorrect trajectories remain scattered as outliers. In light of this discovery, we introduce the Iterative Robust Centroid Estimation (IRCE) algorithm, which generates dense, continuous rewards by mitigating magnitude fluctuations via spherical projection and estimating a robust ``truth centroid'' through iterative aggregation. Experimental results on multiple datasets show that our method maintains model performance while achieving a training speedup of over 2x compared to baselines. Furthermore, extensive results demonstrate strong generalization ability and robustness. The code will be released soon.

