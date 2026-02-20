---
layout: default
title: Canonicalizing Multimodal Contrastive Representation Learning
---

# Canonicalizing Multimodal Contrastive Representation Learning
**arXiv**：[2602.17584v1](https://arxiv.org/abs/2602.17584) · [PDF](https://arxiv.org/pdf/2602.17584.pdf)  
**作者**：Sharut Gupta, Sanyam Kansal, Stefanie Jegelka, Phillip Isola, Vikas Garg  

**一句话要点**：提出多模态对比表示学习的正交映射规范化，以对齐独立训练模型间的表示空间。

**关键词**：多模态对比学习, 表示空间对齐, 正交映射, 模型规范化, 向后兼容性, 隐私保护

## 3 点简述
- 核心问题：独立训练的多模态对比模型间是否存在系统几何关系，能否统一对齐图像和文本编码器。
- 方法要点：证明模型间关系近似为正交映射，理论推导基于多模态核在锚点集上的一致性。
- 实验或效果：在CLIP、SigLIP和FLAVA等模型家族中验证正交映射有效性，支持向后兼容升级和隐私应用。

## 摘要（原文）

> As models and data scale, independently trained networks often induce analogous notions of similarity. But, matching similarities is weaker than establishing an explicit correspondence between the representation spaces, especially for multimodal models, where consistency must hold not only within each modality, but also for the learned image-text coupling. We therefore ask: given two independently trained multimodal contrastive models (with encoders $(f, g)$ and $(\widetilde{f},\widetilde{g})$) -- trained on different distributions and with different architectures -- does a systematic geometric relationship exist between their embedding spaces? If so, what form does it take, and does it hold uniformly across modalities? In this work, we show that across model families such as CLIP, SigLIP, and FLAVA, this geometric relationship is well approximated by an orthogonal map (up to a global mean shift), i.e., there exists an orthogonal map $Q$ where $Q^\top Q = I$ such that $\widetilde{f}(x)\approx Q f(x)$ for paired images $x$. Strikingly, the same $Q$ simultaneously aligns the text encoders i.e., $\widetilde{g}(y)\approx Q g(y)$ for texts $y$. Theoretically, we prove that if the multimodal kernel agrees across models on a small anchor set i.e. $\langle f(x), g(y)\rangle \approx \langle \widetilde{f}(x), \widetilde{g}(y)\rangle$, then the two models must be related by a single orthogonal map $Q$ and the same $Q$ maps images and text across models. More broadly, this finding enables backward-compatible model upgrades, avoiding costly re-embedding, and has implications for the privacy of learned representations.
>   Our project page: https://canonical-multimodal.github.io/

