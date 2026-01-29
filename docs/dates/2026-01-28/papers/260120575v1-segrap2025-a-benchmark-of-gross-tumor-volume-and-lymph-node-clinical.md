---
layout: default
title: SegRap2025: A Benchmark of Gross Tumor Volume and Lymph Node Clinical Target Volume Segmentation for Radiotherapy Planning of Nasopharyngeal Carcinoma
---

# SegRap2025: A Benchmark of Gross Tumor Volume and Lymph Node Clinical Target Volume Segmentation for Radiotherapy Planning of Nasopharyngeal Carcinoma
**arXiv**：[2601.20575v1](https://arxiv.org/abs/2601.20575) · [PDF](https://arxiv.org/pdf/2601.20575.pdf)  
**作者**：Jia Fu, Litingyu Wang, He Li, Zihao Luo, Huamin Wang, Chenyuan Bian, Zijun Gao, Chunbin Gu, Xin Weng, Jianghao Wu, Yicheng Wu, Jin Ye, Linhao Li, Yiwen Ye, Yong Xia, Elias Tappeiner, Fei He, Abdul qayyum, Moona Mazher, Steven A Niederer, Junqiang Chen, Chuanyi Huang, Lisheng Wang, Zhaohu Xing, Hongqiu Wang, Lei Zhu, Shichuan Zhang, Shaoting Zhang, Wenjun Liao, Guotai Wang  

**一句话要点**：提出SegRap2025基准以评估鼻咽癌放疗靶区分割的跨中心和跨模态泛化性

**关键词**：医学图像分割, 放疗规划, 鼻咽癌, 泛化性评估, 多模态CT, 基准数据集

## 3 点简述
- 核心问题：鼻咽癌放疗规划中，从CT扫描准确分割原发肿瘤体积和淋巴结临床靶区面临跨中心和跨模态的泛化挑战。
- 方法要点：基于SegRap2023扩展，构建多中心多模态数据集，设置两个任务分别评估原发肿瘤和淋巴结靶区分割的泛化与鲁棒性。
- 实验或效果：在内部和外部测试集上，最佳模型在原发肿瘤分割任务中平均DSC分别为74.61%和56.79%，淋巴结分割任务中在配对CT、增强CT和非增强CT子集上分别达到60.24%、60.50%和57.23%。

## 摘要（原文）

> Accurate delineation of Gross Tumor Volume (GTV), Lymph Node Clinical Target Volume (LN CTV), and Organ-at-Risk (OAR) from Computed Tomography (CT) scans is essential for precise radiotherapy planning in Nasopharyngeal Carcinoma (NPC). Building upon SegRap2023, which focused on OAR and GTV segmentation using single-center paired non-contrast CT (ncCT) and contrast-enhanced CT (ceCT) scans, the SegRap2025 challenge aims to enhance the generalizability and robustness of segmentation models across imaging centers and modalities. SegRap2025 comprises two tasks: Task01 addresses GTV segmentation using paired CT from the SegRap2023 dataset, with an additional external testing set to evaluate cross-center generalization, and Task02 focuses on LN CTV segmentation using multi-center training data and an unseen external testing set, where each case contains paired CT scans or a single modality, emphasizing both cross-center and cross-modality robustness. This paper presents the challenge setup and provides a comprehensive analysis of the solutions submitted by ten participating teams. For GTV segmentation task, the top-performing models achieved average Dice Similarity Coefficient (DSC) of 74.61% and 56.79% on the internal and external testing cohorts, respectively. For LN CTV segmentation task, the highest average DSC values reached 60.24%, 60.50%, and 57.23% on paired CT, ceCT-only, and ncCT-only subsets, respectively. SegRap2025 establishes a large-scale multi-center, multi-modality benchmark for evaluating the generalization and robustness in radiotherapy target segmentation, providing valuable insights toward clinically applicable automated radiotherapy planning systems. The benchmark is available at: https://hilab-git.github.io/SegRap2025_Challenge.

