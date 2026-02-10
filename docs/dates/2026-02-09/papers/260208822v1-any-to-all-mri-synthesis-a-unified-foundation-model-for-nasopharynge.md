---
layout: default
title: Any-to-All MRI Synthesis: A Unified Foundation Model for Nasopharyngeal Carcinoma and Its Downstream Applications
---

# Any-to-All MRI Synthesis: A Unified Foundation Model for Nasopharyngeal Carcinoma and Its Downstream Applications
**arXiv**：[2602.08822v1](https://arxiv.org/abs/2602.08822) · [PDF](https://arxiv.org/pdf/2602.08822.pdf)  
**作者**：Yao Pu, Yiming Shi, Zhenxi Zhang, Peixin Yu, Yitao Zhuang, Xiang Wang, Hongzhao Chen, Jing Cai, Ge Ren  

**一句话要点**：提出统一基础模型实现任意到全模态MRI合成，以提升鼻咽癌放疗规划准确性。

**关键词**：MRI合成, 基础模型, 视觉-语言对齐, 鼻咽癌放疗, 对比学习, 模态不变表示

## 3 点简述
- 核心问题：临床MRI模态不完整影响鼻咽癌放疗精度，传统方法适应性差且缺乏可解释性。
- 方法要点：集成对比视觉表示学习和视觉-语言对齐，支持任意到全模态合成。
- 实验或效果：在26个验证站点上平均SSIM达0.90、PSNR达27，增强下游任务如分割。

## 摘要（原文）

> Magnetic resonance imaging (MRI) is essential for nasopharyngeal carcinoma (NPC) radiotherapy (RT), but practical constraints, such as patient discomfort, long scan times, and high costs often lead to incomplete modalities in clinical practice, compromising RT planning accuracy. Traditional MRI synthesis methods are modality-specific, limited in anatomical adaptability, and lack clinical interpretability-failing to meet NPC's RT needs. Here, we developed a unified foundation model integrating contrastive visual representation learning and vision-language alignment (VLA) to enable any-to-all MRI synthesis. The model uses a contrastive encoder for modality-invariant representations and a CLIP-based text-informed decoder for semantically consistent synthesis, supporting any-to-all MRI synthesis via one unified foundation model. Trained on 40,825 images from 13 institutions, it achieves consistently high performance (average SSIM 0.90, PSNR 27) across 26 internal/external validation sites (15,748 images), with superior synthesis fidelity and robustness to noise and domain shifts. Meanwhile, its unified representation enhances downstream RT-relevant tasks (e.g., segmentation). This work advances digital medicine solutions for NPC care by leveraging foundation models to bridge technical synthesis and clinical utility.

