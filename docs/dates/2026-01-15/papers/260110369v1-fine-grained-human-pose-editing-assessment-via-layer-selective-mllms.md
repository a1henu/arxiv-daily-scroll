---
layout: default
title: Fine-Grained Human Pose Editing Assessment via Layer-Selective MLLMs
---

# Fine-Grained Human Pose Editing Assessment via Layer-Selective MLLMs
**arXiv**：[2601.10369v1](https://arxiv.org/abs/2601.10369) · [PDF](https://arxiv.org/pdf/2601.10369.pdf)  
**作者**：Ningyu Sun, Zhaolin Cai, Zitong Xu, Peihang Chen, Huiyu Duan, Yichao Yan, Xiongkuo Min, Xiaokang Yang  

**一句话要点**：提出基于层选择性MLLMs的统一框架以解决文本引导人体姿态编辑的评估问题

**关键词**：人体姿态编辑评估, 多模态大语言模型, 层选择性机制, 基准数据集, 对比学习调优, 质量回归

## 3 点简述
- 核心问题：文本引导人体姿态编辑存在结构异常和生成伪影，现有评估指标缺乏细粒度姿态不一致分析
- 方法要点：引入HPE-Bench基准，并基于层选择性MLLMs通过对比LoRA调优和层敏感性分析优化特征层
- 实验或效果：框架在真实性检测和多维质量回归中表现优异，有效连接取证检测与质量评估

## 摘要（原文）

> Text-guided human pose editing has gained significant traction in AIGC applications. However,it remains plagued by structural anomalies and generative artifacts. Existing evaluation metrics often isolate authenticity detection from quality assessment, failing to provide fine-grained insights into pose-specific inconsistencies. To address these limitations, we introduce HPE-Bench, a specialized benchmark comprising 1,700 standardized samples from 17 state-of-the-art editing models, offering both authenticity labels and multi-dimensional quality scores. Furthermore, we propose a unified framework based on layer-selective multimodal large language models (MLLMs). By employing contrastive LoRA tuning and a novel layer sensitivity analysis (LSA) mechanism, we identify the optimal feature layer for pose evaluation. Our framework achieves superior performance in both authenticity detection and multi-dimensional quality regression, effectively bridging the gap between forensic detection and quality assessment.

