---
layout: default
title: Scaling Audio-Visual Quality Assessment Dataset via Crowdsourcing
---

# Scaling Audio-Visual Quality Assessment Dataset via Crowdsourcing
**arXiv**：[2602.22659v1](https://arxiv.org/abs/2602.22659) · [PDF](https://arxiv.org/pdf/2602.22659.pdf)  
**作者**：Renyu Yang, Jian Jin, Lili Meng, Meiqin Liu, Yilin Wang, Balu Adsumilli, Weisi Lin  

**一句话要点**：提出基于众包的音视频质量评估数据集构建方法，以解决现有数据集规模小、多样性不足的问题。

**关键词**：音视频质量评估, 众包标注, 多模态感知, 数据集构建, 主观实验

## 3 点简述
- 核心问题：现有音视频质量评估数据集规模小、内容与质量多样性不足，仅提供整体评分，限制模型开发与多模态感知研究。
- 方法要点：设计众包主观实验框架，打破实验室限制，确保跨环境可靠标注；采用系统数据准备策略，覆盖广泛质量水平和语义场景；扩展额外标注，支持多模态感知机制研究。
- 实验或效果：通过YT-NTU-AVQ数据集验证，该数据集包含1,620个用户生成的音视频序列，是目前最大且最多样化的音视频质量评估数据集。

## 摘要（原文）

> Audio-visual quality assessment (AVQA) research has been stalled by limitations of existing datasets: they are typically small in scale, with insufficient diversity in content and quality, and annotated only with overall scores. These shortcomings provide limited support for model development and multimodal perception research. We propose a practical approach for AVQA dataset construction. First, we design a crowdsourced subjective experiment framework for AVQA, breaks the constraints of in-lab settings and achieves reliable annotation across varied environments. Second, a systematic data preparation strategy is further employed to ensure broad coverage of both quality levels and semantic scenarios. Third, we extend the dataset with additional annotations, enabling research on multimodal perception mechanisms and their relation to content. Finally, we validate this approach through YT-NTU-AVQ, the largest and most diverse AVQA dataset to date, consisting of 1,620 user-generated audio and video (A/V) sequences. The dataset and platform code are available at https://github.com/renyu12/YT-NTU-AVQ

