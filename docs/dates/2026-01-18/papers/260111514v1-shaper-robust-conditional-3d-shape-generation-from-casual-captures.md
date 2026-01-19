---
layout: default
title: ShapeR: Robust Conditional 3D Shape Generation from Casual Captures
---

# ShapeR: Robust Conditional 3D Shape Generation from Casual Captures
**arXiv**：[2601.11514v1](https://arxiv.org/abs/2601.11514) · [PDF](https://arxiv.org/pdf/2601.11514.pdf)  
**作者**：Yawar Siddiqui, Duncan Frost, Samir Aroudj, Armen Avetisyan, Henry Howard-Jenkins, Daniel DeTone, Pierre Moulon, Qirui Wu, Zhengqin Li, Julian Straub, Richard Newcombe, Jakob Engel  

**一句话要点**：提出ShapeR以从随意捕获的图像序列中稳健生成条件3D形状

**关键词**：条件3D形状生成, 视觉-惯性SLAM, 整流流变换器, 野外数据增强, 多模态条件, 度量形状重建

## 3 点简述
- 核心问题：现有3D形状生成方法依赖干净输入，难以处理现实场景中的遮挡和杂乱背景
- 方法要点：结合SLAM点、多视角图像和机器生成描述，通过整流流变换器生成高保真度量3D形状
- 实验或效果：在野外对象基准上显著优于现有方法，Chamfer距离提升2.7倍

## 摘要（原文）

> Recent advances in 3D shape generation have achieved impressive results, but most existing methods rely on clean, unoccluded, and well-segmented inputs. Such conditions are rarely met in real-world scenarios. We present ShapeR, a novel approach for conditional 3D object shape generation from casually captured sequences. Given an image sequence, we leverage off-the-shelf visual-inertial SLAM, 3D detection algorithms, and vision-language models to extract, for each object, a set of sparse SLAM points, posed multi-view images, and machine-generated captions. A rectified flow transformer trained to effectively condition on these modalities then generates high-fidelity metric 3D shapes. To ensure robustness to the challenges of casually captured data, we employ a range of techniques including on-the-fly compositional augmentations, a curriculum training scheme spanning object- and scene-level datasets, and strategies to handle background clutter. Additionally, we introduce a new evaluation benchmark comprising 178 in-the-wild objects across 7 real-world scenes with geometry annotations. Experiments show that ShapeR significantly outperforms existing approaches in this challenging setting, achieving an improvement of 2.7x in Chamfer distance compared to state of the art.

