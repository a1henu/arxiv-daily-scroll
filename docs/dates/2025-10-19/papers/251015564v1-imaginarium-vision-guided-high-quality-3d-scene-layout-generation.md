---
layout: default
title: Imaginarium: Vision-guided High-Quality 3D Scene Layout Generation
---

# Imaginarium: Vision-guided High-Quality 3D Scene Layout Generation
**arXiv**：[2510.15564v1](https://arxiv.org/abs/2510.15564) · [PDF](https://arxiv.org/pdf/2510.15564.pdf)  
**作者**：Xiaoming Zhu, Xu Huang, Qinghongbing Xie, Zhi Deng, Junsheng Yu, Yirui Guan, Zhongyuan Liu, Lin Zhu, Qijun Zhao, Ligang Liu, Long Zeng  

**一句话要点**：提出视觉引导3D场景布局生成系统以解决传统方法在丰富性和空间关系上的不足

**关键词**：3D场景布局生成, 视觉引导系统, 图像解析, 场景图优化, 资产库构建

## 3 点简述
- 核心问题：传统优化方法依赖手动规则，生成模型缺乏丰富性，语言模型难以捕捉复杂空间关系。
- 方法要点：构建高质量资产库，扩展提示为图像并微调，开发图像解析模块恢复3D布局，优化场景图确保逻辑一致。
- 实验或效果：用户测试显示在布局丰富性和质量上显著优于现有方法。

## 摘要（原文）

> Generating artistic and coherent 3D scene layouts is crucial in digital
> content creation. Traditional optimization-based methods are often constrained
> by cumbersome manual rules, while deep generative models face challenges in
> producing content with richness and diversity. Furthermore, approaches that
> utilize large language models frequently lack robustness and fail to accurately
> capture complex spatial relationships. To address these challenges, this paper
> presents a novel vision-guided 3D layout generation system. We first construct
> a high-quality asset library containing 2,037 scene assets and 147 3D scene
> layouts. Subsequently, we employ an image generation model to expand prompt
> representations into images, fine-tuning it to align with our asset library. We
> then develop a robust image parsing module to recover the 3D layout of scenes
> based on visual semantics and geometric information. Finally, we optimize the
> scene layout using scene graphs and overall visual semantics to ensure logical
> coherence and alignment with the images. Extensive user testing demonstrates
> that our algorithm significantly outperforms existing methods in terms of
> layout richness and quality. The code and dataset will be available at
> https://github.com/HiHiAllen/Imaginarium.

