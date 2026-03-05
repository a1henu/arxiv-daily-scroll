---
layout: default
title: UniSync: Towards Generalizable and High-Fidelity Lip Synchronization for Challenging Scenarios
---

# UniSync: Towards Generalizable and High-Fidelity Lip Synchronization for Challenging Scenarios
**arXiv**：[2603.03882v1](https://arxiv.org/abs/2603.03882) · [PDF](https://arxiv.org/pdf/2603.03882.pdf)  
**作者**：Ruidi Fan, Yang Zhou, Siyuan Wang, Tian Yu, Yutong Jiang, Xusheng Liu  

**一句话要点**：提出UniSync统一框架，以解决多样化场景下的唇形同步问题，实现高保真度生成。

**关键词**：唇形同步, 高保真视频生成, 多样化场景处理, 姿态锚定训练, 混合推理策略, 领域适应性微调

## 3 点简述
- 核心问题：现有唇形同步方法存在局部颜色差异或全局背景纹理错位，难以处理多样化真实场景如风格化头像和遮挡。
- 方法要点：采用无掩码姿态锚定训练消除颜色伪影，结合有掩码混合推理确保结构精度和平滑融合，通过小规模多样化视频微调提升领域适应性。
- 实验或效果：在涵盖人脸和风格化头像的RealWorld-LipSync基准上，UniSync显著优于现有方法，展现出强泛化性和生产就绪性。

## 摘要（原文）

> Lip synchronization aims to generate realistic talking videos that match given audio, which is essential for high-quality video dubbing. However, current methods have fundamental drawbacks: mask-based approaches suffer from local color discrepancies, while mask-free methods struggle with global background texture misalignment. Furthermore, most methods struggle with diverse real-world scenarios such as stylized avatars, face occlusion, and extreme lighting conditions. In this paper, we propose UniSync, a unified framework designed for achieving high-fidelity lip synchronization in diverse scenarios. Specifically, UniSync uses a mask-free pose-anchored training strategy to keep head motion and eliminate synthesis color artifacts, while employing mask-based blending consistent inference to ensure structural precision and smooth blending. Notably, fine-tuning on compact but diverse videos empowers our model with exceptional domain adaptability, handling complex corner cases effectively. We also introduce the RealWorld-LipSync benchmark to evaluate models under real-world demands, which covers diverse application scenarios including both human faces and stylized avatars. Extensive experiments demonstrate that UniSync significantly outperforms state-of-the-art methods, advancing the field towards truly generalizable and production-ready lip synchronization.

