---
layout: default
title: Nighttime Hazy Image Enhancement via Progressively and Mutually Reinforcing Night-Haze Priors
---

# Nighttime Hazy Image Enhancement via Progressively and Mutually Reinforcing Night-Haze Priors
**arXiv**：[2601.01998v1](https://arxiv.org/abs/2601.01998) · [PDF](https://arxiv.org/pdf/2601.01998.pdf)  
**作者**：Chen Zhu, Huiwen Zhang, Mu He, Yujie Li, Xiaotian Qiao  

**一句话要点**：提出渐进互增强夜雾先验框架以提升夜间有雾图像可见度

**关键词**：夜间去雾, 低光增强, 渐进恢复, 频域感知, 图像增强, 先验互增强

## 3 点简述
- 核心问题：夜间有雾图像因复杂退化分布导致可见度提升困难，现有方法忽略退化类型间交互。
- 方法要点：利用图像、块、像素级专家在视觉和频域渐进恢复结构，通过频域感知路由器自适应引导。
- 实验或效果：在夜间去雾基准上表现优异，并展示在白天去雾和低光增强任务中的泛化能力。

## 摘要（原文）

> Enhancing the visibility of nighttime hazy images is challenging due to the complex degradation distributions. Existing methods mainly address a single type of degradation (e.g., haze or low-light) at a time, ignoring the interplay of different degradation types and resulting in limited visibility improvement. We observe that the domain knowledge shared between low-light and haze priors can be reinforced mutually for better visibility. Based on this key insight, in this paper, we propose a novel framework that enhances visibility in nighttime hazy images by reinforcing the intrinsic consistency between haze and low-light priors mutually and progressively. In particular, our model utilizes image-, patch-, and pixel-level experts that operate across visual and frequency domains to recover global scene structure, regional patterns, and fine-grained details progressively. A frequency-aware router is further introduced to adaptively guide the contribution of each expert, ensuring robust image restoration. Extensive experiments demonstrate the superior performance of our model on nighttime dehazing benchmarks both quantitatively and qualitatively. Moreover, we showcase the generalizability of our model in daytime dehazing and low-light enhancement tasks.

