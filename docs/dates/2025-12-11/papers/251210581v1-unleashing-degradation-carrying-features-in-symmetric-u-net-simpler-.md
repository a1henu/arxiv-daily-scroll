---
layout: default
title: Unleashing Degradation-Carrying Features in Symmetric U-Net: Simpler and Stronger Baselines for All-in-One Image Restoration
---

# Unleashing Degradation-Carrying Features in Symmetric U-Net: Simpler and Stronger Baselines for All-in-One Image Restoration
**arXiv**：[2512.10581v1](https://arxiv.org/abs/2512.10581) · [PDF](https://arxiv.org/pdf/2512.10581.pdf)  
**作者**：Wenlong Jiao, Heyang Lee, Ping Wang, Pengfei Zhu, Qinghua Hu, Dongwei Ren  

**一句话要点**：提出对称U-Net以简化全场景图像修复，通过释放退化携带特征实现高性能

**关键词**：全场景图像修复, 对称U-Net, 退化携带特征, 跨尺度传播, 语义增强, CLIP特征

## 3 点简述
- 全场景图像修复现有方法依赖复杂架构，导致计算成本高且效率低
- 对称U-Net通过对齐特征尺度和跨尺度传播，有效提取并利用退化信息
- 实验表明SymUNet和SE-SymUNet在多个基准数据集上优于现有方法，计算成本更低

## 摘要（原文）

> All-in-one image restoration aims to handle diverse degradations (e.g., noise, blur, adverse weather) within a unified framework, yet existing methods increasingly rely on complex architectures (e.g., Mixture-of-Experts, diffusion models) and elaborate degradation prompt strategies. In this work, we reveal a critical insight: well-crafted feature extraction inherently encodes degradation-carrying information, and a symmetric U-Net architecture is sufficient to unleash these cues effectively. By aligning feature scales across encoder-decoder and enabling streamlined cross-scale propagation, our symmetric design preserves intrinsic degradation signals robustly, rendering simple additive fusion in skip connections sufficient for state-of-the-art performance. Our primary baseline, SymUNet, is built on this symmetric U-Net and achieves better results across benchmark datasets than existing approaches while reducing computational cost. We further propose a semantic enhanced variant, SE-SymUNet, which integrates direct semantic injection from frozen CLIP features via simple cross-attention to explicitly amplify degradation priors. Extensive experiments on several benchmarks validate the superiority of our methods. Both baselines SymUNet and SE-SymUNet establish simpler and stronger foundations for future advancements in all-in-one image restoration. The source code is available at https://github.com/WenlongJiao/SymUNet.

