---
layout: default
title: Unconditional Human Motion and Shape Generation via Balanced Score-Based Diffusion
---

# Unconditional Human Motion and Shape Generation via Balanced Score-Based Diffusion
**arXiv**：[2510.12537v1](https://arxiv.org/abs/2510.12537) · [PDF](https://arxiv.org/pdf/2510.12537.pdf)  
**作者**：David Björkstrand, Tiesheng Wang, Lars Bretzner, Josephine Sullivan  

**一句话要点**：提出基于平衡分数扩散的无条件人体运动与形状生成方法，避免过参数化输入

**关键词**：人体运动生成, 扩散模型, 分数匹配, 形状生成, 无条件生成

## 3 点简述
- 核心问题：现有方法依赖过参数化输入和辅助损失，可能不必要
- 方法要点：使用分数扩散模型，仅需特征归一化和分析权重L2损失
- 实验或效果：在无条件人体运动生成中达到先进水平，直接生成运动与形状

## 摘要（原文）

> Recent work has explored a range of model families for human motion
> generation, including Variational Autoencoders (VAEs), Generative Adversarial
> Networks (GANs), and diffusion-based models. Despite their differences, many
> methods rely on over-parameterized input features and auxiliary losses to
> improve empirical results. These strategies should not be strictly necessary
> for diffusion models to match the human motion distribution. We show that on
> par with state-of-the-art results in unconditional human motion generation are
> achievable with a score-based diffusion model using only careful feature-space
> normalization and analytically derived weightings for the standard L2
> score-matching loss, while generating both motion and shape directly, thereby
> avoiding slow post hoc shape recovery from joints. We build the method step by
> step, with a clear theoretical motivation for each component, and provide
> targeted ablations demonstrating the effectiveness of each proposed addition in
> isolation.

