---
layout: default
title: Longitudinal NSCLC Treatment Progression via Multimodal Generative Models
---

# Longitudinal NSCLC Treatment Progression via Multimodal Generative Models
**arXiv**：[2603.06147v1](https://arxiv.org/abs/2603.06147) · [PDF](https://arxiv.org/pdf/2603.06147.pdf)  
**作者**：Massimiliano Mantegna, Elena Mulero Ayllón, Alice Natalina Caragliano, Francesco Di Feola, Claudia Tacconi, Michele Fiore, Edy Ippolito, Carlo Greco, Sara Ramella, Philippe C. Cattin, Paolo Soda, Matteo Tortora, Valerio Guarrasi  

**一句话要点**：提出虚拟治疗框架，通过多模态生成模型预测非小细胞肺癌放疗期间的肿瘤演变。

**关键词**：非小细胞肺癌, 多模态生成模型, 放疗预测, 图像到图像翻译, 剂量感知, 纵向分析

## 3 点简述
- 核心问题：预测放疗期间肿瘤演变，涉及解剖和治疗驱动的纵向变化。
- 方法要点：将肿瘤进展建模为剂量感知的多模态条件图像到图像翻译问题。
- 实验或效果：在222名患者数据集上评估，扩散模型在多模态条件下表现更稳定和合理。

## 摘要（原文）

> Predicting tumor evolution during radiotherapy is a clinically critical challenge, particularly when longitudinal changes are driven by both anatomy and treatment. In this work, we introduce a Virtual Treatment (VT) framework that formulates non-small cell lung cancer (NSCLC) progression as a dose-aware multimodal conditional image-to-image translation problem. Given a CT scan, baseline clinical variables, and a specified radiation dose increment, VT aims to synthesize plausible follow-up CT images reflecting treatment-induced anatomical changes. We evaluate the proposed framework on a longitudinal dataset of 222 stage III NSCLC patients, comprising 895 CT scans acquired during radiotherapy under irregular clinical schedules. The generative process is conditioned on delivered dose increments together with demographic and tumor-related clinical variables. Representative GAN-based and diffusion-based models are benchmarked across 2D and 2.5D configurations. Quantitative and qualitative results indicate that diffusion-based models benefit more consistently from multimodal, dose-aware conditioning and produce more stable and anatomically plausible tumor evolution trajectories than GAN-based baselines, supporting the potential of VT as a tool for in-silico treatment monitoring and adaptive radiotherapy research in NSCLC.

