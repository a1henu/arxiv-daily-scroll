---
layout: default
title: From Agnostic to Specific: Latent Preference Diffusion for Multi-Behavior Sequential Recommendation
---

# From Agnostic to Specific: Latent Preference Diffusion for Multi-Behavior Sequential Recommendation
**arXiv**：[2602.23132v1](https://arxiv.org/abs/2602.23132) · [PDF](https://arxiv.org/pdf/2602.23132.pdf)  
**作者**：Ruochen Yang, Xiaodong Li, Jiawei Sheng, Jiangxia Cao, Xinkui Lin, Shen Wang, Shuang Yang, Zhaojie Liu, Tingwen Liu  

**一句话要点**：提出FatsMB框架，基于扩散模型从行为无关到行为特定引导潜在偏好生成，以解决多行为序列推荐中的偏好不确定性和多样性问题。

**关键词**：多行为序列推荐, 扩散模型, 潜在偏好空间, 行为特定建模, 不确定性处理, 推荐多样性

## 3 点简述
- 核心问题：现有方法忽略用户潜在偏好，且偏好评分范式难以处理从低熵行为到高熵项目的不确定性，导致推荐效果不佳。
- 方法要点：设计多行为自编码器构建统一潜在偏好空间，结合行为感知RoPE融合信息，通过扩散模型进行目标行为特定偏好转移，引入多条件引导层归一化去噪。
- 实验或效果：在真实世界数据集上进行了广泛实验，证明了模型的有效性，能够实现多样且准确的推荐。

## 摘要（原文）

> Multi-behavior sequential recommendation (MBSR) aims to learn the dynamic and heterogeneous interactions of users' multi-behavior sequences, so as to capture user preferences under target behavior for the next interacted item prediction. Unlike previous methods that adopt unidirectional modeling by mapping auxiliary behaviors to target behavior, recent concerns are shifting from behavior-fixed to behavior-specific recommendation. However, these methods still ignore the user's latent preference that underlying decision-making, leading to suboptimal solutions. Meanwhile, due to the asymmetric deterministic between items and behaviors, discriminative paradigm based on preference scoring is unsuitable to capture the uncertainty from low-entropy behaviors to high-entropy items, failing to provide efficient and diverse recommendation. To address these challenges, we propose \textbf{FatsMB}, a framework based diffusion model that guides preference generation \textit{\textbf{F}rom Behavior-\textbf{A}gnostic \textbf{T}o Behavior-\textbf{S}pecific} in latent spaces, enabling diverse and accurate \textit{\textbf{M}ulti-\textbf{B}ehavior Sequential Recommendation}. Specifically, we design a Multi-Behavior AutoEncoder (MBAE) to construct a unified user latent preference space, facilitating interaction and collaboration across Behaviors, within Behavior-aware RoPE (BaRoPE) employed for multiple information fusion. Subsequently, we conduct target behavior-specific preference transfer in the latent space, enriching with informative priors. A Multi-Condition Guided Layer Normalization (MCGLN) is introduced for the denoising. Extensive experiments on real-world datasets demonstrate the effectiveness of our model.

