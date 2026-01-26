---
layout: default
title: GPA-VGGT:Adapting VGGT to Large scale Localization by self-Supervised learning with Geometry and Physics Aware loss
---

# GPA-VGGT:Adapting VGGT to Large scale Localization by self-Supervised learning with Geometry and Physics Aware loss
**arXiv**：[2601.16885v1](https://arxiv.org/abs/2601.16885) · [PDF](https://arxiv.org/pdf/2601.16885.pdf)  
**作者**：Yangfan Xu, Lilian Zhang, Xiaofeng He, Pengdong Wu, Wenqi Wu, Jun Mao  

**一句话要点**：提出自监督框架GPA-VGGT，通过几何物理感知损失增强大规模场景定位能力

**关键词**：自监督学习, 相机姿态估计, 几何约束, 大规模定位, 视觉Transformer

## 3 点简述
- 问题：VGGT模型依赖标注数据，难以适应无标签大规模场景定位
- 方法：扩展序列几何约束，结合光度一致性与几何约束进行自监督训练
- 效果：模型快速收敛，在大规模定位任务中性能显著提升

## 摘要（原文）

> Transformer-based general visual geometry frameworks have shown promising performance in camera pose estimation and 3D scene understanding. Recent advancements in Visual Geometry Grounded Transformer (VGGT) models have shown great promise in camera pose estimation and 3D reconstruction. However, these models typically rely on ground truth labels for training, posing challenges when adapting to unlabeled and unseen scenes. In this paper, we propose a self-supervised framework to train VGGT with unlabeled data, thereby enhancing its localization capability in large-scale environments. To achieve this, we extend conventional pair-wise relations to sequence-wise geometric constraints for self-supervised learning. Specifically, in each sequence, we sample multiple source frames and geometrically project them onto different target frames, which improves temporal feature consistency. We formulate physical photometric consistency and geometric constraints as a joint optimization loss to circumvent the requirement for hard labels. By training the model with this proposed method, not only the local and global cross-view attention layers but also the camera and depth heads can effectively capture the underlying multi-view geometry. Experiments demonstrate that the model converges within hundreds of iterations and achieves significant improvements in large-scale localization. Our code will be released at https://github.com/X-yangfan/GPA-VGGT.

