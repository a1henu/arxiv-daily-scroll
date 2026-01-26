---
layout: default
title: AnchoredDream: Zero-Shot 360° Indoor Scene Generation from a Single View via Geometric Grounding
---

# AnchoredDream: Zero-Shot 360° Indoor Scene Generation from a Single View via Geometric Grounding
**arXiv**：[2601.16532v1](https://arxiv.org/abs/2601.16532) · [PDF](https://arxiv.org/pdf/2601.16532.pdf)  
**作者**：Runmao Yao, Junsheng Zhou, Zhen Dong, Yu-Shen Liu  

**一句话要点**：提出AnchoredDream，通过几何锚定实现零样本单视图360°室内场景生成

**关键词**：单视图场景生成, 零样本学习, 几何锚定, 扩散模型, 室内场景, 360°全景

## 3 点简述
- 核心问题：单视图生成360°场景存在外观一致性和几何合理性挑战
- 方法要点：基于外观-几何互促机制，先构建3D布局再渐进生成完整场景
- 实验或效果：在零样本设置下，外观一致性和几何合理性大幅超越现有方法

## 摘要（原文）

> Single-view indoor scene generation plays a crucial role in a range of real-world applications. However, generating a complete 360° scene from a single image remains a highly ill-posed and challenging problem. Recent approaches have made progress by leveraging diffusion models and depth estimation networks, yet they still struggle to maintain appearance consistency and geometric plausibility under large viewpoint changes, limiting their effectiveness in full-scene generation. To address this, we propose AnchoredDream, a novel zero-shot pipeline that anchors 360° scene generation on high-fidelity geometry via an appearance-geometry mutual boosting mechanism. Given a single-view image, our method first performs appearance-guided geometry generation to construct a reliable 3D scene layout. Then, we progressively generate the complete scene through a series of modules: warp-and-inpaint, warp-and-refine, post-optimization, and a novel Grouting Block, which ensures seamless transitions between the input view and generated regions. Extensive experiments demonstrate that AnchoredDream outperforms existing methods by a large margin in both appearance consistency and geometric plausibility--all in a zero-shot manner. Our results highlight the potential of geometric grounding for high-quality, zero-shot single-view scene generation.

