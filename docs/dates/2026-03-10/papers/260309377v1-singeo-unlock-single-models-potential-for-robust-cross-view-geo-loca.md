---
layout: default
title: SinGeo: Unlock Single Model's Potential for Robust Cross-View Geo-Localization
---

# SinGeo: Unlock Single Model's Potential for Robust Cross-View Geo-Localization
**arXiv**：[2603.09377v1](https://arxiv.org/abs/2603.09377) · [PDF](https://arxiv.org/pdf/2603.09377.pdf)  
**作者**：Yang Chen, Xieyuanli Chen, Junxiang Li, Jie Tang, Tao Wu  

**一句话要点**：提出SinGeo框架，通过双判别学习与课程学习实现单模型鲁棒跨视角地理定位

**关键词**：跨视角地理定位, 鲁棒性学习, 双判别学习, 课程学习, 单模型部署, 视图一致性评估

## 3 点简述
- 现有方法依赖固定视场训练，在未知视场和方向下性能下降，需部署多模型
- SinGeo采用双判别学习增强视图内区分性，并首次引入课程学习策略提升鲁棒性
- 在四个基准数据集上取得SOTA结果，并展示跨架构可迁移性和稳定性评估方法

## 摘要（原文）

> Robust cross-view geo-localization (CVGL) remains challenging despite the surge in recent progress. Existing methods still rely on field-of-view (FoV)-specific training paradigms, where models are optimized under a fixed FoV but collapse when tested on unseen FoVs and unknown orientations. This limitation necessitates deploying multiple models to cover diverse variations. Although studies have explored dynamic FoV training by simply randomizing FoVs, they failed to achieve robustness across diverse conditions -- implicitly assuming all FoVs are equally difficult. To address this gap, we present SinGeo, a simple yet powerful framework that enables a single model to realize robust cross-view geo-localization without additional modules or explicit transformations. SinGeo employs a dual discriminative learning architecture that enhances intra-view discriminability within both ground and satellite branches, and is the first to introduce a curriculum learning strategy to achieve robust CVGL. Extensive evaluations on four benchmark datasets reveal that SinGeo sets state-of-the-art (SOTA) results under diverse conditions, and notably outperforms methods specifically trained for extreme FoVs. Beyond superior performance, SinGeo also exhibits cross-architecture transferability. Furthermore, we propose a consistency evaluation method to quantitatively assess model stability under varying views, providing an explainable perspective for understanding and advancing robustness in future CVGL research. Codes will be available upon acceptance.

