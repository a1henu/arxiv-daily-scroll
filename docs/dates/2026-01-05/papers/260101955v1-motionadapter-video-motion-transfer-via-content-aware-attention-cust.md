---
layout: default
title: MotionAdapter: Video Motion Transfer via Content-Aware Attention Customization
---

# MotionAdapter: Video Motion Transfer via Content-Aware Attention Customization
**arXiv**：[2601.01955v1](https://arxiv.org/abs/2601.01955) · [PDF](https://arxiv.org/pdf/2601.01955.pdf)  
**作者**：Zhexin Zhang, Yifeng Zhu, Yangyang Xu, Long Chen, Yong Du, Shengfeng He, Jun Yu  

**一句话要点**：提出MotionAdapter框架，通过内容感知注意力定制实现视频运动迁移

**关键词**：视频运动迁移, 扩散变换器, 注意力机制, 内容感知定制, 运动编辑

## 3 点简述
- 核心问题：基于扩散的视频生成模型难以在视频间迁移复杂运动
- 方法要点：利用3D全注意力模块提取运动场，结合DINO引导定制以适应目标内容
- 实验或效果：在定性和定量评估中优于现有方法，支持复杂运动迁移和编辑

## 摘要（原文）

> Recent advances in diffusion-based text-to-video models, particularly those built on the diffusion transformer architecture, have achieved remarkable progress in generating high-quality and temporally coherent videos. However, transferring complex motions between videos remains challenging. In this work, we present MotionAdapter, a content-aware motion transfer framework that enables robust and semantically aligned motion transfer within DiT-based T2V models. Our key insight is that effective motion transfer requires \romannumeral1) explicit disentanglement of motion from appearance and \romannumeral 2) adaptive customization of motion to target content. MotionAdapter first isolates motion by analyzing cross-frame attention within 3D full-attention modules to extract attention-derived motion fields. To bridge the semantic gap between reference and target videos, we further introduce a DINO-guided motion customization module that rearranges and refines motion fields based on content correspondences. The customized motion field is then used to guide the DiT denoising process, ensuring that the synthesized video inherits the reference motion while preserving target appearance and semantics. Extensive experiments demonstrate that MotionAdapter outperforms state-of-the-art methods in both qualitative and quantitative evaluations. Moreover, MotionAdapter naturally supports complex motion transfer and motion editing tasks such as zooming.

