---
layout: default
title: Controlling Your Image via Simplified Vector Graphics
---

# Controlling Your Image via Simplified Vector Graphics
**arXiv**：[2602.14443v1](https://arxiv.org/abs/2602.14443) · [PDF](https://arxiv.org/pdf/2602.14443.pdf)  
**作者**：Lanqing Guo, Xi Liu, Yufei Wang, Zhihao Li, Siyu Huang  

**一句话要点**：提出基于简化矢量图形的分层可控图像生成方法，实现元素级编辑与逼真输出。

**关键词**：可控图像生成, 矢量图形表示, 元素级编辑, 图像合成框架, 噪声预测

## 3 点简述
- 核心问题：图像生成缺乏元素级控制，难以直观调整形状、颜色或对象。
- 方法要点：高效解析图像为语义对齐的矢量图形表示，并设计基于该表示的合成框架。
- 实验或效果：在图像编辑、对象级操纵和细粒度内容创建中验证有效性，建立可控生成新范式。

## 摘要（原文）

> Recent advances in image generation have achieved remarkable visual quality, while a fundamental challenge remains: Can image generation be controlled at the element level, enabling intuitive modifications such as adjusting shapes, altering colors, or adding and removing objects? In this work, we address this challenge by introducing layer-wise controllable generation through simplified vector graphics (VGs). Our approach first efficiently parses images into hierarchical VG representations that are semantic-aligned and structurally coherent. Building on this representation, we design a novel image synthesis framework guided by VGs, allowing users to freely modify elements and seamlessly translate these edits into photorealistic outputs. By leveraging the structural and semantic features of VGs in conjunction with noise prediction, our method provides precise control over geometry, color, and object semantics. Extensive experiments demonstrate the effectiveness of our approach in diverse applications, including image editing, object-level manipulation, and fine-grained content creation, establishing a new paradigm for controllable image generation. Project page: https://guolanqing.github.io/Vec2Pix/

