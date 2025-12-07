---
layout: default
title: ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching
---

# ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching
**arXiv**：[2512.04904v1](https://arxiv.org/abs/2512.04904) · [PDF](https://arxiv.org/pdf/2512.04904.pdf)  
**作者**：Guanbo Huang, Jingjia Mao, Fanding Huang, Fengkai Liu, Xiangyang Luo, Yaoyuan Liang, Jiasheng Lu, Xiaoe Wang, Pei Liu, Ruiliu Fu, Shao-Lun Huang  

**一句话要点**：提出ReflexFlow以解决流匹配中的曝光偏差问题

**关键词**：流匹配, 曝光偏差, 生成模型, 训练目标, 图像生成

## 3 点简述
- 曝光偏差源于模型泛化不足和低频内容缺失
- 通过抗漂移校正和频率补偿动态调整学习目标
- 在多个数据集上显著提升生成质量，如CelebA-64 FID降低35.65%

## 摘要（原文）

> Despite tremendous recent progress, Flow Matching methods still suffer from exposure bias due to discrepancies in training and inference. This paper investigates the root causes of exposure bias in Flow Matching, including: (1) the model lacks generalization to biased inputs during training, and (2) insufficient low-frequency content captured during early denoising, leading to accumulated bias. Based on these insights, we propose ReflexFlow, a simple and effective reflexive refinement of the Flow Matching learning objective that dynamically corrects exposure bias. ReflexFlow consists of two components: (1) Anti-Drift Rectification (ADR), which reflexively adjusts prediction targets for biased inputs utilizing a redesigned loss under training-time scheduled sampling; and (2) Frequency Compensation (FC), which reflects on missing low-frequency components and compensates them by reweighting the loss using exposure bias. ReflexFlow is model-agnostic, compatible with all Flow Matching frameworks, and improves generation quality across datasets. Experiments on CIFAR-10, CelebA-64, and ImageNet-256 show that ReflexFlow outperforms prior approaches in mitigating exposure bias, achieving a 35.65% reduction in FID on CelebA-64.

