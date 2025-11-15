---
layout: default
title: Dynamic Avatar-Scene Rendering from Human-centric Context
---

# Dynamic Avatar-Scene Rendering from Human-centric Context
**arXiv**：[2511.10539v1](https://arxiv.org/abs/2511.10539) · [PDF](https://arxiv.org/pdf/2511.10539.pdf)  
**作者**：Wenqing Wang, Haosen Yang, Josef Kittler, Xiatian Zhu  

**一句话要点**：提出Separate-then-Map策略以解决单目视频中动态人体与场景渲染的空间不一致问题

**关键词**：动态人体重建, 单目视频渲染, 神经渲染, 空间一致性, 高斯属性变换

## 3 点简述
- 核心问题：现有方法忽略人体与场景的独立运动特性，导致重建不完整和边界视觉伪影
- 方法要点：引入信息映射机制，通过共享变换函数统一分离建模的组件，确保空间和视觉一致性
- 实验或效果：在单目视频数据集上，StM在视觉质量和渲染精度上显著优于现有方法，尤其在交互边界

## 摘要（原文）

> Reconstructing dynamic humans interacting with real-world environments from monocular videos is an important and challenging task. Despite considerable progress in 4D neural rendering, existing approaches either model dynamic scenes holistically or model scenes and backgrounds separately aim to introduce parametric human priors. However, these approaches either neglect distinct motion characteristics of various components in scene especially human, leading to incomplete reconstructions, or ignore the information exchange between the separately modeled components, resulting in spatial inconsistencies and visual artifacts at human-scene boundaries. To address this, we propose {\bf Separate-then-Map} (StM) strategy that introduces a dedicated information mapping mechanism to bridge separately defined and optimized models. Our method employs a shared transformation function for each Gaussian attribute to unify separately modeled components, enhancing computational efficiency by avoiding exhaustive pairwise interactions while ensuring spatial and visual coherence between humans and their surroundings. Extensive experiments on monocular video datasets demonstrate that StM significantly outperforms existing state-of-the-art methods in both visual quality and rendering accuracy, particularly at challenging human-scene interaction boundaries.

