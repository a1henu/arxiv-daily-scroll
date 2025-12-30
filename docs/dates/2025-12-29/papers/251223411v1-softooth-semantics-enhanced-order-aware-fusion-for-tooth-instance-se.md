---
layout: default
title: SOFTooth: Semantics-Enhanced Order-Aware Fusion for Tooth Instance Segmentation
---

# SOFTooth: Semantics-Enhanced Order-Aware Fusion for Tooth Instance Segmentation
**arXiv**：[2512.23411v1](https://arxiv.org/abs/2512.23411) · [PDF](https://arxiv.org/pdf/2512.23411.pdf)  
**作者**：Xiaolan Li, Wanquan Liu, Pengcheng Li, Pengyu Jie, Chenqiang Gao  

**一句话要点**：提出SOFTooth框架，通过语义增强的顺序感知2D-3D融合解决三维牙齿实例分割中的边界模糊和身份不一致问题。

**关键词**：三维牙齿实例分割, 2D-3D融合, 语义增强, 顺序感知匹配, 边界细化, 中心漂移抑制

## 3 点简述
- 核心问题：三维牙齿实例分割面临拥挤牙弓、边界模糊、牙齿缺失和第三磨牙等挑战，导致边界泄漏、中心漂移和身份不一致。
- 方法要点：利用冻结的2D语义嵌入增强3D点特征，结合中心引导掩码细化和顺序感知匈牙利匹配，提升边界精度和标签连贯性。
- 实验或效果：在3DTeethSeg'22数据集上实现最优整体准确率和平均IoU，尤其在第三磨牙案例中表现突出，无需2D微调。

## 摘要（原文）

> Three-dimensional (3D) tooth instance segmentation remains challenging due to crowded arches, ambiguous tooth-gingiva boundaries, missing teeth, and rare yet clinically important third molars. Native 3D methods relying on geometric cues often suffer from boundary leakage, center drift, and inconsistent tooth identities, especially for minority classes and complex anatomies. Meanwhile, 2D foundation models such as the Segment Anything Model (SAM) provide strong boundary-aware semantics, but directly applying them in 3D is impractical in clinical workflows. To address these issues, we propose SOFTooth, a semantics-enhanced, order-aware 2D-3D fusion framework that leverages frozen 2D semantics without explicit 2D mask supervision. First, a point-wise residual gating module injects occlusal-view SAM embeddings into 3D point features to refine tooth-gingiva and inter-tooth boundaries. Second, a center-guided mask refinement regularizes consistency between instance masks and geometric centroids, reducing center drift. Furthermore, an order-aware Hungarian matching strategy integrates anatomical tooth order and center distance into similarity-based assignment, ensuring coherent labeling even under missing or crowded dentitions. On 3DTeethSeg'22, SOFTooth achieves state-of-the-art overall accuracy and mean IoU, with clear gains on cases involving third molars, demonstrating that rich 2D semantics can be effectively transferred to 3D tooth instance segmentation without 2D fine-tuning.

