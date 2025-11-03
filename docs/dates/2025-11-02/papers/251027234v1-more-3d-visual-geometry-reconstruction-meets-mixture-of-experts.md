---
layout: default
title: MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts
---

# MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts
**arXiv**：[2510.27234v1](https://arxiv.org/abs/2510.27234) · [PDF](https://arxiv.org/pdf/2510.27234.pdf)  
**作者**：Jingnan Gao, Zhe Wang, Xianze Fang, Xingyu Ren, Zhuo Chen, Shengqi Liu, Yuhao Cheng, Jiangjing Lyu, Xiaokang Yang, Yichao Yan  

**一句话要点**：提出MoRE模型以解决3D视觉几何重建中的可扩展性和鲁棒性问题

**关键词**：3D视觉几何重建, 专家混合架构, 深度估计优化, 语义特征集成, 多任务学习, 可扩展模型

## 3 点简述
- 核心问题：3D模型扩展困难，源于几何监督复杂性和数据多样性。
- 方法要点：采用MoE架构动态路由特征，结合置信度深度优化和语义特征集成。
- 实验或效果：在多个基准测试中达到SOTA，支持下游应用无需额外计算。

## 摘要（原文）

> Recent advances in language and vision have demonstrated that scaling up
> model capacity consistently improves performance across diverse tasks. In 3D
> visual geometry reconstruction, large-scale training has likewise proven
> effective for learning versatile representations. However, further scaling of
> 3D models is challenging due to the complexity of geometric supervision and the
> diversity of 3D data. To overcome these limitations, we propose MoRE, a dense
> 3D visual foundation model based on a Mixture-of-Experts (MoE) architecture
> that dynamically routes features to task-specific experts, allowing them to
> specialize in complementary data aspects and enhance both scalability and
> adaptability. Aiming to improve robustness under real-world conditions, MoRE
> incorporates a confidence-based depth refinement module that stabilizes and
> refines geometric estimation. In addition, it integrates dense semantic
> features with globally aligned 3D backbone representations for high-fidelity
> surface normal prediction. MoRE is further optimized with tailored loss
> functions to ensure robust learning across diverse inputs and multiple
> geometric tasks. Extensive experiments demonstrate that MoRE achieves
> state-of-the-art performance across multiple benchmarks and supports effective
> downstream applications without extra computation.

