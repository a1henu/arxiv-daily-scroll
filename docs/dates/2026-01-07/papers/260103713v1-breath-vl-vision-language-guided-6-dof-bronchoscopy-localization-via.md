---
layout: default
title: BREATH-VL: Vision-Language-Guided 6-DoF Bronchoscopy Localization via Semantic-Geometric Fusion
---

# BREATH-VL: Vision-Language-Guided 6-DoF Bronchoscopy Localization via Semantic-Geometric Fusion
**arXiv**：[2601.03713v1](https://arxiv.org/abs/2601.03713) · [PDF](https://arxiv.org/pdf/2601.03713.pdf)  
**作者**：Qingyao Tian, Bingyu Yang, Huai Liao, Xinyan Huang, Junyong Li, Dong Yi, Hongbin Liu  

**一句话要点**：提出BREATH-VL框架，通过语义-几何融合实现支气管镜6自由度定位

**关键词**：视觉-语言模型, 6自由度定位, 支气管镜导航, 语义-几何融合, 轻量级上下文学习, 医疗数据集

## 3 点简述
- 问题：缺乏大规模高质量医疗视觉-语言数据集，VLM在细粒度姿态回归和时序特征提取上存在局限
- 方法：构建BREATH数据集，结合VLM语义理解与视觉配准几何信息，引入轻量级上下文学习机制
- 效果：在准确性和泛化性上超越视觉基线方法，平移误差降低25.5%，计算延迟具有竞争力

## 摘要（原文）

> Vision-language models (VLMs) have recently shown remarkable performance in navigation and localization tasks by leveraging large-scale pretraining for semantic understanding. However, applying VLMs to 6-DoF endoscopic camera localization presents several challenges: 1) the lack of large-scale, high-quality, densely annotated, and localization-oriented vision-language datasets in real-world medical settings; 2) limited capability for fine-grained pose regression; and 3) high computational latency when extracting temporal features from past frames. To address these issues, we first construct BREATH dataset, the largest in-vivo endoscopic localization dataset to date, collected in the complex human airway. Building on this dataset, we propose BREATH-VL, a hybrid framework that integrates semantic cues from VLMs with geometric information from vision-based registration methods for accurate 6-DoF pose estimation. Our motivation lies in the complementary strengths of both approaches: VLMs offer generalizable semantic understanding, while registration methods provide precise geometric alignment. To further enhance the VLM's ability to capture temporal context, we introduce a lightweight context-learning mechanism that encodes motion history as linguistic prompts, enabling efficient temporal reasoning without expensive video-level computation. Extensive experiments demonstrate that the vision-language module delivers robust semantic localization in challenging surgical scenes. Building on this, our BREATH-VL outperforms state-of-the-art vision-only localization methods in both accuracy and generalization, reducing translational error by 25.5% compared with the best-performing baseline, while achieving competitive computational latency.

