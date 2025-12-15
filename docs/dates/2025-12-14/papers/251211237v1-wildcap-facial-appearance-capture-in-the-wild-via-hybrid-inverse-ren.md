---
layout: default
title: WildCap: Facial Appearance Capture in the Wild via Hybrid Inverse Rendering
---

# WildCap: Facial Appearance Capture in the Wild via Hybrid Inverse Rendering
**arXiv**：[2512.11237v1](https://arxiv.org/abs/2512.11237) · [PDF](https://arxiv.org/pdf/2512.11237.pdf)  
**作者**：Yuxuan Han, Xin Ming, Tianxiao Li, Zhuofan Shen, Qixuan Zhang, Lan Xu, Feng Xu  

**一句话要点**：提出WildCap方法，通过混合逆渲染在野外智能手机视频中实现高质量面部外观捕捉。

**关键词**：面部外观捕捉, 混合逆渲染, 野外捕获, 智能手机视频, 光照分离, 纹理网格模型

## 3 点简述
- 现有方法在可控光照下实现高质量面部捕捉，但野外捕获成本高且受限。
- 采用混合逆渲染框架，先数据驱动转换图像，再模型优化，解决光照与材质分离问题。
- 提出纹理网格光照模型，结合扩散先验优化，显著提升野外捕获质量，缩小与可控记录的差距。

## 摘要（原文）

> Existing methods achieve high-quality facial appearance capture under controllable lighting, which increases capture cost and limits usability. We propose WildCap, a novel method for high-quality facial appearance capture from a smartphone video recorded in the wild. To disentangle high-quality reflectance from complex lighting effects in in-the-wild captures, we propose a novel hybrid inverse rendering framework. Specifically, we first apply a data-driven method, i.e., SwitchLight, to convert the captured images into more constrained conditions and then adopt model-based inverse rendering. However, unavoidable local artifacts in network predictions, such as shadow-baking, are non-physical and thus hinder accurate inverse rendering of lighting and material. To address this, we propose a novel texel grid lighting model to explain non-physical effects as clean albedo illuminated by local physical lighting. During optimization, we jointly sample a diffusion prior for reflectance maps and optimize the lighting, effectively resolving scale ambiguity between local lights and albedo. Our method achieves significantly better results than prior arts in the same capture setup, closing the quality gap between in-the-wild and controllable recordings by a large margin. Our code will be released \href{https://yxuhan.github.io/WildCap/index.html}{\textcolor{magenta}{here}}.

