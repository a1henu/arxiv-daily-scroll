---
layout: default
title: Rethinking Intracranial Aneurysm Vessel Segmentation: A Perspective from Computational Fluid Dynamics Applications
---

# Rethinking Intracranial Aneurysm Vessel Segmentation: A Perspective from Computational Fluid Dynamics Applications
**arXiv**：[2512.01319v1](https://arxiv.org/abs/2512.01319) · [PDF](https://arxiv.org/pdf/2512.01319.pdf)  
**作者**：Feiyang Xiao, Yichi Zhang, Xigui Li, Yuanye Zhou, Chen Jiang, Xin Guo, Limei Han, Yuxin Li, Fengping Zhu, Yuan Cheng  

**一句话要点**：提出IAVS数据集与评估系统，以提升颅内动脉瘤血管分割在计算流体动力学应用中的实用性。

**关键词**：颅内动脉瘤分割, 计算流体动力学, 医学图像数据集, 血流动力学分析, 多中心研究

## 3 点简述
- 当前分割方法重图像指标，轻CFD应用效果，导致临床实用性不足。
- 构建首个多中心IAVS数据集，含641个3D MRA图像和血流动力学分析结果。
- 建立两阶段评估基准和标准化CFD适用性系统，提供开箱即用框架。

## 摘要（原文）

> The precise segmentation of intracranial aneurysms and their parent vessels (IA-Vessel) is a critical step for hemodynamic analyses, which mainly depends on computational fluid dynamics (CFD). However, current segmentation methods predominantly focus on image-based evaluation metrics, often neglecting their practical effectiveness in subsequent CFD applications. To address this deficiency, we present the Intracranial Aneurysm Vessel Segmentation (IAVS) dataset, the first comprehensive, multi-center collection comprising 641 3D MRA images with 587 annotations of aneurysms and IA-Vessels. In addition to image-mask pairs, IAVS dataset includes detailed hemodynamic analysis outcomes, addressing the limitations of existing datasets that neglect topological integrity and CFD applicability. To facilitate the development and evaluation of clinically relevant techniques, we construct two evaluation benchmarks including global localization of aneurysms (Stage I) and fine-grained segmentation of IA-Vessel (Stage II) and develop a simple and effective two-stage framework, which can be used as a out-of-the-box method and strong baseline. For comprehensive evaluation of applicability of segmentation results, we establish a standardized CFD applicability evaluation system that enables the automated and consistent conversion of segmentation masks into CFD models, offering an applicability-focused assessment of segmentation outcomes. The dataset, code, and model will be public available at https://github.com/AbsoluteResonance/IAVS.

