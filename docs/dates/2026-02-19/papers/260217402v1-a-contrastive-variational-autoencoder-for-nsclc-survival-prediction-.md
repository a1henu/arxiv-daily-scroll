---
layout: default
title: A Contrastive Variational AutoEncoder for NSCLC Survival Prediction with Missing Modalities
---

# A Contrastive Variational AutoEncoder for NSCLC Survival Prediction with Missing Modalities
**arXiv**：[2602.17402v1](https://arxiv.org/abs/2602.17402) · [PDF](https://arxiv.org/pdf/2602.17402.pdf)  
**作者**：Michele Zanitti, Vanja Miskovic, Francesco Trovò, Alessandra Laura Giulia Pedrocchi, Ming Shen, Yan Kyaw Tun, Arsela Prelaj, Sokol Kosta  

**一句话要点**：提出多模态对比变分自编码器以解决非小细胞肺癌生存预测中模态缺失的鲁棒性问题

**关键词**：多模态学习, 生存预测, 变分自编码器, 对比学习, 模态缺失, 非小细胞肺癌

## 3 点简述
- 核心问题：真实临床数据常缺失模态，现有模型在严重缺失时缺乏鲁棒性。
- 方法要点：使用模态特定变分编码器、融合瓶颈与多任务目标，包括对比损失和随机模态掩码。
- 实验或效果：在TCGA数据集上验证了疾病特异性生存预测的有效性和对严重缺失的鲁棒性。

## 摘要（原文）

> Predicting survival outcomes for non-small cell lung cancer (NSCLC) patients is challenging due to the different individual prognostic features. This task can benefit from the integration of whole-slide images, bulk transcriptomics, and DNA methylation, which offer complementary views of the patient's condition at diagnosis. However, real-world clinical datasets are often incomplete, with entire modalities missing for a significant fraction of patients. State-of-the-art models rely on available data to create patient-level representations or use generative models to infer missing modalities, but they lack robustness in cases of severe missingness. We propose a Multimodal Contrastive Variational AutoEncoder (MCVAE) to address this issue: modality-specific variational encoders capture the uncertainty in each data source, and a fusion bottleneck with learned gating mechanisms is introduced to normalize the contributions from present modalities. We propose a multi-task objective that combines survival loss and reconstruction loss to regularize patient representations, along with a cross-modal contrastive loss that enforces cross-modal alignment in the latent space. During training, we apply stochastic modality masking to improve the robustness to arbitrary missingness patterns. Extensive evaluations on the TCGA-LUAD (n=475) and TCGA-LUSC (n=446) datasets demonstrate the efficacy of our approach in predicting disease-specific survival (DSS) and its robustness to severe missingness scenarios compared to two state-of-the-art models. Finally, we bring some clarifications on multimodal integration by testing our model on all subsets of modalities, finding that integration is not always beneficial to the task.

