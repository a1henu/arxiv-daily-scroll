---
layout: default
title: Towards Personalized Multi-Modal MRI Synthesis across Heterogeneous Datasets
---

# Towards Personalized Multi-Modal MRI Synthesis across Heterogeneous Datasets
**arXiv**：[2602.19723v1](https://arxiv.org/abs/2602.19723) · [PDF](https://arxiv.org/pdf/2602.19723.pdf)  
**作者**：Yue Zhang, Zhizheng Zhuo, Siyao Xu, Shan Lv, Zhaoxi Liu, Jun Qiu, Qiuli Wang, Yaou Liu, S. Kevin Zhou  

**一句话要点**：提出PMM-Synth框架以解决多模态MRI合成在异构数据集间的泛化问题

**关键词**：多模态MRI合成, 跨数据集泛化, 个性化特征调制, 模态一致批量调度, 选择性监督损失, 临床数据集评估

## 3 点简述
- 核心问题：现有统一合成模型训练和评估局限于单一数据集，泛化能力不足，影响实际部署。
- 方法要点：通过个性化特征调制、模态一致批量调度和选择性监督损失，实现跨异构数据集的有效泛化。
- 实验或效果：在四个临床数据集上，PMM-Synth在多种合成任务中优于现有方法，PSNR和SSIM得分更高，并提升下游任务性能。

## 摘要（原文）

> Synthesizing missing modalities in multi-modal magnetic resonance imaging (MRI) is vital for ensuring diagnostic completeness, particularly when full acquisitions are infeasible due to time constraints, motion artifacts, and patient tolerance. Recent unified synthesis models have enabled flexible synthesis tasks by accommodating various input-output configurations. However, their training and evaluation are typically restricted to a single dataset, limiting their generalizability across diverse clinical datasets and impeding practical deployment. To address this limitation, we propose PMM-Synth, a personalized MRI synthesis framework that not only supports various synthesis tasks but also generalizes effectively across heterogeneous datasets. PMM-Synth is jointly trained on multiple multi-modal MRI datasets that differ in modality coverage, disease types, and intensity distributions. It achieves cross-dataset generalization through three core innovations: a Personalized Feature Modulation module that dynamically adapts feature representations based on dataset identifier to mitigate the impact of distributional shifts; a Modality-Consistent Batch Scheduler that facilitates stable and efficient batch training under inconsistent modality conditions; and a selective supervision loss to ensure effective learning when ground truth modalities are partially missing. Evaluated on four clinical multi-modal MRI datasets, PMM-Synth consistently outperforms state-of-the-art methods in both one-to-one and many-to-one synthesis tasks, achieving superior PSNR and SSIM scores. Qualitative results further demonstrate improved preservation of anatomical structures and pathological details. Additionally, downstream tumor segmentation and radiological reporting studies suggest that PMM-Synth holds potential for supporting reliable diagnosis under real-world modality-missing scenarios.

