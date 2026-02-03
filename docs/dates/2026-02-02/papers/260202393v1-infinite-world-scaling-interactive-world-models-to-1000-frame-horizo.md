---
layout: default
title: Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory
---

# Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory
**arXiv**：[2602.02393v1](https://arxiv.org/abs/2602.02393) · [PDF](https://arxiv.org/pdf/2602.02393.pdf)  
**作者**：Ruiqi Wu, Xuanhua He, Meng Cheng, Tianyu Yang, Yong Zhang, Zhuoliang Kang, Xunliang Cai, Xiaoming Wei, Chunle Guo, Chongyi Li, Ming-Ming Cheng  

**一句话要点**：提出Infinite-World，通过无姿态分层记忆和不确定性动作标注，在真实世界视频中实现1000+帧的交互式世界建模。

**关键词**：交互式世界模型, 长视频记忆, 无姿态建模, 动作标注, 分层压缩, 真实世界视频

## 3 点简述
- 核心问题：现有世界模型依赖合成数据和精确姿态，难以处理真实视频中的噪声姿态和视角稀疏问题。
- 方法要点：引入分层无姿态记忆压缩器，联合优化生成骨干，无需几何先验；提出不确定性动作标注模块，将连续运动离散化以利用原始数据。
- 实验或效果：通过密集重访微调策略激活长程闭环能力，实验显示在视觉质量、动作可控性和空间一致性上表现优越。

## 摘要（原文）

> We propose Infinite-World, a robust interactive world model capable of maintaining coherent visual memory over 1000+ frames in complex real-world environments. While existing world models can be efficiently optimized on synthetic data with perfect ground-truth, they lack an effective training paradigm for real-world videos due to noisy pose estimations and the scarcity of viewpoint revisits. To bridge this gap, we first introduce a Hierarchical Pose-free Memory Compressor (HPMC) that recursively distills historical latents into a fixed-budget representation. By jointly optimizing the compressor with the generative backbone, HPMC enables the model to autonomously anchor generations in the distant past with bounded computational cost, eliminating the need for explicit geometric priors. Second, we propose an Uncertainty-aware Action Labeling module that discretizes continuous motion into a tri-state logic. This strategy maximizes the utilization of raw video data while shielding the deterministic action space from being corrupted by noisy trajectories, ensuring robust action-response learning. Furthermore, guided by insights from a pilot toy study, we employ a Revisit-Dense Finetuning Strategy using a compact, 30-minute dataset to efficiently activate the model's long-range loop-closure capabilities. Extensive experiments, including objective metrics and user studies, demonstrate that Infinite-World achieves superior performance in visual quality, action controllability, and spatial consistency.

