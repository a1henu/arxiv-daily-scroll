---
layout: default
title: FullPart: Generating each 3D Part at Full Resolution
---

# FullPart: Generating each 3D Part at Full Resolution
**arXiv**：[2510.26140v1](https://arxiv.org/abs/2510.26140) · [PDF](https://arxiv.org/pdf/2510.26140.pdf)  
**作者**：Lihe Ding, Shaocong Dong, Yaokun Li, Chenjian Gao, Xiao Chen, Rui Han, Yihao Kuang, Hong Zhang, Bo Huang, Zhanpeng Huang, Zibin Wang, Dan Xu, Tianfan Xue  

**一句话要点**：提出FullPart框架，结合隐式与显式方法，实现高分辨率3D部件生成。

**关键词**：3D部件生成, 隐式扩散, 显式体素, 边界框布局, 全分辨率生成, PartVerse-XL数据集

## 3 点简述
- 核心问题：现有方法在3D部件生成中细节不足或小部件质量退化。
- 方法要点：先隐式扩散生成边界框布局，再在各自全分辨率体素网格中生成部件。
- 实验或效果：在PartVerse-XL数据集上实现SOTA，并释放代码数据。

## 摘要（原文）

> Part-based 3D generation holds great potential for various applications.
> Previous part generators that represent parts using implicit vector-set tokens
> often suffer from insufficient geometric details. Another line of work adopts
> an explicit voxel representation but shares a global voxel grid among all
> parts; this often causes small parts to occupy too few voxels, leading to
> degraded quality. In this paper, we propose FullPart, a novel framework that
> combines both implicit and explicit paradigms. It first derives the bounding
> box layout through an implicit box vector-set diffusion process, a task that
> implicit diffusion handles effectively since box tokens contain little
> geometric detail. Then, it generates detailed parts, each within its own fixed
> full-resolution voxel grid. Instead of sharing a global low-resolution space,
> each part in our method - even small ones - is generated at full resolution,
> enabling the synthesis of intricate details. We further introduce a
> center-point encoding strategy to address the misalignment issue when
> exchanging information between parts of different actual sizes, thereby
> maintaining global coherence. Moreover, to tackle the scarcity of reliable part
> data, we present PartVerse-XL, the largest human-annotated 3D part dataset to
> date with 40K objects and 320K parts. Extensive experiments demonstrate that
> FullPart achieves state-of-the-art results in 3D part generation. We will
> release all code, data, and model to benefit future research in 3D part
> generation.

