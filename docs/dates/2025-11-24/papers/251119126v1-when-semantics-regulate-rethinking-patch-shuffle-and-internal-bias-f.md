---
layout: default
title: When Semantics Regulate: Rethinking Patch Shuffle and Internal Bias for Generated Image Detection with CLIP
---

# When Semantics Regulate: Rethinking Patch Shuffle and Internal Bias for Generated Image Detection with CLIP
**arXiv**：[2511.19126v1](https://arxiv.org/abs/2511.19126) · [PDF](https://arxiv.org/pdf/2511.19126.pdf)  
**作者**：Beilin Chu, Weike You, Mengtao Li, Tingting Zheng, Kehan Zhao, Xuan Xu, Zhigao Lu, Jia Song, Moxuan Xu, Linna Zhou  

**一句话要点**：提出SemAnti语义对抗微调范式，以提升CLIP在AI生成图像检测中的跨域鲁棒性。

**关键词**：AI生成图像检测, CLIP模型, 语义偏差, Patch Shuffle, 跨域泛化, 微调范式

## 3 点简述
- 核心问题：CLIP检测器依赖语义线索，在分布偏移下性能脆弱。
- 方法要点：通过Patch Shuffle抑制语义偏差，仅微调伪影敏感层。
- 实验或效果：在AIGCDetectBenchmark和GenImage上实现SOTA跨域泛化。

## 摘要（原文）

> The rapid progress of GANs and Diffusion Models poses new challenges for detecting AI-generated images. Although CLIP-based detectors exhibit promising generalization, they often rely on semantic cues rather than generator artifacts, leading to brittle performance under distribution shifts. In this work, we revisit the nature of semantic bias and uncover that Patch Shuffle provides an unusually strong benefit for CLIP, that disrupts global semantic continuity while preserving local artifact cues, which reduces semantic entropy and homogenizes feature distributions between natural and synthetic images. Through a detailed layer-wise analysis, we further show that CLIP's deep semantic structure functions as a regulator that stabilizes cross-domain representations once semantic bias is suppressed. Guided by these findings, we propose SemAnti, a semantic-antagonistic fine-tuning paradigm that freezes the semantic subspace and adapts only artifact-sensitive layers under shuffled semantics. Despite its simplicity, SemAnti achieves state-of-the-art cross-domain generalization on AIGCDetectBenchmark and GenImage, demonstrating that regulating semantics is key to unlocking CLIP's full potential for robust AI-generated image detection.

