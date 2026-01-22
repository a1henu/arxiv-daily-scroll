---
layout: default
title: RayRoPE: Projective Ray Positional Encoding for Multi-view Attention
---

# RayRoPE: Projective Ray Positional Encoding for Multi-view Attention
**arXiv**：[2601.15275v1](https://arxiv.org/abs/2601.15275) · [PDF](https://arxiv.org/pdf/2601.15275.pdf)  
**作者**：Yu Wu, Minsik Jeon, Jen-Hao Rick Chang, Oncel Tuzel, Shubham Tulsiani  

**一句话要点**：提出RayRoPE以解决多视图注意力中位置编码的几何感知与SE(3)不变性问题

**关键词**：多视图注意力, 位置编码, SE(3)不变性, 几何感知, 新视角合成, 立体深度估计

## 3 点简述
- 核心问题：现有多视图注意力位置编码方案无法同时实现唯一编码、SE(3)不变性和几何适应性
- 方法要点：基于射线预测3D点进行几何感知编码，计算查询帧投影坐标以实现SE(3)不变性
- 实验或效果：在CO3D数据集上LPIPS指标相对提升15%，支持RGB-D输入并带来更大增益

## 摘要（原文）

> We study positional encodings for multi-view transformers that process tokens from a set of posed input images, and seek a mechanism that encodes patches uniquely, allows SE(3)-invariant attention with multi-frequency similarity, and can be adaptive to the geometry of the underlying scene. We find that prior (absolute or relative) encoding schemes for multi-view attention do not meet the above desiderata, and present RayRoPE to address this gap. RayRoPE represents patch positions based on associated rays but leverages a predicted point along the ray instead of the direction for a geometry-aware encoding. To achieve SE(3) invariance, RayRoPE computes query-frame projective coordinates for computing multi-frequency similarity. Lastly, as the 'predicted' 3D point along a ray may not be precise, RayRoPE presents a mechanism to analytically compute the expected position encoding under uncertainty. We validate RayRoPE on the tasks of novel-view synthesis and stereo depth estimation and show that it consistently improves over alternate position encoding schemes (e.g. 15% relative improvement on LPIPS in CO3D). We also show that RayRoPE can seamlessly incorporate RGB-D input, resulting in even larger gains over alternatives that cannot positionally encode this information.

