---
layout: default
title: Missing-by-Design: Certifiable Modality Deletion for Revocable Multimodal Sentiment Analysis
---

# Missing-by-Design: Certifiable Modality Deletion for Revocable Multimodal Sentiment Analysis
**arXiv**：[2602.16144v1](https://arxiv.org/abs/2602.16144) · [PDF](https://arxiv.org/pdf/2602.16144.pdf)  
**作者**：Rong Fu, Wenxin Zhang, Ziming Wang, Chunlei Meng, Jiaxuan Lu, Jiekai Wu, Kangan Qian, Hao Zhang, Simon Fong  

**一句话要点**：提出Missing-by-Design框架，通过可验证模态删除实现可撤销多模态情感分析，以应对隐私合规需求。

**关键词**：可撤销多模态分析, 模态删除, 隐私保护, 结构化表示学习, 可验证证书

## 3 点简述
- 核心问题：多模态系统需选择性撤销敏感数据模态，以满足隐私合规和用户自主权要求。
- 方法要点：结合结构化表示学习和可验证参数修改流程，学习属性感知嵌入并基于生成器重建缺失通道。
- 实验或效果：在基准数据集上展示强预测性能，提供实用隐私-效用权衡，替代完全重训练。

## 摘要（原文）

> As multimodal systems increasingly process sensitive personal data, the ability to selectively revoke specific data modalities has become a critical requirement for privacy compliance and user autonomy. We present Missing-by-Design (MBD), a unified framework for revocable multimodal sentiment analysis that combines structured representation learning with a certifiable parameter-modification pipeline. Revocability is critical in privacy-sensitive applications where users or regulators may request removal of modality-specific information. MBD learns property-aware embeddings and employs generator-based reconstruction to recover missing channels while preserving task-relevant signals. For deletion requests, the framework applies saliency-driven candidate selection and a calibrated Gaussian update to produce a machine-verifiable Modality Deletion Certificate. Experiments on benchmark datasets show that MBD achieves strong predictive performance under incomplete inputs and delivers a practical privacy-utility trade-off, positioning surgical unlearning as an efficient alternative to full retraining.

