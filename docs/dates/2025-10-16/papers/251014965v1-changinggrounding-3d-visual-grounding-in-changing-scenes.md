---
layout: default
title: ChangingGrounding: 3D Visual Grounding in Changing Scenes
---

# ChangingGrounding: 3D Visual Grounding in Changing Scenes
**arXiv**：[2510.14965v1](https://arxiv.org/abs/2510.14965) · [PDF](https://arxiv.org/pdf/2510.14965.pdf)  
**作者**：Miao Hu, Zhiwei Huang, Tai Wang, Jiangmiao Pang, Dahua Lin, Nanning Zheng, Runsen Xu  

**一句话要点**：提出ChangingGrounding基准与Mem-ChangingGrounder方法，以解决动态场景中3D视觉定位问题。

**关键词**：3D视觉定位, 动态场景, 跨模态检索, 多视图融合, 零样本学习, 基准数据集

## 3 点简述
- 核心问题：现有3D视觉定位方法依赖更新点云，难以应对场景变化，阻碍实际部署。
- 方法要点：结合跨模态检索与轻量多视图融合，实现零样本目标定位与高效探索。
- 实验或效果：在ChangingGrounding基准上，Mem-ChangingGrounder实现最高定位精度并降低探索成本。

## 摘要（原文）

> Real-world robots localize objects from natural-language instructions while
> scenes around them keep changing. Yet most of the existing 3D visual grounding
> (3DVG) method still assumes a reconstructed and up-to-date point cloud, an
> assumption that forces costly re-scans and hinders deployment. We argue that
> 3DVG should be formulated as an active, memory-driven problem, and we introduce
> ChangingGrounding, the first benchmark that explicitly measures how well an
> agent can exploit past observations, explore only where needed, and still
> deliver precise 3D boxes in changing scenes. To set a strong reference point,
> we also propose Mem-ChangingGrounder, a zero-shot method for this task that
> marries cross-modal retrieval with lightweight multi-view fusion: it identifies
> the object type implied by the query, retrieves relevant memories to guide
> actions, then explores the target efficiently in the scene, falls back when
> previous operations are invalid, performs multi-view scanning of the target,
> and projects the fused evidence from multi-view scans to get accurate object
> bounding boxes. We evaluate different baselines on ChangingGrounding, and our
> Mem-ChangingGrounder achieves the highest localization accuracy while greatly
> reducing exploration cost. We hope this benchmark and method catalyze a shift
> toward practical, memory-centric 3DVG research for real-world applications.
> Project page: https://hm123450.github.io/CGB/ .

