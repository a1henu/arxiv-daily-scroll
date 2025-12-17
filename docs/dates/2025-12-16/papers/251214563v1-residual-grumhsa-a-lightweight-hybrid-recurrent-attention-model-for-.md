---
layout: default
title: Residual GRU+MHSA: A Lightweight Hybrid Recurrent Attention Model for Cardiovascular Disease Detection
---

# Residual GRU+MHSA: A Lightweight Hybrid Recurrent Attention Model for Cardiovascular Disease Detection
**arXiv**：[2512.14563v1](https://arxiv.org/abs/2512.14563) · [PDF](https://arxiv.org/pdf/2512.14563.pdf)  
**作者**：Tejaswani Dash, Gautam Datla, Anudeep Vurity, Tazeem Ahmad, Mohd Adnan, Saima Rafi, Saisha Patro, Saina Patro  

**一句话要点**：提出Residual GRU+MHSA轻量混合模型，用于心血管疾病检测的临床记录分析。

**关键词**：心血管疾病检测, 轻量混合模型, 残差GRU, 多头自注意力, 临床记录分析, 资源受限部署

## 3 点简述
- 心血管疾病检测需可靠预测工具，传统方法依赖手工特征，机器学习泛化性差。
- 模型集成残差双向GRU、通道重加权和多头自注意力池化，处理表格临床数据。
- 在UCI数据集上评估，准确率0.861，优于经典和深度学习基线，支持资源受限部署。

## 摘要（原文）

> Cardiovascular disease (CVD) remains the leading cause of mortality worldwide, underscoring the need for reliable and efficient predictive tools that support early intervention. Traditional diagnostic approaches rely on handcrafted features and clinician expertise, while machine learning methods improve reproducibility but often struggle to generalize across noisy and heterogeneous clinical data. In this work, we propose Residual GRU with Multi-Head Self-Attention, a compact deep learning architecture designed for tabular clinical records. The model integrates residual bidirectional gated recurrent units for sequential modeling of feature columns, a channel reweighting block, and multi-head self-attention pooling with a learnable classification token to capture global context. We evaluate the model on the UCI Heart Disease dataset using 5-fold stratified cross-validation and compare it against classical methods such as Logistic Regression, Random Forest, and Support Vector Machines, as well as modern deep learning baselines including DeepMLP, convolutional networks, recurrent networks, and Transformers. The proposed model achieves an accuracy of 0.861, macro-F1 of 0.860, ROC-AUC of 0.908, and PR-AUC of 0.904, outperforming all baselines. Ablation studies confirm the individual contributions of residual recurrence, channel gating, and attention pooling. t-SNE visualizations further indicate that the learned embeddings exhibit clearer separation between disease and non-disease classes compared to raw features. These results demonstrate that lightweight hybrid recurrent and attention-based architectures provide a strong balance between accuracy and efficiency for clinical risk prediction, supporting deployment in resource-constrained healthcare settings.

