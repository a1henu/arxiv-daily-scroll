---
layout: default
title: SurgAtt-Tracker: Online Surgical Attention Tracking via Temporal Proposal Reranking and Motion-Aware Refinement
---

# SurgAtt-Tracker: Online Surgical Attention Tracking via Temporal Proposal Reranking and Motion-Aware Refinement
**arXiv**：[2602.20636v1](https://arxiv.org/abs/2602.20636) · [PDF](https://arxiv.org/pdf/2602.20636.pdf)  
**作者**：Rulin Zhou, Guankun Wang, An Wang, Yujie Ma, Lixin Ouyang, Bolin Cui, Junyan Li, Chaowei Zhu, Mingyang Li, Ming Chen, Xiaopin Zhong, Peng Lu, Jiankun Wang, Xianming Liu, Hongliang Ren  

**一句话要点**：提出SurgAtt-Tracker框架，通过时序提案重排和运动感知细化，实现微创手术中在线注意力跟踪以指导视野规划。

**关键词**：手术注意力跟踪, 时空学习, 视野指导, 时序提案重排, 运动感知细化, 微创手术

## 3 点简述
- 核心问题：现有方法常混淆视觉注意力估计与相机控制，或依赖直接对象中心假设，难以提供连续可解释的视野指导。
- 方法要点：将手术注意力跟踪建模为时空学习问题，利用提案级重排和运动感知细化来增强时序一致性，而非直接回归。
- 实验或效果：在多个数据集上验证，SurgAtt-Tracker在遮挡、多器械干扰和跨域设置下表现优异，支持下游机器人视野规划。

## 摘要（原文）

> Accurate and stable field-of-view (FoV) guidance is critical for safe and efficient minimally invasive surgery, yet existing approaches often conflate visual attention estimation with downstream camera control or rely on direct object-centric assumptions. In this work, we formulate surgical attention tracking as a spatio-temporal learning problem and model surgeon focus as a dense attention heatmap, enabling continuous and interpretable frame-wise FoV guidance. We propose SurgAtt-Tracker, a holistic framework that robustly tracks surgical attention by exploiting temporal coherence through proposal-level reranking and motion-aware refinement, rather than direct regression. To support systematic training and evaluation, we introduce SurgAtt-1.16M, a large-scale benchmark with a clinically grounded annotation protocol that enables comprehensive heatmap-based attention analysis across procedures and institutions. Extensive experiments on multiple surgical datasets demonstrate that SurgAtt-Tracker consistently achieves state-of-the-art performance and strong robustness under occlusion, multi-instrument interference, and cross-domain settings. Beyond attention tracking, our approach provides a frame-wise FoV guidance signal that can directly support downstream robotic FoV planning and automatic camera control.

