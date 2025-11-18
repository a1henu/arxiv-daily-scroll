---
layout: default
title: RefineVAD: Semantic-Guided Feature Recalibration for Weakly Supervised Video Anomaly Detection
---

# RefineVAD: Semantic-Guided Feature Recalibration for Weakly Supervised Video Anomaly Detection
**arXiv**：[2511.13204v1](https://arxiv.org/abs/2511.13204) · [PDF](https://arxiv.org/pdf/2511.13204.pdf)  
**作者**：Junhee Lee, ChaeBeen Bang, MyoungChul Kim, MyeongAh Cho  

**一句话要点**：提出RefineVAD框架，通过语义引导特征重校准解决弱监督视频异常检测中异常多样性建模不足问题。

**关键词**：弱监督视频异常检测, 语义引导特征重校准, 时序注意力机制, 类别原型对齐, Transformer建模

## 3 点简述
- 核心问题：现有方法将异常视为单一类别，忽略其语义和时序多样性。
- 方法要点：集成MoTAR模块动态调整时序焦点，CORE模块注入类别先验对齐特征。
- 实验或效果：在WVAD基准上验证有效性，强调语义上下文对异常模式引导的重要性。

## 摘要（原文）

> Weakly-Supervised Video Anomaly Detection aims to identify anomalous events using only video-level labels, balancing annotation efficiency with practical applicability. However, existing methods often oversimplify the anomaly space by treating all abnormal events as a single category, overlooking the diverse semantic and temporal characteristics intrinsic to real-world anomalies. Inspired by how humans perceive anomalies, by jointly interpreting temporal motion patterns and semantic structures underlying different anomaly types, we propose RefineVAD, a novel framework that mimics this dual-process reasoning. Our framework integrates two core modules. The first, Motion-aware Temporal Attention and Recalibration (MoTAR), estimates motion salience and dynamically adjusts temporal focus via shift-based attention and global Transformer-based modeling. The second, Category-Oriented Refinement (CORE), injects soft anomaly category priors into the representation space by aligning segment-level features with learnable category prototypes through cross-attention. By jointly leveraging temporal dynamics and semantic structure, explicitly models both "how" motion evolves and "what" semantic category it resembles. Extensive experiments on WVAD benchmark validate the effectiveness of RefineVAD and highlight the importance of integrating semantic context to guide feature refinement toward anomaly-relevant patterns.

