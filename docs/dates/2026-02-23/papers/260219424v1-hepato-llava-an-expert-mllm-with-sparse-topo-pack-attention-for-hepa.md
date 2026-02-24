---
layout: default
title: Hepato-LLaVA: An Expert MLLM with Sparse Topo-Pack Attention for Hepatocellular Pathology Analysis on Whole Slide Images
---

# Hepato-LLaVA: An Expert MLLM with Sparse Topo-Pack Attention for Hepatocellular Pathology Analysis on Whole Slide Images
**arXiv**：[2602.19424v1](https://arxiv.org/abs/2602.19424) · [PDF](https://arxiv.org/pdf/2602.19424.pdf)  
**作者**：Yuxuan Yang, Zhonghao Yan, Yi Zhang, Bo Yun, Muxi Diao, Guowei Zhao, Kongming Liang, Wenbin Li, Zhanyu Ma  

**一句话要点**：提出Hepato-LLaVA，一种基于稀疏拓扑包注意力的专家多模态大语言模型，用于全切片图像上的肝细胞癌病理分析。

**关键词**：肝细胞癌病理分析, 多模态大语言模型, 稀疏拓扑包注意力, 全切片图像, 医学视觉问答

## 3 点简述
- 核心问题：现有方法因固定分辨率处理和低效特征聚合，导致信息丢失或冗余，影响肝细胞癌诊断。
- 方法要点：引入稀疏拓扑包注意力机制，建模二维组织拓扑，聚合局部证据为语义摘要令牌，保留全局上下文。
- 实验或效果：在肝细胞癌诊断和描述任务上达到最先进性能，显著优于现有方法，并发布临床验证数据集HepatoPathoVQA。

## 摘要（原文）

> Hepatocellular Carcinoma diagnosis relies heavily on the interpretation of gigapixel Whole Slide Images. However, current computational approaches are constrained by fixed-resolution processing mechanisms and inefficient feature aggregation, which inevitably lead to either severe information loss or high feature redundancy. To address these challenges, we propose Hepato-LLaVA, a specialized Multi-modal Large Language Model designed for fine-grained hepatocellular pathology analysis. We introduce a novel Sparse Topo-Pack Attention mechanism that explicitly models 2D tissue topology. This mechanism effectively aggregates local diagnostic evidence into semantic summary tokens while preserving global context. Furthermore, to overcome the lack of multi-scale data, we present HepatoPathoVQA, a clinically grounded dataset comprising 33K hierarchically structured question-answer pairs validated by expert pathologists. Our experiments demonstrate that Hepato-LLaVA achieves state-of-the-art performance on HCC diagnosis and captioning tasks, significantly outperforming existing methods. Our code and implementation details are available at https://pris-cv.github.io/Hepto-LLaVA/.

