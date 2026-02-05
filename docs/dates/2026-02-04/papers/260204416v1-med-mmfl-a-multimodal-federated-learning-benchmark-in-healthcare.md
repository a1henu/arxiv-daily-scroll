---
layout: default
title: Med-MMFL: A Multimodal Federated Learning Benchmark in Healthcare
---

# Med-MMFL: A Multimodal Federated Learning Benchmark in Healthcare
**arXiv**：[2602.04416v1](https://arxiv.org/abs/2602.04416) · [PDF](https://arxiv.org/pdf/2602.04416.pdf)  
**作者**：Aavash Chhetri, Bibek Niroula, Pratik Shrestha, Yash Raj Shrestha, Lesley A Anderson, Prashnna K Gyawali, Loris Bazzani, Binod Bhattarai  

**一句话要点**：提出Med-MMFL基准以解决医疗多模态联邦学习缺乏标准化评估的问题

**关键词**：多模态联邦学习, 医疗基准, 数据隐私, 模态对齐, 非独立同分布, 可复现性

## 3 点简述
- 医疗多模态联邦学习缺乏统一基准，阻碍系统化研究进展
- 涵盖10种模态、多种任务和联邦场景，评估六种先进FL算法
- 在自然和合成联邦设置下进行实验，支持可复现性和公平比较

## 摘要（原文）

> Federated learning (FL) enables collaborative model training across decentralized medical institutions while preserving data privacy. However, medical FL benchmarks remain scarce, with existing efforts focusing mainly on unimodal or bimodal modalities and a limited range of medical tasks. This gap underscores the need for standardized evaluation to advance systematic understanding in medical MultiModal FL (MMFL). To this end, we introduce Med-MMFL, the first comprehensive MMFL benchmark for the medical domain, encompassing diverse modalities, tasks, and federation scenarios. Our benchmark evaluates six representative state-of-the-art FL algorithms, covering different aggregation strategies, loss formulations, and regularization techniques. It spans datasets with 2 to 4 modalities, comprising a total of 10 unique medical modalities, including text, pathology images, ECG, X-ray, radiology reports, and multiple MRI sequences. Experiments are conducted across naturally federated, synthetic IID, and synthetic non-IID settings to simulate real-world heterogeneity. We assess segmentation, classification, modality alignment (retrieval), and VQA tasks. To support reproducibility and fair comparison of future multimodal federated learning (MMFL) methods under realistic medical settings, we release the complete benchmark implementation, including data processing and partitioning pipelines, at https://github.com/bhattarailab/Med-MMFL-Benchmark .

