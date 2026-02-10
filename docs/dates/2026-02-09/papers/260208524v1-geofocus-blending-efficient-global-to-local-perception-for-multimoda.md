---
layout: default
title: GeoFocus: Blending Efficient Global-to-Local Perception for Multimodal Geometry Problem-Solving
---

# GeoFocus: Blending Efficient Global-to-Local Perception for Multimodal Geometry Problem-Solving
**arXiv**：[2602.08524v1](https://arxiv.org/abs/2602.08524) · [PDF](https://arxiv.org/pdf/2602.08524.pdf)  
**作者**：Linger Deng, Yuliang Liu, Wenwen Yu, Zujia Zhang, Jianzhong Ju, Zhenbo Luo, Xiang Bai  

**一句话要点**：提出GeoFocus框架，通过局部感知与拓扑编码提升多模态几何问题求解能力

**关键词**：几何问题求解, 多模态模型, 局部感知, 拓扑编码, 视觉推理

## 3 点简述
- 几何问题求解需兼顾全局形状识别与局部关系，对大型多模态模型构成挑战
- 框架包含Critical Local Perceptor增强局部特征，VertexLang语言优化全局拓扑编码
- 在多个数据集上实现精度提升，并减少训练时间，展现鲁棒性

## 摘要（原文）

> Geometry problem-solving remains a significant challenge for Large Multimodal Models (LMMs), requiring not only global shape recognition but also attention to intricate local relationships related to geometric theory. To address this, we propose GeoFocus, a novel framework comprising two core modules. 1) Critical Local Perceptor, which automatically identifies and emphasizes critical local structure (e.g., angles, parallel lines, comparative distances) through thirteen theory-based perception templates, boosting critical local feature coverage by 61% compared to previous methods. 2) VertexLang, a compact topology formal language, encodes global figures through vertex coordinates and connectivity relations. By replacing bulky code-based encodings, VertexLang reduces global perception training time by 20% while improving topology recognition accuracy. When evaluated in Geo3K, GeoQA, and FormalGeo7K, GeoFocus achieves a 4.7% accuracy improvement over leading specialized models and demonstrates superior robustness in MATHVERSE under diverse visual conditions. Project Page -- https://github.com/dle666/GeoFocus

