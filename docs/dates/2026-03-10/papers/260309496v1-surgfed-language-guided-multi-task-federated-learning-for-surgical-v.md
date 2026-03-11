---
layout: default
title: SurgFed: Language-guided Multi-Task Federated Learning for Surgical Video Understanding
---

# SurgFed: Language-guided Multi-Task Federated Learning for Surgical Video Understanding
**arXiv**：[2603.09496v1](https://arxiv.org/abs/2603.09496) · [PDF](https://arxiv.org/pdf/2603.09496.pdf)  
**作者**：Zheng Fang, Ziwei Niu, Ziyue Wang, Zhu Zhuo, Haofeng Liu, Shuyang Qian, Jun Xia, Yueming Jin  

**一句话要点**：提出SurgFed框架，通过语言引导解决手术视频多任务联邦学习中的组织多样性和任务多样性挑战。

**关键词**：手术视频理解, 多任务联邦学习, 语言引导学习, 组织多样性, 任务交互建模

## 3 点简述
- 核心问题：手术视频联邦学习中，组织多样性和任务多样性导致本地模型适应差和服务器聚合不准确。
- 方法要点：设计语言引导通道选择（LCS）和语言引导超聚合（LHA），利用预定义文本输入增强本地适应和跨站点任务交互。
- 实验或效果：在五个公共数据集上优于现有方法，覆盖四种手术类型，代码已开源。

## 摘要（原文）

> Surgical scene Multi-Task Federated Learning (MTFL) is essential for robot-assisted minimally invasive surgery (RAS) but remains underexplored in surgical video understanding due to two key challenges: (1) Tissue Diversity: Local models struggle to adapt to site-specific tissue features, limiting their effectiveness in heterogeneous clinical environments and leading to poor local predictions. (2) Task Diversity: Server-side aggregation, relying solely on gradient-based clustering, often produces suboptimal or incorrect parameter updates due to inter-site task heterogeneity, resulting in inaccurate localization. In light of these two issues, we propose SurgFed, a multi-task federated learning framework, enabling federated learning for surgical scene segmentation and depth estimation across diverse surgical types. SurgFed is powered by two appealing designs, i.e., Language-guided Channel Selection (LCS) and Language-guided Hyper Aggregation (LHA), to address the challenge of fully exploration on corss-site and cross-task. Technically, the LCS is first designed a lightweight personalized channel selection network that enhances site-specific adaptation using pre-defined text inputs, which optimally the local model learn the specific embeddings. We further introduce the LHA that employs a layer-wise cross-attention mechanism with pre-defined text inputs to model task interactions across sites and guide a hypernetwork for personalized parameter updates. Extensive empirical evidence shows that SurgFed yields improvements over the state-of-the-art methods in five public datasets across four surgical types. The code is available at https://anonymous.4open.science/r/SurgFed-070E/.

