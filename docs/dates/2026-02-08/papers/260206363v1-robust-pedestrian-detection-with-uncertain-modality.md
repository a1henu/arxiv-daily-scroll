---
layout: default
title: Robust Pedestrian Detection with Uncertain Modality
---

# Robust Pedestrian Detection with Uncertain Modality
**arXiv**：[2602.06363v1](https://arxiv.org/abs/2602.06363) · [PDF](https://arxiv.org/pdf/2602.06363.pdf)  
**作者**：Qian Bie, Xiao Wang, Bin Yang, Zhixi Yu, Jun Chen, Xin Xu  

**一句话要点**：提出自适应不确定性感知网络以解决不确定模态输入下的行人检测问题

**关键词**：行人检测, 跨模态融合, 不确定性感知, 自适应网络, TRNT数据集

## 3 点简述
- 核心问题：现实场景中模态输入组合不确定，现有跨模态方法性能下降
- 方法要点：引入统一模态验证精炼和模态感知交互模块，自适应融合可用模态信息
- 实验或效果：构建TRNT数据集，AUNet在不确定输入下提升检测鲁棒性

## 摘要（原文）

> Existing cross-modal pedestrian detection (CMPD) employs complementary information from RGB and thermal-infrared (TIR) modalities to detect pedestrians in 24h-surveillance systems.RGB captures rich pedestrian details under daylight, while TIR excels at night. However, TIR focuses primarily on the person's silhouette, neglecting critical texture details essential for detection. While the near-infrared (NIR) captures texture under low-light conditions, which effectively alleviates performance issues of RGB and detail loss in TIR, thereby reducing missed detections. To this end, we construct a new Triplet RGB-NIR-TIR (TRNT) dataset, comprising 8,281 pixel-aligned image triplets, establishing a comprehensive foundation for algorithmic research. However, due to the variable nature of real-world scenarios, imaging devices may not always capture all three modalities simultaneously. This results in input data with unpredictable combinations of modal types, which challenge existing CMPD methods that fail to extract robust pedestrian information under arbitrary input combinations, leading to significant performance degradation. To address these challenges, we propose the Adaptive Uncertainty-aware Network (AUNet) for accurately discriminating modal availability and fully utilizing the available information under uncertain inputs. Specifically, we introduce Unified Modality Validation Refinement (UMVR), which includes an uncertainty-aware router to validate modal availability and a semantic refinement to ensure the reliability of information within the modality. Furthermore, we design a Modality-Aware Interaction (MAI) module to adaptively activate or deactivate its internal interaction mechanisms per UMVR output, enabling effective complementary information fusion from available modalities.

