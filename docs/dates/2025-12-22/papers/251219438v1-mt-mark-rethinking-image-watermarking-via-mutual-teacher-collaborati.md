---
layout: default
title: MT-Mark: Rethinking Image Watermarking via Mutual-Teacher Collaboration with Adaptive Feature Modulation
---

# MT-Mark: Rethinking Image Watermarking via Mutual-Teacher Collaboration with Adaptive Feature Modulation
**arXiv**：[2512.19438v1](https://arxiv.org/abs/2512.19438) · [PDF](https://arxiv.org/pdf/2512.19438.pdf)  
**作者**：Fei Ge, Ying Huang, Jie Liu, Guixuan Zhang, Zhi Zeng, Shuwu Zhang, Hu Guan  

**一句话要点**：提出MT-Mark方法，通过互教师协作与自适应特征调制解决深度图像水印嵌入与提取弱耦合问题。

**关键词**：图像水印, 协作学习, 自适应特征调制, 鲁棒性学习, 深度神经网络

## 3 点简述
- 核心问题：现有深度图像水印方法中嵌入器与提取器缺乏显式协作，导致训练孤立和鲁棒性学习受限。
- 方法要点：引入协作交互机制和自适应特征调制模块，实现嵌入与提取的双向通信和内容感知特征调节。
- 实验或效果：在真实世界和AI生成数据集上，该方法在保持高感知质量的同时，提取准确率优于现有方法，展现强鲁棒性和泛化能力。

## 摘要（原文）

> Existing deep image watermarking methods follow a fixed embedding-distortion-extraction pipeline, where the embedder and extractor are weakly coupled through a final loss and optimized in isolation. This design lacks explicit collaboration, leaving no structured mechanism for the embedder to incorporate decoding-aware cues or for the extractor to guide embedding during training. To address this architectural limitation, we rethink deep image watermarking by reformulating embedding and extraction as explicitly collaborative components. To realize this reformulation, we introduce a Collaborative Interaction Mechanism (CIM) that establishes direct, bidirectional communication between the embedder and extractor, enabling a mutual-teacher training paradigm and coordinated optimization. Built upon this explicitly collaborative architecture, we further propose an Adaptive Feature Modulation Module (AFMM) to support effective interaction. AFMM enables content-aware feature regulation by decoupling modulation structure and strength, guiding watermark embedding toward stable image features while suppressing host interference during extraction. Under CIM, the AFMMs on both sides form a closed-loop collaboration that aligns embedding behavior with extraction objectives. This architecture-level redesign changes how robustness is learned in watermarking systems. Rather than relying on exhaustive distortion simulation, robustness emerges from coordinated representation learning between embedding and extraction. Experiments on real-world and AI-generated datasets demonstrate that the proposed method consistently outperforms state-of-the-art approaches in watermark extraction accuracy while maintaining high perceptual quality, showing strong robustness and generalization.

