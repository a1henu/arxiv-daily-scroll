---
layout: default
title: MMCTOP: A Multimodal Textualization and Mixture-of-Experts Framework for Clinical Trial Outcome Prediction
---

# MMCTOP: A Multimodal Textualization and Mixture-of-Experts Framework for Clinical Trial Outcome Prediction
**arXiv**：[2512.21897v1](https://arxiv.org/abs/2512.21897) · [PDF](https://arxiv.org/pdf/2512.21897.pdf)  
**作者**：Carolina Aparício, Qi Shi, Bo Wen, Tesfaye Yadete, Qiwei Han  

**一句话要点**：提出MMCTOP框架，通过多模态文本化和专家混合解决临床试验结果预测中的异构数据融合挑战。

**关键词**：多模态数据融合, 临床试验结果预测, 稀疏专家混合, 模式感知表示学习, 生物医学信息学

## 3 点简述
- 核心问题：高维生物医学信息学中多模态数据融合的挑战，涉及分子结构、协议元数据和疾病本体等异构信号。
- 方法要点：结合模式感知表示学习和药物-疾病条件稀疏专家混合，通过模式特定编码器和变压器骨干实现对齐嵌入融合。
- 实验或效果：在基准数据集上，MMCTOP在精度、F1和AUC方面优于单模态和多模态基线，并通过消融实验验证了文本化和专家路由的贡献。

## 摘要（原文）

> Addressing the challenge of multimodal data fusion in high-dimensional biomedical informatics, we propose MMCTOP, a MultiModal Clinical-Trial Outcome Prediction framework that integrates heterogeneous biomedical signals spanning (i) molecular structure representations, (ii) protocol metadata and long-form eligibility narratives, and (iii) disease ontologies. MMCTOP couples schema-guided textualization and input-fidelity validation with modality-aware representation learning, in which domain-specific encoders generate aligned embeddings that are fused by a transformer backbone augmented with a drug-disease-conditioned sparse Mixture-of-Experts (SMoE). This design explicitly supports specialization across therapeutic and design subspaces while maintaining scalable computation through top-k routing. MMCTOP achieves consistent improvements in precision, F1, and AUC over unimodal and multimodal baselines on benchmark datasets, and ablations show that schema-guided textualization and selective expert routing contribute materially to performance and stability. We additionally apply temperature scaling to obtain calibrated probabilities, ensuring reliable risk estimation for downstream decision support. Overall, MMCTOP advances multimodal trial modeling by combining controlled narrative normalization, context-conditioned expert fusion, and operational safeguards aimed at auditability and reproducibility in biomedical informatics.

