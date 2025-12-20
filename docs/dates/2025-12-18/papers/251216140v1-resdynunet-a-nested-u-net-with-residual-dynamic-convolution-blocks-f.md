---
layout: default
title: ResDynUNet++: A nested U-Net with residual dynamic convolution blocks for dual-spectral CT
---

# ResDynUNet++: A nested U-Net with residual dynamic convolution blocks for dual-spectral CT
**arXiv**：[2512.16140v1](https://arxiv.org/abs/2512.16140) · [PDF](https://arxiv.org/pdf/2512.16140.pdf)  
**作者**：Ze Yuan, Wenbin Li, Shusen Zhao  

**一句话要点**：提出ResDynUNet++，一种结合知识驱动与数据驱动的混合框架，用于双能CT重建以解决通道不平衡和伪影问题。

**关键词**：双能CT重建, 混合框架, 残差动态卷积, UNet++, 知识驱动, 数据驱动

## 3 点简述
- 核心问题：双能CT重建中通道不平衡和近界面大伪影的挑战。
- 方法要点：采用OPMT快速生成中间解，再通过ResDynUNet++网络进行精炼，该网络基于UNet++并引入残差动态卷积块。
- 实验或效果：在合成体模和真实临床数据集上验证了方法的有效性和优越性能。

## 摘要（原文）

> We propose a hybrid reconstruction framework for dual-spectral CT (DSCT) that integrates iterative methods with deep learning models. The reconstruction process consists of two complementary components: a knowledge-driven module and a data-driven module. In the knowledge-driven phase, we employ the oblique projection modification technique (OPMT) to reconstruct an intermediate solution of the basis material images from the projection data. We select OPMT for this role because of its fast convergence, which allows it to rapidly generate an intermediate solution that successfully achieves basis material decomposition. Subsequently, in the data-driven phase, we introduce a novel neural network, ResDynUNet++, to refine this intermediate solution. The ResDynUNet++ is built upon a UNet++ backbone by replacing standard convolutions with residual dynamic convolution blocks, which combine the adaptive, input-specific feature extraction of dynamic convolution with the stable training of residual connections. This architecture is designed to address challenges like channel imbalance and near-interface large artifacts in DSCT, producing clean and accurate final solutions. Extensive experiments on both synthetic phantoms and real clinical datasets validate the efficacy and superior performance of the proposed method.

