---
layout: default
title: GPD: Guided Progressive Distillation for Fast and High-Quality Video Generation
---

# GPD: Guided Progressive Distillation for Fast and High-Quality Video Generation
**arXiv**：[2602.01814v1](https://arxiv.org/abs/2602.01814) · [PDF](https://arxiv.org/pdf/2602.01814.pdf)  
**作者**：Xiao Liang, Yunzhu Zhang, Linchao Zhu  

**一句话要点**：提出引导渐进蒸馏框架以加速高质量视频生成

**关键词**：视频生成, 扩散模型, 模型蒸馏, 计算加速, 频域约束

## 3 点简述
- 扩散模型视频生成计算成本高，现有方法加速时质量下降
- 引入教师模型渐进指导学生模型使用更大步长，结合在线生成目标和频域约束
- 在Wan2.1模型上，采样步数从48减至6，VBench上保持视觉质量

## 摘要（原文）

> Diffusion models have achieved remarkable success in video generation; however, the high computational cost of the denoising process remains a major bottleneck. Existing approaches have shown promise in reducing the number of diffusion steps, but they often suffer from significant quality degradation when applied to video generation. We propose Guided Progressive Distillation (GPD), a framework that accelerates the diffusion process for fast and high-quality video generation. GPD introduces a novel training strategy in which a teacher model progressively guides a student model to operate with larger step sizes. The framework consists of two key components: (1) an online-generated training target that reduces optimization difficulty while improving computational efficiency, and (2) frequency-domain constraints in the latent space that promote the preservation of fine-grained details and temporal dynamics. Applied to the Wan2.1 model, GPD reduces the number of sampling steps from 48 to 6 while maintaining competitive visual quality on VBench. Compared with existing distillation methods, GPD demonstrates clear advantages in both pipeline simplicity and quality preservation.

