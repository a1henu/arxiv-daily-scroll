---
layout: default
title: DCCS-Det: Directional Context and Cross-Scale-Aware Detector for Infrared Small Target
---

# DCCS-Det: Directional Context and Cross-Scale-Aware Detector for Infrared Small Target
**arXiv**：[2601.16428v1](https://arxiv.org/abs/2601.16428) · [PDF](https://arxiv.org/pdf/2601.16428.pdf)  
**作者**：Shuying Li, Qiang Ma, San Zhang, Chuang Yang  

**一句话要点**：提出DCCS-Det以解决红外小目标检测中局部-全局特征建模不足和特征退化问题

**关键词**：红外小目标检测, 方向感知上下文, 跨尺度特征提取, 双流显著性增强, 潜在感知语义聚合, 随机池化采样

## 3 点简述
- 核心问题：现有方法在局部-全局特征联合建模不足，导致目标-背景区分困难，且特征冗余和语义稀释降低目标表示质量。
- 方法要点：引入双流显著性增强块整合局部感知与方向感知上下文聚合，以及潜在感知语义提取与聚合模块通过跨尺度特征提取和随机池化采样缓解特征退化。
- 实验或效果：在多个数据集上实现最先进的检测精度和竞争性效率，消融研究验证了DSE和LaSEA在复杂场景下提升目标感知和特征表示的有效性。

## 摘要（原文）

> Infrared small target detection (IRSTD) is critical for applications like remote sensing and surveillance, which aims to identify small, low-contrast targets against complex backgrounds. However, existing methods often struggle with inadequate joint modeling of local-global features (harming target-background discrimination) or feature redundancy and semantic dilution (degrading target representation quality). To tackle these issues, we propose DCCS-Det (Directional Context and Cross-Scale Aware Detector for Infrared Small Target), a novel detector that incorporates a Dual-stream Saliency Enhancement (DSE) block and a Latent-aware Semantic Extraction and Aggregation (LaSEA) module. The DSE block integrates localized perception with direction-aware context aggregation to help capture long-range spatial dependencies and local details. On this basis, the LaSEA module mitigates feature degradation via cross-scale feature extraction and random pooling sampling strategies, enhancing discriminative features and suppressing noise. Extensive experiments show that DCCS-Det achieves state-of-the-art detection accuracy with competitive efficiency across multiple datasets. Ablation studies further validate the contributions of DSE and LaSEA in improving target perception and feature representation under complex scenarios. \href{https://huggingface.co/InPeerReview/InfraredSmallTargetDetection-IRSTD.DCCS}{DCCS-Det Official Code is Available Here!}

