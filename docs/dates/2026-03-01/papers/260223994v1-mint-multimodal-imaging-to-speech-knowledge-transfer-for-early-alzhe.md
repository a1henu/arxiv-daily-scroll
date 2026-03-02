---
layout: default
title: MINT: Multimodal Imaging-to-Speech Knowledge Transfer for Early Alzheimer's Screening
---

# MINT: Multimodal Imaging-to-Speech Knowledge Transfer for Early Alzheimer's Screening
**arXiv**：[2602.23994v1](https://arxiv.org/abs/2602.23994) · [PDF](https://arxiv.org/pdf/2602.23994.pdf)  
**作者**：Vrushank Ahire, Yogesh Kumar, Anouck Girard, M. A. Ganaie  

**一句话要点**：提出MINT框架，通过MRI到语音的知识转移，实现无成像的早期阿尔茨海默病筛查。

**关键词**：知识转移, 多模态学习, 阿尔茨海默病筛查, 神经成像, 语音分析, 几何对齐

## 3 点简述
- 核心问题：神经成像成本高，仅语音分类器缺乏生物学基础，难以区分认知正常与轻度认知障碍。
- 方法要点：使用MRI教师模型定义嵌入空间，通过几何损失对齐语音表示，保持成像编码器保真度。
- 实验或效果：在ADNI-4上，对齐语音性能接近仅语音基线，多模态融合优于单独MRI，无需推理时成像。

## 摘要（原文）

> Alzheimer's disease is a progressive neurodegenerative disorder in which mild cognitive impairment (MCI) marks a critical transition between aging and dementia. Neuroimaging modalities, such as structural MRI, provide biomarkers of this transition; however, their high costs and infrastructure needs limit their deployment at a population scale. Speech analysis offers a non-invasive alternative, but speech-only classifiers are developed independently of neuroimaging, leaving decision boundaries biologically ungrounded and limiting reliability on the subtle CN-versus-MCI distinction. We propose MINT (Multimodal Imaging-to-Speech Knowledge Transfer), a three-stage cross-modal framework that transfers biomarker structure from MRI into a speech encoder at training time. An MRI teacher, trained on 1,228 subjects, defines a compact neuroimaging embedding space for CN-versus-MCI classification. A residual projection head aligns speech representations to this frozen imaging manifold via a combined geometric loss, adapting speech to the learned biomarker space while preserving imaging encoder fidelity. The frozen MRI classifier, which is never exposed to speech, is applied to aligned embeddings at inference and requires no scanner. Evaluation on ADNI-4 shows aligned speech achieves performance comparable to speech-only baselines (AUC 0.720 vs 0.711) while requiring no imaging at inference, demonstrating that MRI-derived decision boundaries can ground speech representations. Multimodal fusion improves over MRI alone (0.973 vs 0.958). Ablation studies identify dropout regularization and self-supervised pretraining as critical design decisions. To our knowledge, this is the first demonstration of MRI-to-speech knowledge transfer for early Alzheimer's screening, establishing a biologically grounded pathway for population-level cognitive triage without neuroimaging at inference.

