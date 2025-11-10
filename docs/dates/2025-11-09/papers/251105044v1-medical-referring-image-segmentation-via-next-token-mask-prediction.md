---
layout: default
title: Medical Referring Image Segmentation via Next-Token Mask Prediction
---

# Medical Referring Image Segmentation via Next-Token Mask Prediction
**arXiv**：[2511.05044v1](https://arxiv.org/abs/2511.05044) · [PDF](https://arxiv.org/pdf/2511.05044.pdf)  
**作者**：Xinyu Chen, Yiran Wang, Gaoyang Pang, Jiafu Hao, Chentao Yue, Luping Zhou, Yonghui Li  

**一句话要点**：提出NTP-MRISeg框架，将医学参考图像分割重构为自回归下一令牌预测任务。

**关键词**：医学图像分割, 多模态学习, 自回归预测, 令牌级对比学习, 下一令牌预测, 端到端训练

## 3 点简述
- 医学参考图像分割需基于自然语言描述分割目标区域，现有方法多模态融合复杂。
- 采用统一多模态序列自回归预测，无需模态特定融合，引入NkTP、TCL和HET策略优化。
- 在QaTa-COV19和MosMedData+数据集上实现新SOTA性能，验证框架有效性。

## 摘要（原文）

> Medical Referring Image Segmentation (MRIS) involves segmenting target
> regions in medical images based on natural language descriptions. While
> achieving promising results, recent approaches usually involve complex design
> of multimodal fusion or multi-stage decoders. In this work, we propose
> NTP-MRISeg, a novel framework that reformulates MRIS as an autoregressive
> next-token prediction task over a unified multimodal sequence of tokenized
> image, text, and mask representations. This formulation streamlines model
> design by eliminating the need for modality-specific fusion and external
> segmentation models, supports a unified architecture for end-to-end training.
> It also enables the use of pretrained tokenizers from emerging large-scale
> multimodal models, enhancing generalization and adaptability. More importantly,
> to address challenges under this formulation-such as exposure bias, long-tail
> token distributions, and fine-grained lesion edges-we propose three novel
> strategies: (1) a Next-k Token Prediction (NkTP) scheme to reduce cumulative
> prediction errors, (2) Token-level Contrastive Learning (TCL) to enhance
> boundary sensitivity and mitigate long-tail distribution effects, and (3) a
> memory-based Hard Error Token (HET) optimization strategy that emphasizes
> difficult tokens during training. Extensive experiments on the QaTa-COV19 and
> MosMedData+ datasets demonstrate that NTP-MRISeg achieves new state-of-the-art
> performance, offering a streamlined and effective alternative to traditional
> MRIS pipelines.

