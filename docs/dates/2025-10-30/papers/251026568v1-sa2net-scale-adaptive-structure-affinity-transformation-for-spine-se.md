---
layout: default
title: SA$^{2}$Net: Scale-Adaptive Structure-Affinity Transformation for Spine Segmentation from Ultrasound Volume Projection Imaging
---

# SA$^{2}$Net: Scale-Adaptive Structure-Affinity Transformation for Spine Segmentation from Ultrasound Volume Projection Imaging
**arXiv**：[2510.26568v1](https://arxiv.org/abs/2510.26568) · [PDF](https://arxiv.org/pdf/2510.26568.pdf)  
**作者**：Hao Xie, Zixun Huang, Yushen Zuo, Yakun Ju, Frank H. F. Leung, N. F. Law, Kin-Man Lam, Yong-Ping Zheng, Sai Ho Ling  

**一句话要点**：提出SA²Net以解决超声脊柱分割中的上下文和结构建模问题

**关键词**：脊柱分割, 超声体积投影成像, 尺度自适应, 结构亲和变换, Transformer解码器, 特征混合损失

## 3 点简述
- 脊柱分割面临全局上下文学习不足和结构知识编码困难的核心问题
- 方法包括尺度自适应策略学习长距离相关性和结构亲和变换结合Transformer解码器
- 实验显示SA²Net在分割性能上优于现有方法，并具有对多种骨干网络的适应性

## 摘要（原文）

> Spine segmentation, based on ultrasound volume projection imaging (VPI),
> plays a vital role for intelligent scoliosis diagnosis in clinical
> applications. However, this task faces several significant challenges. Firstly,
> the global contextual knowledge of spines may not be well-learned if we neglect
> the high spatial correlation of different bone features. Secondly, the spine
> bones contain rich structural knowledge regarding their shapes and positions,
> which deserves to be encoded into the segmentation process. To address these
> challenges, we propose a novel scale-adaptive structure-aware network
> (SA$^{2}$Net) for effective spine segmentation. First, we propose a
> scale-adaptive complementary strategy to learn the cross-dimensional
> long-distance correlation features for spinal images. Second, motivated by the
> consistency between multi-head self-attention in Transformers and semantic
> level affinity, we propose structure-affinity transformation to transform
> semantic features with class-specific affinity and combine it with a
> Transformer decoder for structure-aware reasoning. In addition, we adopt a
> feature mixing loss aggregation method to enhance model training. This method
> improves the robustness and accuracy of the segmentation process. The
> experimental results demonstrate that our SA$^{2}$Net achieves superior
> segmentation performance compared to other state-of-the-art methods. Moreover,
> the adaptability of SA$^{2}$Net to various backbones enhances its potential as
> a promising tool for advanced scoliosis diagnosis using intelligent spinal
> image analysis. The code and experimental demo are available at
> https://github.com/taetiseo09/SA2Net.

