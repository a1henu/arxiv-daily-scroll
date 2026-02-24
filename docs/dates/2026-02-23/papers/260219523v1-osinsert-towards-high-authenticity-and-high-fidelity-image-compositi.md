---
layout: default
title: OSInsert: Towards High-authenticity and High-fidelity Image Composition
---

# OSInsert: Towards High-authenticity and High-fidelity Image Composition
**arXiv**：[2602.19523v1](https://arxiv.org/abs/2602.19523) · [PDF](https://arxiv.org/pdf/2602.19523.pdf)  
**作者**：Jingyuan Wang, Li Niu  

**一句话要点**：提出OSInsert两阶段策略，实现高真实性与高保真度的图像合成

**关键词**：图像合成, 生成对抗网络, 两阶段策略, 高真实性, 高保真度, 前景背景融合

## 3 点简述
- 核心问题：现有方法难以同时实现图像合成的高真实性与高保真度
- 方法要点：第一阶段用高真实性方法生成合理前景形状，作为第二阶段高保真方法的条件
- 实验或效果：在MureCOM数据集上验证了两阶段策略的有效性，代码模型已开源

## 摘要（原文）

> Generative image composition aims to regenerate the given foreground object in the background image to produce a realistic composite image. Some high-authenticity methods can adjust foreground pose/view to be compatible with background, while some high-fidelity methods can preserve the foreground details accurately. However, existing methods can hardly achieve both goals at the same time. In this work, we propose a two-stage strategy to achieve both goals. In the first stage, we use high-authenticity method to generate reasonable foreground shape, serving as the condition of high-fidelity method in the second stage. The experiments on MureCOM dataset verify the effectiveness of our two-stage strategy. The code and model have been released at https://github.com/bcmi/OSInsert-Image-Composition.

