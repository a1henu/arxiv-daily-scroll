---
layout: default
title: InvCoSS: Inversion-driven Continual Self-supervised Learning in Medical Multi-modal Image Pre-training
---

# InvCoSS: Inversion-driven Continual Self-supervised Learning in Medical Multi-modal Image Pre-training
**arXiv**：[2512.19213v1](https://arxiv.org/abs/2512.19213) · [PDF](https://arxiv.org/pdf/2512.19213.pdf)  
**作者**：Zihao Luo, Shaohao Rui, Zhenyu Tang, Guotai Wang, Xiaosong Wang  

**一句话要点**：提出InvCoSS框架，通过模型反演生成合成图像，解决医学多模态图像持续自监督学习中的数据隐私和遗忘问题。

**关键词**：持续自监督学习, 医学多模态图像, 模型反演, 合成图像生成, 隐私保护, 灾难性遗忘

## 3 点简述
- 核心问题：现有持续自监督学习方法依赖重放真实数据，导致隐私泄露和跨站点数据转移受限。
- 方法要点：使用InvUNet多尺度融合架构生成高保真合成图像，结合排斥表示学习机制增强多样性，避免模式崩溃。
- 实验或效果：在九个下游任务中验证，性能媲美或优于数据重放方法，显著减少存储需求并消除隐私约束。

## 摘要（原文）

> Continual self-supervised learning (CSSL) in medical imaging trains a foundation model sequentially, alleviating the need for collecting multi-modal images for joint training and offering promising improvements in downstream performance while preserving data privacy. However, most existing methods still rely on replaying data from previous stages to prevent catastrophic forgetting, which compromises privacy and limits their applicability in real-world scenarios where data transfer across sites is often restricted. In this work, we propose InvCoSS, an inversion-driven continual self-supervised learning framework for medical multi-modal image pre-training. Specifically, after training on a previous task, InvCoSS inverts the pre-trained self-supervised model to generate synthetic images that approximate the original training distribution. These synthetic images are then combined with data from the new task for joint optimization, which effectively mitigates catastrophic forgetting while strictly adhering to the constraint of no access to previous real data. Furthermore, to improve the fidelity of synthetic images, we introduce a novel InvUNet with a multi-scale fusion architecture to restore both high- and low-frequency components of the inverted images. To enhance diversity and prevent mode collapse, we design a repulsive representation-learning mechanism that encourages a diverse feature space for synthetic images without class guidance. Extensive experiments across nine downstream tasks validate the effectiveness of InvCoSS, achieving performance comparable to or even superior to prior data-replay methods while significantly reducing storage requirements and eliminating data privacy constraints.

