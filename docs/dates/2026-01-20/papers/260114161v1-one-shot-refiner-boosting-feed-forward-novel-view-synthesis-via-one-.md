---
layout: default
title: One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion
---

# One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion
**arXiv**：[2601.14161v1](https://arxiv.org/abs/2601.14161) · [PDF](https://arxiv.org/pdf/2601.14161.pdf)  
**作者**：Yitong Dong, Qi Zhang, Minchao Jiang, Zhiqiang Wu, Qingnan Fan, Ying Feng, Huaqi Zhang, Hujun Bao, Guofeng Zhang  

**一句话要点**：提出One-Shot Refiner框架，通过一步扩散提升前馈式稀疏图像新视角合成质量

**关键词**：新视角合成, 3D高斯溅射, 扩散模型, 视觉Transformer, 高分辨率处理, 联合训练

## 3 点简述
- 核心问题：基于ViT的前馈3DGS方法受限于低分辨率输入和3D无关生成增强导致视角间结构不一致
- 方法要点：设计双域细节感知模块处理高分辨率图像，并引入特征引导扩散网络以保持高频细节
- 实验或效果：在多个数据集上验证了方法能维持优越的生成质量，支持联合优化

## 摘要（原文）

> We present a novel framework for high-fidelity novel view synthesis (NVS) from sparse images, addressing key limitations in recent feed-forward 3D Gaussian Splatting (3DGS) methods built on Vision Transformer (ViT) backbones. While ViT-based pipelines offer strong geometric priors, they are often constrained by low-resolution inputs due to computational costs. Moreover, existing generative enhancement methods tend to be 3D-agnostic, resulting in inconsistent structures across views, especially in unseen regions. To overcome these challenges, we design a Dual-Domain Detail Perception Module, which enables handling high-resolution images without being limited by the ViT backbone, and endows Gaussians with additional features to store high-frequency details. We develop a feature-guided diffusion network, which can preserve high-frequency details during the restoration process. We introduce a unified training strategy that enables joint optimization of the ViT-based geometric backbone and the diffusion-based refinement module. Experiments demonstrate that our method can maintain superior generation quality across multiple datasets.

