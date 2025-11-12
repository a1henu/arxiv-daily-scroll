---
layout: default
title: PC-Diffusion: Aligning Diffusion Models with Human Preferences via Preference Classifier
---

# PC-Diffusion: Aligning Diffusion Models with Human Preferences via Preference Classifier
**arXiv**：[2511.07806v1](https://arxiv.org/abs/2511.07806) · [PDF](https://arxiv.org/pdf/2511.07806.pdf)  
**作者**：Shaomeng Wang, He Wang, Xiaolu Wei, Longquan Dai, Jinhui Tang  

**一句话要点**：提出PC-Diffusion框架，通过偏好分类器对齐扩散模型与人类偏好

**关键词**：扩散模型, 偏好对齐, 轻量分类器, 直接偏好优化, 图像生成, 计算效率

## 3 点简述
- 扩散模型输出常与人类偏好不一致，现有DPO方法计算成本高且依赖参考模型
- PC-Diffusion使用轻量偏好分类器直接建模样本偏好，无需全模型微调或参考模型
- 实验显示PC-Diffusion在保持偏好一致性的同时显著降低训练成本，实现高效稳定生成

## 摘要（原文）

> Diffusion models have achieved remarkable success in conditional image generation, yet their outputs often remain misaligned with human preferences. To address this, recent work has applied Direct Preference Optimization (DPO) to diffusion models, yielding significant improvements.~However, DPO-like methods exhibit two key limitations: 1) High computational cost,due to the entire model fine-tuning; 2) Sensitivity to reference model quality}, due to its tendency to introduce instability and bias. To overcome these limitations, we propose a novel framework for human preference alignment in diffusion models (PC-Diffusion), using a lightweight, trainable Preference Classifier that directly models the relative preference between samples. By restricting preference learning to this classifier, PC-Diffusion decouples preference alignment from the generative model, eliminating the need for entire model fine-tuning and reference model reliance.~We further provide theoretical guarantees for PC-Diffusion:1) PC-Diffusion ensures that the preference-guided distributions are consistently propagated across timesteps. 2)The training objective of the preference classifier is equivalent to DPO, but does not require a reference model.3) The proposed preference-guided correction can progressively steer generation toward preference-aligned regions.~Empirical results show that PC-Diffusion achieves comparable preference consistency to DPO while significantly reducing training costs and enabling efficient and stable preference-guided generation.

