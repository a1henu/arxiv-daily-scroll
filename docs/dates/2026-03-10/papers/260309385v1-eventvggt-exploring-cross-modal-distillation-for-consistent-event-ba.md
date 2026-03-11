---
layout: default
title: EventVGGT: Exploring Cross-Modal Distillation for Consistent Event-based Depth Estimation
---

# EventVGGT: Exploring Cross-Modal Distillation for Consistent Event-based Depth Estimation
**arXiv**：[2603.09385v1](https://arxiv.org/abs/2603.09385) · [PDF](https://arxiv.org/pdf/2603.09385.pdf)  
**作者**：Yinrui Ren, Jinjing Zhu, Kanghao Chen, Zhuoxiao Li, Jing Ou, Zidong Cao, Tongyan Hua, Peilun Shi, Yingchun Fu, Wufan Zhao, Hui Xiong  

**一句话要点**：提出EventVGGT框架，通过跨模态蒸馏解决事件流深度估计中的时间不一致性问题。

**关键词**：事件相机深度估计, 跨模态蒸馏, 时空一致性, 视觉基础模型, 零样本泛化

## 3 点简述
- 核心问题：事件流深度估计因缺乏密集标注和忽略时间连续性，导致预测不一致和不准确。
- 方法要点：将事件流建模为视频序列，从VGGT蒸馏时空和多视图几何先验，采用三级蒸馏策略。
- 实验或效果：在EventScape数据集上深度误差降低超53%，并在未见数据集上展示零样本泛化能力。

## 摘要（原文）

> Event cameras offer superior sensitivity to high-speed motion and extreme lighting, making event-based monocular depth estimation a promising approach for robust 3D perception in challenging conditions. However, progress is severely hindered by the scarcity of dense depth annotations. While recent annotation-free approaches mitigate this by distilling knowledge from Vision Foundation Models (VFMs), a critical limitation persists: they process event streams as independent frames. By neglecting the inherent temporal continuity of event data, these methods fail to leverage the rich temporal priors encoded in VFMs, ultimately yielding temporally inconsistent and less accurate depth predictions. To address this, we introduce EventVGGT, a novel framework that explicitly models the event stream as a coherent video sequence. To the best of our knowledge, we are the first to distill spatio-temporal and multi-view geometric priors from the Visual Geometry Grounded Transformer (VGGT) into the event domain. We achieve this via a comprehensive tri-level distillation strategy: (i) Cross-Modal Feature Mixture (CMFM) bridges the modality gap at the output level by fusing RGB and event features to generate auxiliary depth predictions; (ii) Spatio-Temporal Feature Distillation (STFD) distills VGGT's powerful spatio-temporal representations at the feature level; and (iii) Temporal Consistency Distillation (TCD) enforces cross-frame coherence at the temporal level by aligning inter-frame depth changes. Extensive experiments demonstrate that EventVGGT consistently outperforms existing methods -- reducing the absolute mean depth error at 30m by over 53\% on EventScape (from 2.30 to 1.06) -- while exhibiting robust zero-shot generalization on the unseen DENSE and MVSEC datasets.

