---
layout: default
title: Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers
---

# Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers
**arXiv**：[2603.02919v1](https://arxiv.org/abs/2603.02919) · [PDF](https://arxiv.org/pdf/2603.02919.pdf)  
**作者**：Youngjun Jun, Seil Kang, Woojung Han, Seong Jae Hwang  

**一句话要点**：提出可解释运动注意力图以在视频扩散变换器中时空定位运动概念

**关键词**：视频扩散变换器, 可解释性, 运动定位, 显著图, 零样本学习, 时空分析

## 3 点简述
- 研究视频扩散变换器如何将运动词转换为视频，聚焦时空定位问题
- 引入GramCol生成每帧显著图，并提出运动特征选择算法获得IMAP
- 实验显示方法在运动定位和零样本视频语义分割中表现优异

## 摘要（原文）

> Video Diffusion Transformers (DiTs) have been synthesizing high-quality video with high fidelity from given text descriptions involving motion. However, understanding how Video DiTs convert motion words into video remains insufficient. Furthermore, while prior studies on interpretable saliency maps primarily target objects, motion-related behavior in Video DiTs remains largely unexplored. In this paper, we investigate concrete motion features that specify when and which object moves for a given motion concept. First, to spatially localize, we introduce GramCol, which adaptively produces per-frame saliency maps for any text concept, including both motion and non-motion. Second, we propose a motion-feature selection algorithm to obtain an Interpretable Motion-Attentive Map (IMAP) that localizes motion spatially and temporally. Our method discovers concept saliency maps without the need for any gradient calculation or parameter update. Experimentally, our method shows outstanding localization capability on the motion localization task and zero-shot video semantic segmentation, providing interpretable and clearer saliency maps for both motion and non-motion concepts.

