---
layout: default
title: MUT3R: Motion-aware Updating Transformer for Dynamic 3D Reconstruction
---

# MUT3R: Motion-aware Updating Transformer for Dynamic 3D Reconstruction
**arXiv**：[2512.03939v1](https://arxiv.org/abs/2512.03939) · [PDF](https://arxiv.org/pdf/2512.03939.pdf)  
**作者**：Guole Shen, Tianchen Deng, Xingrui Qin, Nailin Wang, Jianyu Wang, Yanbo Wang, Yongtao Chen, Hesheng Wang, Jingchuan Wang  

**一句话要点**：提出MUT3R框架，利用注意力机制抑制动态内容以提升动态3D重建的稳定性。

**关键词**：动态3D重建, 注意力机制, Transformer, 无训练框架, 运动感知, 流式场景

## 3 点简述
- 核心问题：现有状态循环神经网络在动态3D重建中易受运动区域干扰，导致伪影。
- 方法要点：分析预训练Transformer的注意力图，提取隐含运动线索，设计无训练的门控模块抑制动态内容。
- 实验或效果：在多个动态基准测试中，提升时间一致性和相机姿态鲁棒性，无需重新训练。

## 摘要（原文）

> Recent stateful recurrent neural networks have achieved remarkable progress on static 3D reconstruction but remain vulnerable to motion-induced artifacts, where non-rigid regions corrupt attention propagation between the spatial memory and image feature. By analyzing the internal behaviors of the state and image token updating mechanism, we find that aggregating self-attention maps across layers reveals a consistent pattern: dynamic regions are naturally down-weighted, exposing an implicit motion cue that the pretrained transformer already encodes but never explicitly uses. Motivated by this observation, we introduce MUT3R, a training-free framework that applies the attention-derived motion cue to suppress dynamic content in the early layers of the transformer during inference. Our attention-level gating module suppresses the influence of dynamic regions before their artifacts propagate through the feature hierarchy. Notably, we do not retrain or fine-tune the model; we let the pretrained transformer diagnose its own motion cues and correct itself. This early regulation stabilizes geometric reasoning in streaming scenarios and leads to improvements in temporal consistency and camera pose robustness across multiple dynamic benchmarks, offering a simple and training-free pathway toward motion-aware streaming reconstruction.

