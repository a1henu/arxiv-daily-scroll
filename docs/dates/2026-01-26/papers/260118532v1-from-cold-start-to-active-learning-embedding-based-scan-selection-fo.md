---
layout: default
title: From Cold Start to Active Learning: Embedding-Based Scan Selection for Medical Image Segmentation
---

# From Cold Start to Active Learning: Embedding-Based Scan Selection for Medical Image Segmentation
**arXiv**：[2601.18532v1](https://arxiv.org/abs/2601.18532) · [PDF](https://arxiv.org/pdf/2601.18532.pdf)  
**作者**：Devon Levy, Bar Assayag, Laura Gaspar, Ilan Shimshoni, Bella Specktor-Fadida  

**一句话要点**：提出基于嵌入与聚类的冷启动采样和不确定性主动学习框架，提升医学图像分割在低数据场景下的准确性。

**关键词**：医学图像分割, 主动学习, 冷启动采样, 嵌入聚类, 不确定性选择, 低数据场景

## 3 点简述
- 核心问题：医学图像分割中手动标注成本高，主动学习需有效选择信息样本以降低标注负担。
- 方法要点：冷启动阶段结合基础模型嵌入与聚类，自动选择聚类数并按比例采样；主动学习阶段集成空间多样性指导不确定性选择。
- 实验或效果：在X射线和MRI数据集上验证，冷启动和主动学习均优于基线，提升Dice分数并降低Hausdorff距离。

## 摘要（原文）

> Accurate segmentation annotations are critical for disease monitoring, yet manual labeling remains a major bottleneck due to the time and expertise required. Active learning (AL) alleviates this burden by prioritizing informative samples for annotation, typically through a diversity-based cold-start phase followed by uncertainty-driven selection. We propose a novel cold-start sampling strategy that combines foundation-model embeddings with clustering, including automatic selection of the number of clusters and proportional sampling across clusters, to construct a diverse and representative initial training. This is followed by an uncertainty-based AL framework that integrates spatial diversity to guide sample selection. The proposed method is intuitive and interpretable, enabling visualization of the feature-space distribution of candidate samples. We evaluate our approach on three datasets spanning X-ray and MRI modalities. On the CheXmask dataset, the cold-start strategy outperforms random selection, improving Dice from 0.918 to 0.929 and reducing the Hausdorff distance from 32.41 to 27.66 mm. In the AL setting, combined entropy and diversity selection improves Dice from 0.919 to 0.939 and reduces the Hausdorff distance from 30.10 to 19.16 mm. On the Montgomery dataset, cold-start gains are substantial, with Dice improving from 0.928 to 0.950 and Hausdorff distance decreasing from 14.22 to 9.38 mm. On the SynthStrip dataset, cold-start selection slightly affects Dice but reduces the Hausdorff distance from 9.43 to 8.69 mm, while active learning improves Dice from 0.816 to 0.826 and reduces the Hausdorff distance from 7.76 to 6.38 mm. Overall, the proposed framework consistently outperforms baseline methods in low-data regimes, improving segmentation accuracy.

