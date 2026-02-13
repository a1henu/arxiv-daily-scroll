---
layout: default
title: RI-Mamba: Rotation-Invariant Mamba for Robust Text-to-Shape Retrieval
---

# RI-Mamba: Rotation-Invariant Mamba for Robust Text-to-Shape Retrieval
**arXiv**：[2602.11673v1](https://arxiv.org/abs/2602.11673) · [PDF](https://arxiv.org/pdf/2602.11673.pdf)  
**作者**：Khanh Nguyen, Dasith de Silva Edirimuni, Ghulam Mubashar Hassan, Ajmal Mian  

**一句话要点**：提出RI-Mamba以解决点云在任意旋转下的文本到形状检索问题

**关键词**：点云检索, 旋转不变性, 状态空间模型, 跨模态对比学习, 文本到形状检索

## 3 点简述
- 现有方法依赖规范姿态且类别有限，难以处理随机旋转的多样对象
- RI-Mamba通过全局局部参考系和Hilbert排序实现旋转不变性，并引入方向嵌入增强表达
- 在OmniObject3D基准上超过200个类别达到最优性能，代码已开源

## 摘要（原文）

> 3D assets have rapidly expanded in quantity and diversity due to the growing popularity of virtual reality and gaming. As a result, text-to-shape retrieval has become essential in facilitating intuitive search within large repositories. However, existing methods require canonical poses and support few object categories, limiting their real-world applicability where objects can belong to diverse classes and appear in random orientations. To address this challenge, we propose RI-Mamba, the first rotation-invariant state-space model for point clouds. RI-Mamba defines global and local reference frames to disentangle pose from geometry and uses Hilbert sorting to construct token sequences with meaningful geometric structure while maintaining rotation invariance. We further introduce a novel strategy to compute orientational embeddings and reintegrate them via feature-wise linear modulation, effectively recovering spatial context and enhancing model expressiveness. Our strategy is inherently compatible with state-space models and operates in linear time. To scale up retrieval, we adopt cross-modal contrastive learning with automated triplet generation, allowing training on diverse datasets without manual annotation. Extensive experiments demonstrate RI-Mamba's superior representational capacity and robustness, achieving state-of-the-art performance on the OmniObject3D benchmark across more than 200 object categories under arbitrary orientations. Our code will be made available at https://github.com/ndkhanh360/RI-Mamba.git.

