---
layout: default
title: Another BRIXEL in the Wall: Towards Cheaper Dense Features
---

# Another BRIXEL in the Wall: Towards Cheaper Dense Features
**arXiv**：[2511.05168v1](https://arxiv.org/abs/2511.05168) · [PDF](https://arxiv.org/pdf/2511.05168.pdf)  
**作者**：Alexander Lappe, Martin A. Giese  

**一句话要点**：提出BRIXEL知识蒸馏方法以降低高分辨率密集特征计算成本

**关键词**：知识蒸馏, 密集特征提取, 计算效率优化, DINOv3模型, 高分辨率图像处理

## 3 点简述
- 核心问题：DINOv3模型在高分辨率下计算密集特征图成本高昂
- 方法要点：通过学生模型学习自身特征图在高分辨率下的蒸馏
- 实验或效果：在固定分辨率下超越基线，计算成本大幅降低

## 摘要（原文）

> Vision foundation models achieve strong performance on both global and
> locally dense downstream tasks. Pretrained on large images, the recent DINOv3
> model family is able to produce very fine-grained dense feature maps, enabling
> state-of-the-art performance. However, computing these feature maps requires
> the input image to be available at very high resolution, as well as large
> amounts of compute due to the squared complexity of the transformer
> architecture. To address these issues, we propose BRIXEL, a simple knowledge
> distillation approach that has the student learn to reproduce its own feature
> maps at higher resolution. Despite its simplicity, BRIXEL outperforms the
> baseline DINOv3 models by large margins on downstream tasks when the resolution
> is kept fixed. Moreover, it is able to produce feature maps that are very
> similar to those of the teacher at a fraction of the computational cost. Code
> and model weights are available at https://github.com/alexanderlappe/BRIXEL.

