---
layout: default
title: PI-Light: Physics-Inspired Diffusion for Full-Image Relighting
---

# PI-Light: Physics-Inspired Diffusion for Full-Image Relighting
**arXiv**：[2601.22135v1](https://arxiv.org/abs/2601.22135) · [PDF](https://arxiv.org/pdf/2601.22135.pdf)  
**作者**：Zhexin Liang, Zhaoxi Chen, Yongwei Chen, Tianyi Wei, Tengfei Wang, Xingang Pan  

**一句话要点**：提出PI-Light框架，利用物理启发扩散模型解决全图像重照明的物理合理性和泛化性问题。

**关键词**：全图像重照明, 物理启发扩散模型, 批量感知注意力, 物理引导神经渲染, 泛化性提升, 真实场景编辑

## 3 点简述
- 核心问题：全图像重照明面临数据收集难、物理合理性保持难和数据驱动先验泛化性有限等挑战。
- 方法要点：采用两阶段框架，结合批量感知注意力、物理引导神经渲染模块和物理启发损失，增强物理合理性和一致性。
- 实验或效果：在多样化材料上合成镜面高光和漫反射，相比先前方法在真实场景中实现更优泛化。

## 摘要（原文）

> Full-image relighting remains a challenging problem due to the difficulty of collecting large-scale structured paired data, the difficulty of maintaining physical plausibility, and the limited generalizability imposed by data-driven priors. Existing attempts to bridge the synthetic-to-real gap for full-scene relighting remain suboptimal. To tackle these challenges, we introduce Physics-Inspired diffusion for full-image reLight ($π$-Light, or PI-Light), a two-stage framework that leverages physics-inspired diffusion models. Our design incorporates (i) batch-aware attention, which improves the consistency of intrinsic predictions across a collection of images, (ii) a physics-guided neural rendering module that enforces physically plausible light transport, (iii) physics-inspired losses that regularize training dynamics toward a physically meaningful landscape, thereby enhancing generalizability to real-world image editing, and (iv) a carefully curated dataset of diverse objects and scenes captured under controlled lighting conditions. Together, these components enable efficient finetuning of pretrained diffusion models while also providing a solid benchmark for downstream evaluation. Experiments demonstrate that $π$-Light synthesizes specular highlights and diffuse reflections across a wide variety of materials, achieving superior generalization to real-world scenes compared with prior approaches.

