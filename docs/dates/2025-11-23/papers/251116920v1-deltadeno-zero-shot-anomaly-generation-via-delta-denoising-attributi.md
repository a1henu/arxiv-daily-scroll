---
layout: default
title: DeltaDeno: Zero-Shot Anomaly Generation via Delta-Denoising Attribution
---

# DeltaDeno: Zero-Shot Anomaly Generation via Delta-Denoising Attribution
**arXiv**：[2511.16920v1](https://arxiv.org/abs/2511.16920) · [PDF](https://arxiv.org/pdf/2511.16920.pdf)  
**作者**：Chaoran Xu, Chengkan Lv, Qiyu Chen, Yunkang Cao, Feng Zhang, Zhengtao Zhang  

**一句话要点**：提出DeltaDeno方法以在零样本场景下生成异常样本

**关键词**：零样本异常生成, 扩散模型, 去噪对比, 图像定位, 潜在修复

## 3 点简述
- 核心问题：异常样本稀缺，传统方法依赖少量样本微调易过拟合
- 方法要点：基于扩散模型对比分支，通过去噪差异定位并编辑缺陷
- 实验效果：在公共数据集上生成真实异常，提升下游检测性能

## 摘要（原文）

> Anomaly generation is often framed as few-shot fine-tuning with anomalous samples, which contradicts the scarcity that motivates generation and tends to overfit category priors. We tackle the setting where no real anomaly samples or training are available. We propose Delta-Denoising (DeltaDeno), a training-free zero-shot anomaly generation method that localizes and edits defects by contrasting two diffusion branches driven by a minimal prompt pair under a shared schedule. By accumulating per-step denoising deltas into an image-specific localization map, we obtain a mask to guide the latent inpainting during later diffusion steps and preserve the surrounding context while generating realistic local defects. To improve stability and control, DeltaDeno performs token-level prompt refinement that aligns shared content and strengthens anomaly tokens, and applies a spatial attention bias restricted to anomaly tokens in the predicted region. Experiments on public datasets show that DeltaDeno achieves great generation, realism and consistent gains in downstream detection performance. Code will be made publicly available.

