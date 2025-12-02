---
layout: default
title: Efficient Training of Diffusion Mixture-of-Experts Models: A Practical Recipe
---

# Efficient Training of Diffusion Mixture-of-Experts Models: A Practical Recipe
**arXiv**：[2512.01252v1](https://arxiv.org/abs/2512.01252) · [PDF](https://arxiv.org/pdf/2512.01252.pdf)  
**作者**：Yahui Liu, Yang Yue, Jingyuan Zhang, Chenxi Sun, Yang Zhou, Wencong Zeng, Ruiming Tang, Guorui Zhou  

**一句话要点**：提出高效训练扩散专家混合模型的架构配置方案，以提升性能并减少激活参数。

**关键词**：扩散模型, 专家混合, 架构优化, 高效训练, 参数效率

## 3 点简述
- 核心问题：扩散专家混合模型的架构配置空间未充分探索，影响性能优化。
- 方法要点：借鉴大语言模型设计，系统研究专家模块、宽度、数量和位置编码等关键因素。
- 实验或效果：新架构在潜空间和像素空间扩散框架中高效应用，超越基线且参数更少。

## 摘要（原文）

> Recent efforts on Diffusion Mixture-of-Experts (MoE) models have primarily focused on developing more sophisticated routing mechanisms. However, we observe that the underlying architectural configuration space remains markedly under-explored. Inspired by the MoE design paradigms established in large language models (LLMs), we identify a set of crucial architectural factors for building effective Diffusion MoE models--including DeepSeek-style expert modules, alternative intermediate widths, varying expert counts, and enhanced attention positional encodings. Our systematic study reveals that carefully tuning these configurations is essential for unlocking the full potential of Diffusion MoE models, often yielding gains that exceed those achieved by routing innovations alone. Through extensive experiments, we present novel architectures that can be efficiently applied to both latent and pixel-space diffusion frameworks, which provide a practical and efficient training recipe that enables Diffusion MoE models to surpass strong baselines while using equal or fewer activated parameters. All code and models are publicly available at: https://github.com/yhlleo/EfficientMoE.

