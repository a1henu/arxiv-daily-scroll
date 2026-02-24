---
layout: default
title: SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis
---

# SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis
**arXiv**：[2602.20079v1](https://arxiv.org/abs/2602.20079) · [PDF](https://arxiv.org/pdf/2602.20079.pdf)  
**作者**：Xinya Chen, Christopher Wewer, Jiahao Xie, Xinting Hu, Jan Eric Lenssen  

**一句话要点**：提出SemanticNVS，通过集成预训练语义特征提取器提升生成式新视角合成的语义场景理解

**关键词**：新视角合成, 语义场景理解, 扩散模型, 多视图生成, 相机条件模型

## 3 点简述
- 核心问题：现有新视角合成方法在长距离相机运动下生成语义不合理和扭曲图像，质量严重下降
- 方法要点：集成预训练语义特征提取器，采用扭曲语义特征和交替理解生成策略增强场景语义条件
- 实验或效果：在多个数据集上实现定性和定量改进，FID提升4.69%-15.26%优于现有方法

## 摘要（原文）

> We present SemanticNVS, a camera-conditioned multi-view diffusion model for novel view synthesis (NVS), which improves generation quality and consistency by integrating pre-trained semantic feature extractors. Existing NVS methods perform well for views near the input view, however, they tend to generate semantically implausible and distorted images under long-range camera motion, revealing severe degradation. We speculate that this degradation is due to current models failing to fully understand their conditioning or intermediate generated scene content. Here, we propose to integrate pre-trained semantic feature extractors to incorporate stronger scene semantics as conditioning to achieve high-quality generation even at distant viewpoints. We investigate two different strategies, (1) warped semantic features and (2) an alternating scheme of understanding and generation at each denoising step. Experimental results on multiple datasets demonstrate the clear qualitative and quantitative (4.69%-15.26% in FID) improvement over state-of-the-art alternatives.

