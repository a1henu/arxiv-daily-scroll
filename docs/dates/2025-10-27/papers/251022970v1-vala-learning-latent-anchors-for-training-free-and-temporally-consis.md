---
layout: default
title: VALA: Learning Latent Anchors for Training-Free and Temporally Consistent
---

# VALA: Learning Latent Anchors for Training-Free and Temporally Consistent
**arXiv**：[2510.22970v1](https://arxiv.org/abs/2510.22970) · [PDF](https://arxiv.org/pdf/2510.22970.pdf)  
**作者**：Zhangkai Wu, Xuhui Fan, Zhongyuan Xie, Kaize Shi, Longbing Cao  

**一句话要点**：提出VALA以解决训练免费视频编辑中的时间一致性问题

**关键词**：训练免费视频编辑, 变分对齐, 潜在锚点, 时间一致性, 对比学习, DDIM反演

## 3 点简述
- 现有方法依赖启发式帧选择，导致手动偏差和可扩展性差
- VALA使用变分对齐模块自适应选择关键帧并压缩潜在特征为语义锚点
- 实验显示在真实视频编辑基准上实现高保真、高质量和高效性能

## 摘要（原文）

> Recent advances in training-free video editing have enabled lightweight and
> precise cross-frame generation by leveraging pre-trained text-to-image
> diffusion models. However, existing methods often rely on heuristic frame
> selection to maintain temporal consistency during DDIM inversion, which
> introduces manual bias and reduces the scalability of end-to-end inference. In
> this paper, we propose~\textbf{VALA} (\textbf{V}ariational \textbf{A}lignment
> for \textbf{L}atent \textbf{A}nchors), a variational alignment module that
> adaptively selects key frames and compresses their latent features into
> semantic anchors for consistent video editing. To learn meaningful assignments,
> VALA propose a variational framework with a contrastive learning objective.
> Therefore, it can transform cross-frame latent representations into compressed
> latent anchors that preserve both content and temporal coherence. Our method
> can be fully integrated into training-free text-to-image based video editing
> models. Extensive experiments on real-world video editing benchmarks show that
> VALA achieves state-of-the-art performance in inversion fidelity, editing
> quality, and temporal consistency, while offering improved efficiency over
> prior methods.

