---
layout: default
title: FarmMind: Reasoning-Query-Driven Dynamic Segmentation for Farmland Remote Sensing Images
---

# FarmMind: Reasoning-Query-Driven Dynamic Segmentation for Farmland Remote Sensing Images
**arXiv**：[2601.22809v1](https://arxiv.org/abs/2601.22809) · [PDF](https://arxiv.org/pdf/2601.22809.pdf)  
**作者**：Haiyang Wu, Weiliang Mu, Jipeng Zhang, Zhong Dandan, Zhuofei Du, Haifeng Li, Tao Chao  

**一句话要点**：提出FarmMind框架，通过推理查询机制动态分割农田遥感图像以解决模糊场景问题。

**关键词**：农田遥感图像分割, 动态分割框架, 推理查询机制, 模糊场景处理, 辅助图像查询

## 3 点简述
- 现有农田遥感图像分割方法依赖单张图像，处理模糊场景时推理能力受限。
- FarmMind引入推理查询机制，模拟专家思维，动态查询辅助图像以补偿信息不足。
- 实验表明FarmMind在分割性能和泛化能力上优于现有方法，代码和数据集已公开。

## 摘要（原文）

> Existing methods for farmland remote sensing image (FRSI) segmentation generally follow a static segmentation paradigm, where analysis relies solely on the limited information contained within a single input patch. Consequently, their reasoning capability is limited when dealing with complex scenes characterized by ambiguity and visual uncertainty. In contrast, human experts, when interpreting remote sensing images in such ambiguous cases, tend to actively query auxiliary images (such as higher-resolution, larger-scale, or temporally adjacent data) to conduct cross-verification and achieve more comprehensive reasoning. Inspired by this, we propose a reasoning-query-driven dynamic segmentation framework for FRSIs, named FarmMind. This framework breaks through the limitations of the static segmentation paradigm by introducing a reasoning-query mechanism, which dynamically and on-demand queries external auxiliary images to compensate for the insufficient information in a single input image. Unlike direct queries, this mechanism simulates the thinking process of human experts when faced with segmentation ambiguity: it first analyzes the root causes of segmentation ambiguities through reasoning, and then determines what type of auxiliary image needs to be queried based on this analysis. Extensive experiments demonstrate that FarmMind achieves superior segmentation performance and stronger generalization ability compared with existing methods. The source code and dataset used in this work are publicly available at: https://github.com/WithoutOcean/FarmMind.

