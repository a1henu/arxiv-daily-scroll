---
layout: default
title: ELITE: Efficient Gaussian Head Avatar from a Monocular Video via Learned Initialization and TEst-time Generative Adaptation
---

# ELITE: Efficient Gaussian Head Avatar from a Monocular Video via Learned Initialization and TEst-time Generative Adaptation
**arXiv**：[2601.10200v1](https://arxiv.org/abs/2601.10200) · [PDF](https://arxiv.org/pdf/2601.10200.pdf)  
**作者**：Kim Youwang, Lee Hyoseok, Subin Park, Gerard Pons-Moll, Tae-Hyun Oh  

**一句话要点**：提出ELITE方法，通过学习初始化和测试时生成适应，从单目视频高效合成高斯头部化身。

**关键词**：高斯化身合成, 单目视频, 测试时适应, 扩散增强, 网格到高斯先验, 高效渲染

## 3 点简述
- 核心问题：单目视频缺少视觉线索，现有方法泛化差或计算重且易产生身份幻觉。
- 方法要点：结合3D和2D先验，使用前馈网格到高斯先验模型快速初始化，并设计渲染引导的单步扩散增强器进行测试时适应。
- 实验或效果：在挑战性表情下生成视觉更优化身，合成速度比2D生成先验方法快60倍。

## 摘要（原文）

> We introduce ELITE, an Efficient Gaussian head avatar synthesis from a monocular video via Learned Initialization and TEst-time generative adaptation. Prior works rely either on a 3D data prior or a 2D generative prior to compensate for missing visual cues in monocular videos. However, 3D data prior methods often struggle to generalize in-the-wild, while 2D generative prior methods are computationally heavy and prone to identity hallucination. We identify a complementary synergy between these two priors and design an efficient system that achieves high-fidelity animatable avatar synthesis with strong in-the-wild generalization. Specifically, we introduce a feed-forward Mesh2Gaussian Prior Model (MGPM) that enables fast initialization of a Gaussian avatar. To further bridge the domain gap at test time, we design a test-time generative adaptation stage, leveraging both real and synthetic images as supervision. Unlike previous full diffusion denoising strategies that are slow and hallucination-prone, we propose a rendering-guided single-step diffusion enhancer that restores missing visual details, grounded on Gaussian avatar renderings. Our experiments demonstrate that ELITE produces visually superior avatars to prior works, even for challenging expressions, while achieving 60x faster synthesis than the 2D generative prior method.

