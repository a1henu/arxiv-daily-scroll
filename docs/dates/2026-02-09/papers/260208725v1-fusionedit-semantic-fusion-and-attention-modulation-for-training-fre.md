---
layout: default
title: FusionEdit: Semantic Fusion and Attention Modulation for Training-Free Image Editing
---

# FusionEdit: Semantic Fusion and Attention Modulation for Training-Free Image Editing
**arXiv**：[2602.08725v1](https://arxiv.org/abs/2602.08725) · [PDF](https://arxiv.org/pdf/2602.08725.pdf)  
**作者**：Yongwen Lai, Chaoqun Wang, Shaobo Min  

**一句话要点**：提出FusionEdit框架，通过语义融合与注意力调制实现免训练图像编辑

**关键词**：文本引导图像编辑, 免训练框架, 语义融合, 注意力调制, 边界优化

## 3 点简述
- 核心问题：现有方法使用硬掩码边界导致伪影和编辑性降低
- 方法要点：自动识别编辑区域，采用距离感知潜在融合和总变差损失优化边界
- 实验或效果：在实验中显著优于先进方法，代码已开源

## 摘要（原文）

> Text-guided image editing aims to modify specific regions according to the target prompt while preserving the identity of the source image. Recent methods exploit explicit binary masks to constrain editing, but hard mask boundaries introduce artifacts and reduce editability. To address these issues, we propose FusionEdit, a training-free image editing framework that achieves precise and controllable edits. First, editing and preserved regions are automatically identified by measuring semantic discrepancies between source and target prompts. To mitigate boundary artifacts, FusionEdit performs distance-aware latent fusion along region boundaries to yield the soft and accurate mask, and employs a total variation loss to enforce smooth transitions, obtaining natural editing results. Second, FusionEdit leverages AdaIN-based modulation within DiT attention layers to perform a statistical attention fusion in the editing region, enhancing editability while preserving global consistency with the source image. Extensive experiments demonstrate that our FusionEdit significantly outperforms state-of-the-art methods. Code is available at \href{https://github.com/Yvan1001/FusionEdit}{https://github.com/Yvan1001/FusionEdit}.

