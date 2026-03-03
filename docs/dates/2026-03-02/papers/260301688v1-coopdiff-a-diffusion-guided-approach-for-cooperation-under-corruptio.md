---
layout: default
title: CoopDiff: A Diffusion-Guided Approach for Cooperation under Corruptions
---

# CoopDiff: A Diffusion-Guided Approach for Cooperation under Corruptions
**arXiv**：[2603.01688v1](https://arxiv.org/abs/2603.01688) · [PDF](https://arxiv.org/pdf/2603.01688.pdf)  
**作者**：Gong Chen, Chaokun Zhang, Pengcheng Lv  

**一句话要点**：提出CoopDiff扩散引导框架以解决合作感知在现实世界退化下的鲁棒性问题

**关键词**：合作感知, 扩散模型, 去噪机制, 师生范式, 多退化基准, 自适应融合

## 3 点简述
- 核心问题：现实世界中的多样不可预测退化削弱合作感知的鲁棒性和泛化能力
- 方法要点：采用师生范式，教师通过扩散去噪生成清洁监督特征，学生通过双分支编码和自适应解码重建目标
- 实验或效果：在OPV2Vn和DAIR-V2Xn基准上优于先前方法，降低相对退化误差，提供精度与效率的可调平衡

## 摘要（原文）

> Cooperative perception lets agents share information to expand coverage and improve scene understanding. However, in real-world scenarios, diverse and unpredictable corruptions undermine its robustness and generalization. To address these challenges, we introduce CoopDiff, a diffusion-based cooperative perception framework that mitigates corruptions via a denoising mechanism. CoopDiff adopts a teacher-student paradigm: the Quality-Aware Teacher performs voxel-level early fusion with Quality of Interest weighting and semantic guidance, then produces clean supervision features via a diffusion denoiser. The Dual-Branch Diffusion Student first separates ego and cooperative streams in encoding to reconstruct the teacher's clean targets. And then, an Ego-Guided Cross-Attention mechanism facilitates balanced decoding under degradation by adaptively integrating ego and cooperative features. We evaluate CoopDiff on two constructed multi-degradation benchmarks, OPV2Vn and DAIR-V2Xn, each incorporating six corruption types, including environmental and sensor-level distortions. Benefiting from the inherent denoising properties of diffusion, CoopDiff consistently outperforms prior methods across all degradation types and lowers the relative corruption error. Furthermore, it offers a tunable balance between precision and inference efficiency.

