---
layout: default
title: RecoverMark: Robust Watermarking for Localization and Recovery of Manipulated Faces
---

# RecoverMark: Robust Watermarking for Localization and Recovery of Manipulated Faces
**arXiv**：[2602.20618v1](https://arxiv.org/abs/2602.20618) · [PDF](https://arxiv.org/pdf/2602.20618.pdf)  
**作者**：Haonan An, Xiaohui Ye, Guang Hua, Yihang Tao, Hangcheng Cao, Xiangyu Yu, Yuguang Fang  

**一句话要点**：提出RecoverMark框架，通过将人脸内容作为水印嵌入背景，实现对抗攻击的鲁棒性人脸篡改定位、恢复与所有权验证。

**关键词**：人脸水印, 篡改恢复, 鲁棒性嵌入, 所有权验证, 对抗攻击, 语义一致性

## 3 点简述
- 核心问题：现有脆弱水印方法易受移除攻击，且与鲁棒水印相互干扰，影响篡改检测与恢复效果。
- 方法要点：利用背景语义一致性约束，将人脸内容作为水印嵌入背景，采用两阶段训练和失真层模拟攻击，增强鲁棒性。
- 实验或效果：在多种攻击和分布内外数据上验证了鲁棒性，能同时实现篡改定位、内容恢复和所有权保护。

## 摘要（原文）

> The proliferation of AI-generated content has facilitated sophisticated face manipulation, severely undermining visual integrity and posing unprecedented challenges to intellectual property. In response, a common proactive defense leverages fragile watermarks to detect, localize, or even recover manipulated regions. However, these methods always assume an adversary unaware of the embedded watermark, overlooking their inherent vulnerability to watermark removal attacks. Furthermore, this fragility is exacerbated in the commonly used dual-watermark strategy that adds a robust watermark for image ownership verification, where mutual interference and limited embedding capacity reduce the fragile watermark's effectiveness. To address the gap, we propose RecoverMark, a watermarking framework that achieves robust manipulation localization, content recovery, and ownership verification simultaneously. Our key insight is twofold. First, we exploit a critical real-world constraint: an adversary must preserve the background's semantic consistency to avoid visual detection, even if they apply global, imperceptible watermark removal attacks. Second, using the image's own content (face, in this paper) as the watermark enhances extraction robustness. Based on these insights, RecoverMark treats the protected face content itself as the watermark and embeds it into the surrounding background. By designing a robust two-stage training paradigm with carefully crafted distortion layers that simulate comprehensive potential attacks and a progressive training strategy, RecoverMark achieves a robust watermark embedding in no fragile manner for image manipulation localization, recovery, and image IP protection simultaneously. Extensive experiments demonstrate the proposed RecoverMark's robustness against both seen and unseen attacks and its generalizability to in-distribution and out-of-distribution data.

