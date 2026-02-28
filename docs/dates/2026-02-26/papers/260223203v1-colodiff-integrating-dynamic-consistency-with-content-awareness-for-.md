---
layout: default
title: ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation
---

# ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation
**arXiv**：[2602.23203v1](https://arxiv.org/abs/2602.23203) · [PDF](https://arxiv.org/pdf/2602.23203.pdf)  
**作者**：Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  

**一句话要点**：提出ColoDiff框架，通过动态一致性与内容感知生成结肠镜视频以缓解数据稀缺问题。

**关键词**：结肠镜视频生成, 扩散模型, 时间一致性, 内容感知控制, 非马尔可夫采样, 临床数据增强

## 3 点简述
- 核心问题：结肠镜视频生成需处理不规则肠道结构、多样疾病表征和成像模态，确保时间一致性和临床属性精确控制。
- 方法要点：TimeStream模块解耦时间依赖，Content-Aware模块注入噪声嵌入和可学习原型实现精细控制，非马尔可夫采样加速生成。
- 实验或效果：在多个数据集评估，生成视频过渡平滑、动态丰富，提升下游任务如疾病诊断和病变分割性能。

## 摘要（原文）

> Colonoscopy video generation delivers dynamic, information-rich data critical for diagnosing intestinal diseases, particularly in data-scarce scenarios. High-quality video generation demands temporal consistency and precise control over clinical attributes, but faces challenges from irregular intestinal structures, diverse disease representations, and various imaging modalities. To this end, we propose ColoDiff, a diffusion-based framework that generates dynamic-consistent and content-aware colonoscopy videos, aiming to alleviate data shortage and assist clinical analysis. At the inter-frame level, our TimeStream module decouples temporal dependency from video sequences through a cross-frame tokenization mechanism, enabling intricate dynamic modeling despite irregular intestinal structures. At the intra-frame level, our Content-Aware module incorporates noise-injected embeddings and learnable prototypes to realize precise control over clinical attributes, breaking through the coarse guidance of diffusion models. Additionally, ColoDiff employs a non-Markovian sampling strategy that cuts steps by over 90% for real-time generation. ColoDiff is evaluated across three public datasets and one hospital database, based on both generation metrics and downstream tasks including disease diagnosis, modality discrimination, bowel preparation scoring, and lesion segmentation. Extensive experiments show ColoDiff generates videos with smooth transitions and rich dynamics. ColoDiff presents an effort in controllable colonoscopy video generation, revealing the potential of synthetic videos in complementing authentic representation and mitigating data scarcity in clinical settings.

