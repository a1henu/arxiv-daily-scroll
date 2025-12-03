---
layout: default
title: Tissue-mask supported inter-subject whole-body image registration in the UK Biobank - A method benchmarking study
---

# Tissue-mask supported inter-subject whole-body image registration in the UK Biobank - A method benchmarking study
**arXiv**：[2512.02702v1](https://arxiv.org/abs/2512.02702) · [PDF](https://arxiv.org/pdf/2512.02702.pdf)  
**作者**：Yasemin Utkueri, Elin Lundström, Håkan Ahlström, Johan Öfverstedt, Joel Kullberg  

**一句话要点**：提出基于组织掩码的性别分层全身图像配准方法，提升UK Biobank数据配准精度

**关键词**：全身图像配准, 组织掩码, UK Biobank, 性别分层, 图割配准, 医学图像分析

## 3 点简述
- 核心问题：UK Biobank大规模全身MR图像需跨受试者配准以实现空间标准化和相关性分析。
- 方法要点：使用VIBESegmentator生成皮下脂肪和肌肉掩码，增强基于强度的图割配准，并分性别处理。
- 实验或效果：在4000名受试者上评估，相比基线方法Dice分数提升6-13个百分点，年龄相关性图谱更清晰。

## 摘要（原文）

> The UK Biobank is a large-scale study collecting whole-body MR imaging and non-imaging health data. Robust and accurate inter-subject image registration of these whole-body MR images would enable their body-wide spatial standardization, and region-/voxel-wise correlation analysis of non-imaging data with image-derived parameters (e.g., tissue volume or fat content).
>   We propose a sex-stratified inter-subject whole-body MR image registration approach that uses subcutaneous adipose tissue- and muscle-masks from the state-of-the-art VIBESegmentator method to augment intensity-based graph-cut registration. The proposed method was evaluated on a subset of 4000 subjects by comparing it to an intensity-only method as well as two previously published registration methods, uniGradICON and MIRTK. The evaluation comprised overlap measures applied to the 71 VIBESegmentator masks: 1) Dice scores, and 2) voxel-wise label error frequency. Additionally, voxel-wise correlation between age and each of fat content and tissue volume was studied to exemplify the usefulness for medical research.
>   The proposed method exhibited a mean dice score of 0.77 / 0.75 across the cohort and the 71 masks for males/females, respectively. When compared to the intensity-only registration, the mean values were 6 percentage points (pp) higher for both sexes, and the label error frequency was decreased in most tissue regions. These differences were 9pp / 8pp against uniGradICON and 12pp / 13pp against MIRTK. Using the proposed method, the age-correlation maps were less noisy and showed higher anatomical alignment.
>   In conclusion, the image registration method using two tissue masks improves whole-body registration of UK Biobank images.

