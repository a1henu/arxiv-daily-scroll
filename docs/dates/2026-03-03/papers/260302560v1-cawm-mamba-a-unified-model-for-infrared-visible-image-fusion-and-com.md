---
layout: default
title: CAWM-Mamba: A unified model for infrared-visible image fusion and compound adverse weather restoration
---

# CAWM-Mamba: A unified model for infrared-visible image fusion and compound adverse weather restoration
**arXiv**：[2603.02560v1](https://arxiv.org/abs/2603.02560) · [PDF](https://arxiv.org/pdf/2603.02560.pdf)  
**作者**：Huichun Liu, Xiaosong Li, Zhuangfan Huang, Tao Ye, Yang Liu, Haishu Tan  

**一句话要点**：提出CAWM-Mamba统一模型，以解决红外-可见光图像融合与复合恶劣天气恢复问题。

**关键词**：红外-可见光图像融合, 复合恶劣天气恢复, 端到端框架, 小波域分解, 跨模态特征交互, 自动驾驶感知

## 3 点简述
- 核心问题：现有方法仅处理单一天气退化，无法应对如雾+雨等复合退化场景。
- 方法要点：采用Weather-Aware Preprocess Module、Cross-modal Feature Interaction Module和Wavelet Space State Block实现端到端融合与恢复。
- 实验或效果：在AWMM-100K基准和标准数据集上优于现有方法，提升下游任务性能。

## 摘要（原文）

> Multimodal Image Fusion (MMIF) integrates complementary information from various modalities to produce clearer and more informative fused images. MMIF under adverse weather is particularly crucial in autonomous driving and UAV monitoring applications. However, existing adverse weather fusion methods generally only tackle single types of degradation such as haze, rain, or snow, and fail when multiple degradations coexist (e.g., haze+rain, rain+snow). To address this challenge, we propose Compound Adverse Weather Mamba (CAWM-Mamba), the first end-to-end framework that jointly performs image fusion and compound weather restoration with unified shared weights. Our network contains three key components: (1) a Weather-Aware Preprocess Module (WAPM) to enhance degraded visible features and extracts global weather embeddings; (2) a Cross-modal Feature Interaction Module (CFIM) to facilitate the alignment of heterogeneous modalities and exchange of complementary features across modalities; and (3) a Wavelet Space State Block (WSSB) that leverages wavelet-domain decomposition to decouple multi-frequency degradations. WSSB includes Freq-SSM, a module that models anisotropic high-frequency degradation without redundancy, and a unified degradation representation mechanism to further improve generalization across complex compound weather conditions. Extensive experiments on the AWMM-100K benchmark and three standard fusion datasets demonstrate that CAWM-Mamba consistently outperforms state-of-the-art methods in both compound and single-weather scenarios. In addition, our fusion results excel in downstream tasks covering semantic segmentation and object detection, confirming the practical value in real-world adverse weather perception. The source code will be available at https://github.com/Feecuin/CAWM-Mamba.

