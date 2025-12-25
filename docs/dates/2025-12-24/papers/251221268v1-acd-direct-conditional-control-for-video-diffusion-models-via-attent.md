---
layout: default
title: ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision
---

# ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision
**arXiv**：[2512.21268v1](https://arxiv.org/abs/2512.21268) · [PDF](https://arxiv.org/pdf/2512.21268.pdf)  
**作者**：Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  

**一句话要点**：提出ACD框架，通过注意力监督实现视频扩散模型的直接条件控制

**关键词**：视频扩散模型, 条件控制, 注意力监督, 布局控制, 视频合成

## 3 点简述
- 现有方法如无分类器引导或基于分类器引导存在条件对齐不足或对抗伪影问题
- ACD通过将模型注意力图与外部控制信号对齐，实现更精确的条件控制
- 实验表明ACD在基准数据集上提升条件对齐，同时保持时间一致性和视觉保真度

## 摘要（原文）

> Controllability is a fundamental requirement in video synthesis, where accurate alignment with conditioning signals is essential. Existing classifier-free guidance methods typically achieve conditioning indirectly by modeling the joint distribution of data and conditions, which often results in limited controllability over the specified conditions. Classifier-based guidance enforces conditions through an external classifier, but the model may exploit this mechanism to raise the classifier score without genuinely satisfying the intended condition, resulting in adversarial artifacts and limited effective controllability. In this paper, we propose Attention-Conditional Diffusion (ACD), a novel framework for direct conditional control in video diffusion models via attention supervision. By aligning the model's attention maps with external control signals, ACD achieves better controllability. To support this, we introduce a sparse 3D-aware object layout as an efficient conditioning signal, along with a dedicated Layout ControlNet and an automated annotation pipeline for scalable layout integration. Extensive experiments on benchmark video generation datasets demonstrate that ACD delivers superior alignment with conditioning inputs while preserving temporal coherence and visual fidelity, establishing an effective paradigm for conditional video synthesis.

