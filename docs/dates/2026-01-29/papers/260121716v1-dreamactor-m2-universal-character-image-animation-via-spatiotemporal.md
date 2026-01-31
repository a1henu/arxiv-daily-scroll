---
layout: default
title: DreamActor-M2: Universal Character Image Animation via Spatiotemporal In-Context Learning
---

# DreamActor-M2: Universal Character Image Animation via Spatiotemporal In-Context Learning
**arXiv**：[2601.21716v1](https://arxiv.org/abs/2601.21716) · [PDF](https://arxiv.org/pdf/2601.21716.pdf)  
**作者**：Mingshuang Luo, Shuang Liang, Zhengkun Rong, Yuxuan Luo, Tianshu Hu, Ruibing Hou, Hong Chang, Yong Li, Yuan Zhang, Mingyuan Gao  

**一句话要点**：提出DreamActor-M2框架，通过时空上下文学习实现通用角色图像动画

**关键词**：角色图像动画, 时空上下文学习, RGB驱动动画, 跨域泛化, 基准评估

## 3 点简述
- 核心问题：现有方法在身份保持与运动一致性间存在权衡，且过度依赖显式姿态先验，限制泛化能力
- 方法要点：采用两阶段范式，融合外观与运动线索到统一潜在空间，并引入自引导数据合成管道实现RGB驱动动画
- 实验或效果：在AW Bench基准上实现最先进性能，提升视觉保真度和跨域泛化能力

## 摘要（原文）

> Character image animation aims to synthesize high-fidelity videos by transferring motion from a driving sequence to a static reference image. Despite recent advancements, existing methods suffer from two fundamental challenges: (1) suboptimal motion injection strategies that lead to a trade-off between identity preservation and motion consistency, manifesting as a "see-saw", and (2) an over-reliance on explicit pose priors (e.g., skeletons), which inadequately capture intricate dynamics and hinder generalization to arbitrary, non-humanoid characters. To address these challenges, we present DreamActor-M2, a universal animation framework that reimagines motion conditioning as an in-context learning problem. Our approach follows a two-stage paradigm. First, we bridge the input modality gap by fusing reference appearance and motion cues into a unified latent space, enabling the model to jointly reason about spatial identity and temporal dynamics by leveraging the generative prior of foundational models. Second, we introduce a self-bootstrapped data synthesis pipeline that curates pseudo cross-identity training pairs, facilitating a seamless transition from pose-dependent control to direct, end-to-end RGB-driven animation. This strategy significantly enhances generalization across diverse characters and motion scenarios. To facilitate comprehensive evaluation, we further introduce AW Bench, a versatile benchmark encompassing a wide spectrum of characters types and motion scenarios. Extensive experiments demonstrate that DreamActor-M2 achieves state-of-the-art performance, delivering superior visual fidelity and robust cross-domain generalization. Project Page: https://grisoon.github.io/DreamActor-M2/

