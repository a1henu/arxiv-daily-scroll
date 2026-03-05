---
layout: default
title: Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On
---

# Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On
**arXiv**：[2603.04290v1](https://arxiv.org/abs/2603.04290) · [PDF](https://arxiv.org/pdf/2603.04290.pdf)  
**作者**：Zhiyi Chen, Hsuan-I Ho, Tianjian Jiang, Jie Song, Manuel Kaufmann, Chen Guo  

**一句话要点**：提出Gaussian Wardrobe框架，通过分解式3D高斯表示实现自由形式虚拟试穿

**关键词**：3D高斯表示, 分解式神经化身, 虚拟试穿, 多视角视频数字化, 自由形式衣物建模, 姿态合成

## 3 点简述
- 核心问题：现有3D神经化身方法将人体与衣物视为不可分实体，难以建模复杂自由形式衣物动态并限制衣物跨个体重用。
- 方法要点：开发分解式3D高斯表示，从多视角视频中解耦衣物层并规范化为形状无关空间，构建多层自由形式衣物的化身。
- 实验或效果：在新型姿态合成基准上实现最先进性能，建模高保真动态的真实感化身，并支持衣物自由转移到新主体的虚拟试穿应用。

## 摘要（原文）

> We introduce Gaussian Wardrobe, a novel framework to digitalize compositional 3D neural avatars from multi-view videos. Existing methods for 3D neural avatars typically treat the human body and clothing as an inseparable entity. However, this paradigm fails to capture the dynamics of complex free-form garments and limits the reuse of clothing across different individuals. To overcome these problems, we develop a novel, compositional 3D Gaussian representation to build avatars from multiple layers of free-form garments. The core of our method is decomposing neural avatars into bodies and layers of shape-agnostic neural garments. To achieve this, our framework learns to disentangle each garment layer from multi-view videos and canonicalizes it into a shape-independent space. In experiments, our method models photorealistic avatars with high-fidelity dynamics, achieving new state-of-the-art performance on novel pose synthesis benchmarks. In addition, we demonstrate that the learned compositional garments contribute to a versatile digital wardrobe, enabling a practical virtual try-on application where clothing can be freely transferred to new subjects. Project page: https://ait.ethz.ch/gaussianwardrobe

